import requests

city = "贵阳"
url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
res = requests.get(url).json()
print(res)
weather = res['data']['list'][0]
print(weather)