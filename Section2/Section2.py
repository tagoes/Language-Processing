import subprocess

# 「popular-names.txt」をダウンロード
subprocess.run("wget https://nlp100.github.io/data/popular-names.txt", shell=True)
# Google Colaboratoryの場合は↓
# !wget https://nlp100.github.io/data/popular-names.txt