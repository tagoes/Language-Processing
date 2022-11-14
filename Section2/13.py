# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

import subprocess

# 「col1.txt」「col2.txt」「merge.txt」を開く
with open('col1.txt', 'r') as f1, \
     open('col2.txt', 'r') as f2, \
     open('merge.txt', 'w') as f3:
    # 行単位で処理
    for (line1, line2) in zip(f1.read().splitlines(), f2.readlines()):
        # col1.txtとcol2.txtをタブ区切りでマージしてファイルに書き込み
        f3.write(line1 + '\t' + line2)

# UNIXコマンドを実行して実行結果を確認
# subprocess.run("paste col1.txt col2.txt", shell=True)
# paste：複数のファイルを行単位で連結するコマンド