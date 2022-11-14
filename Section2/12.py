# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

import subprocess

# 「popular-names.txt」「col1.txt」「col2.txt」を開く
with open('popular-names.txt', 'r') as f1, \
     open('col1.txt', 'w') as f2, \
     open('col2.txt', 'w') as f3:
    # 行単位で処理
    for line in f1.readlines():
        # 文字列をタブ区切りで分割
        col = line.split('\t')

        # 1列目をcol1.txtとして保存
        f2.write(col[0] + '\n')
        
        # 2列目をcol2.txtとして保存
        f3.write(col[1] + '\n')

# UNIXコマンドを実行して実行結果を確認
# subprocess.run("cut -f 1 popular-names.txt", shell=True)
# subprocess.run("cut -f 2 popular-names.txt", shell=True)
# cut：ファイルを行単位で分割するコマンド