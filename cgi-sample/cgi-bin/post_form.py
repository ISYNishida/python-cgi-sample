#!/usr/bin/env python3
import cgi
import cgitb
import html

cgitb.enable()  # CGI デバッグ用

from data_store import save_message, load_messages

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
name = form.getfirst("name", "")
comment = form.getfirst("comment", "")

# POSTされたデータがあれば保存
if name and comment:
    save_message(
        html.escape(name),
        html.escape(comment)
    )

# 全データを読み出す
messages = load_messages()

# HTML 出力
print("""
<html>
<head>
<meta charset="utf-8">
<title>Python CGI Message Board</title>
</head>
<body>
<h1>Python CGI Message Board</h1>

<form method="POST" action="/cgi-bin/post_form.py">
    名前: <input type="text" name="name"><br>
    ひとこと: <input type="text" name="comment"><br>
    <input type="submit" value="投稿">
</form>

<hr>
<h2>投稿一覧</h2>
<ul>
""")

for m in messages:
    print(f"<li><strong>{m['name']}:</strong> {m['comment']}</li>")

print("""
</ul>
</body>
</html>
""")

