#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Máquina de Produtos Digitais — servidor local do painel (SQLite). Só Python padrão.
Uso: python painel-server.py  (ou duplo clique em iniciar-painel.bat / .command)
Abre em http://localhost:8767 — edições e drag&drop salvam no maquina.db."""
import json, sqlite3, os, sys, webbrowser
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PASTA = os.path.dirname(os.path.abspath(__file__))
os.chdir(PASTA)
DB = os.path.join(PASTA, 'maquina.db')
PORTA = 8767
CONFIG = os.path.join(PASTA, 'maquina-config.json')

CAMPOS = ['slug', 'titulo', 'habilidade', 'publico', 'etapa', 'problema', 'promessa',
          'produto', 'paginaArq', 'compradores', 'lancamento', 'validacao',
          'formato', 'preco', 'criadoEm']

def conexao():
    c = sqlite3.connect(DB)
    c.execute('''CREATE TABLE IF NOT EXISTS projetos(
        slug TEXT PRIMARY KEY, titulo TEXT, habilidade TEXT, publico TEXT,
        etapa TEXT DEFAULT 'problema',
        problema TEXT, promessa TEXT, produto TEXT,
        paginaArq TEXT, compradores TEXT, lancamento TEXT, validacao TEXT,
        formato TEXT, preco REAL,
        criadoEm TEXT DEFAULT (datetime('now','localtime')),
        atualizado TEXT DEFAULT (datetime('now','localtime')))''')
    for col, tipo in [('titulo', 'TEXT'), ('habilidade', 'TEXT'), ('publico', 'TEXT'),
                      ('problema', 'TEXT'), ('promessa', 'TEXT'), ('produto', 'TEXT'),
                      ('paginaArq', 'TEXT'), ('compradores', 'TEXT'), ('lancamento', 'TEXT'),
                      ('validacao', 'TEXT'), ('formato', 'TEXT'), ('preco', 'REAL'),
                      ('criadoEm', 'TEXT')]:
        try: c.execute('ALTER TABLE projetos ADD COLUMN %s %s' % (col, tipo))
        except sqlite3.OperationalError: pass
    return c

def ler_config():
    try: return json.load(open(CONFIG, encoding='utf-8'))
    except Exception: return {}

def importar_snapshot():
    """Primeira execução sem banco: importa os projetos embutidos no painel.html."""
    try:
        html = open(os.path.join(PASTA, 'painel.html'), encoding='utf-8').read()
        ini = html.index('<script id="dados" type="application/json">') + len('<script id="dados" type="application/json">')
        fim = html.index('</script>', ini)
        dados = json.loads(html[ini:fim])
        c = conexao()
        for p in dados.get('projetos', []):
            c.execute('INSERT OR IGNORE INTO projetos (%s) VALUES (%s)' % (','.join(CAMPOS), ','.join('?' * len(CAMPOS))),
                      [p.get(k) for k in CAMPOS])
        c.commit(); c.close()
        print('Snapshot importado do painel.html para o maquina.db')
    except Exception as e:
        print('(sem snapshot para importar: %s)' % e)

class App(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        super().end_headers()
    def _json(self, code, obj):
        corpo = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', str(len(corpo)))
        self.end_headers(); self.wfile.write(corpo)
    def _corpo(self):
        n = int(self.headers.get('Content-Length', 0))
        return json.loads(self.rfile.read(n).decode('utf-8')) if n else {}
    def do_GET(self):
        if self.path.split('?')[0] == '/api/config':
            return self._json(200, ler_config())
        if self.path.split('?')[0] == '/api/projetos':
            c = conexao(); c.row_factory = sqlite3.Row
            rows = [dict(r) for r in c.execute('SELECT * FROM projetos ORDER BY atualizado DESC').fetchall()]; c.close()
            return self._json(200, rows)
        if self.path in ('/', ''):
            dh = os.path.join(PASTA, 'painel.html')
            tp = os.path.join(PASTA, 'painel-template.html')
            if os.path.exists(tp):
                import datetime as _dt
                c = conexao(); c.row_factory = sqlite3.Row
                _projs = [dict(r) for r in c.execute('SELECT * FROM projetos ORDER BY atualizado DESC').fetchall()]; c.close()
                _t = open(tp, encoding='utf-8').read().replace('__DADOS__',
                    json.dumps({'atualizado': _dt.datetime.now().strftime('%d/%m/%Y %H:%M'), 'projetos': _projs}, ensure_ascii=False))
                open(dh, 'w', encoding='utf-8').write(_t)
            self.path = '/painel.html'
        return SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
        if self.path.split('?')[0] == '/api/projetos':
            p = self._corpo(); c = conexao()
            c.execute('INSERT OR REPLACE INTO projetos (%s) VALUES (%s)' % (','.join(CAMPOS), ','.join('?' * len(CAMPOS))),
                      [p.get(k) for k in CAMPOS])
            c.commit(); c.close(); return self._json(200, {'ok': True})
        return self._json(404, {'erro': 'rota'})
    def do_PUT(self):
        partes = self.path.split('?')[0].split('/')
        if len(partes) == 4 and partes[1] == 'api' and partes[2] == 'projetos':
            slug, ch = partes[3], self._corpo()
            sets = [k for k in ch if k in CAMPOS and k != 'slug']
            if sets:
                c = conexao()
                c.execute('UPDATE projetos SET %s, atualizado=datetime("now","localtime") WHERE slug=?' %
                          ','.join('%s=?' % k for k in sets), [ch[k] for k in sets] + [slug])
                c.commit(); c.close()
            return self._json(200, {'ok': True})
        return self._json(404, {'erro': 'rota'})
    def do_DELETE(self):
        partes = self.path.split('?')[0].split('/')
        if len(partes) == 4 and partes[1] == 'api' and partes[2] == 'projetos':
            c = conexao(); c.execute('DELETE FROM projetos WHERE slug=?', (partes[3],)); c.commit(); c.close()
            return self._json(200, {'ok': True})
        return self._json(404, {'erro': 'rota'})
    def log_message(self, *a): pass

if __name__ == '__main__':
    novo = not os.path.exists(DB)
    conexao().close()
    if novo: importar_snapshot()
    print('Painel rodando em http://localhost:%d  (Ctrl+C para parar)' % PORTA)
    try: webbrowser.open('http://localhost:%d' % PORTA)
    except Exception: pass
    try: ThreadingHTTPServer(('127.0.0.1', PORTA), App).serve_forever()
    except KeyboardInterrupt: print('\nEncerrado.')
