# 11.タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import subprocess

# 「popular-names.txt」を開く
with open('popular-names.txt', 'r') as f:
    # ファイルの読み込み
    text = f.read()

    # タブをスペースに置換
    print(text.replace('\t', ' '))

# UNIXコマンドを実行して実行結果を確認
# subprocess.run("sed 's/\t/ /g' popular-names.txt", shell=True)
# subprocess.run("tr '\t' ' ' < popular-names.txt", shell=True)
# subprocess.run("expand -t 1 popular-names.txt", shell=True)
# sed：行単位でテキストを編集するコマンド