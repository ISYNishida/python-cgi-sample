# Python CGI Sample

Python CGI を使って、Webの入出力と
ファイル操作を構造化して実装したサンプルです。

## 構成
└── cgi-sample
    ├── cgi-bin
    │   ├── data_store.py
    │   ├── post_form.py
    │   ├── search_form.py
    │   └── test.py
    ├── data
    │   └── messages.txt
    └── README.md

## 実行方法
$ python -m http.server 8080 --cgi

詳細は以下を参照してください。
https://qiita.com/isy-nishida/items/5602bd8997131b76ccaf
Python CGI その3：単体テストという考え方
