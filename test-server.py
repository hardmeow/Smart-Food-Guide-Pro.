#!/usr/bin/env python3
"""
简单的 HTTP 服务器，用于本地测试 smartfood-scanner.html
运行: python3 test-server.py
然后访问: http://localhost:8000/smartfood-scanner.html
"""

import http.server
import socketserver
import os

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"✅ 服务器运行在 http://localhost:{PORT}/")
    print(f"📱 打开浏览器访问: http://localhost:{PORT}/smartfood-scanner.html")
    print("按 Ctrl+C 停止服务器")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 服务器已停止")
