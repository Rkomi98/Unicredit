// Mini static server (niente process.cwd: evita l'errore uv_cwd del sandbox della preview).
const http = require('http');
const fs = require('fs');
const path = require('path');
const ROOT = '/Users/mirkocalcaterra/Documents/GitHub/Unicredit/gioco';
const PORT = process.env.PORT ? Number(process.env.PORT) : 8123;
const TYPES = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml',
  '.csv': 'text/csv', '.mp3': 'audio/mpeg', '.pdf': 'application/pdf',
  '.md': 'text/markdown; charset=utf-8', '.txt': 'text/plain; charset=utf-8',
  '.json': 'application/json', '.sqlite': 'application/octet-stream', '.xlsx': 'application/octet-stream'
};
http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p === '/' || p === '') p = '/restaurant_game.html';
  const fp = path.join(ROOT, p);
  if (!fp.startsWith(ROOT)) { res.writeHead(403); res.end('forbidden'); return; }
  fs.readFile(fp, (e, data) => {
    if (e) { res.writeHead(404); res.end('not found'); return; }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(fp).toLowerCase()] || 'application/octet-stream' });
    res.end(data);
  });
}).listen(PORT, () => console.log('static server on http://localhost:' + PORT));
