# 10. 行数のカウント
# 行数をカウントせよ．
# 確認にはwcコマンドを用いよ．

import subprocess

# 「popular-names.txt」を開く
with open('popular-names.txt', 'r') as f:
    # ファイルの読み込み
    text = f.read()
    
    # 行数をカウント
    count = text.count('\n')
    print('行数：{}'.format(count))

# UNIXコマンドを実行して実行結果を確認
# subprocess.run("wc popular-names.txt", shell=True)
# wc：ファイルの行数・単語数・バイト数を表示するコマンド