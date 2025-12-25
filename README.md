# Python CGI Sample

Python CGI を使って、Webの入出力と
ファイル操作を構造化して実装したサンプルです。

```text
└── cgi-sample
    ├── index.html
    ├── cgi-bin
    │   ├── data_store.py      # データ保存処理
    │   ├── post_form.py       # POSTフォーム処理
    │   ├── search_form.py     # 検索フォーム処理
    │   └── test.py            # 動作確認用
    ├── data
    │   └── messages.txt       # 保存データ
    └── README.md
```
## 実行方法
$ python -m http.server 8080 --cgi

詳細は次のページを参照してください。<br/>
https://qiita.com/isy-nishida/items/5602bd8997131b76ccaf <br/>
Python CGI その3：単体テストという考え方 
