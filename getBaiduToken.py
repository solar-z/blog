import os

print(os.environ)

baiduToken = os.environ["BAIDU_TOKEN"]
with open('./_config.yml','+r') as f:
    t = f.read()
    t = t.replace('${{ secrets.BAIDU_TOKEN }}', baiduToken)

    print(t)

    f.seek(0, 0)
    f.write(t)

    f.truncate()

GitalkToken = os.environ["GITALK_TOKEN"]
GitalkId = os.environ["GITALKID"]
with open('./_config.butterfly.yml','+r') as f:
    t = f.read()
    t = t.replace('${{ secrets.GITALK_TOKEN }}', GitalkToken)
    t = t.replace('${{ secrets.GITALKID }}', GitalkId)

    print(t)

    f.seek(0, 0)
    f.write(t)

    f.truncate()