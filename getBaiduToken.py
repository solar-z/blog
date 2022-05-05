import os

baiduToken = os.environ["BAIDU_TOKEN"]
with open('./_config.yml','+r') as f:
    t = f.read()
    t = t.replace('${{ secrets.BAIDU_TOKEN }}', baiduToken)

    print(t)

    f.seek(0, 0)
    f.write(t)

    f.truncate()