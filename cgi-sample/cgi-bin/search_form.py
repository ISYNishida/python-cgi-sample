#!/usr/bin/env python3
import cgi
import cgitb
from data_store import search_by_name

cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
keyword = form.getvalue("name", "")

print("<html><body>")
print("<h1>投稿検索</h1>")

print("""
<form method="get">
  名前：<input type="text" name="name">
  <input type="submit" value="検索">
</form>
<hr>
""")

if keyword:
    results = search_by_name(keyword)
    print(f"<h2>検索結果（{len(results)}件）</h2>")
    for r in results:
        print(f"<p>{r['name']} : {r['comment']}</p>")

print("</body></html>")

