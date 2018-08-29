import requests
r = 100

url = "https://apidocs.sendinblue.com/api-status/"
for i in range(r):
    res = requests.get(url.format(i))
    delay = res.headers.get("DELAY")
    d = res.headers.get("DATE")
    print("{}:{} delay {} iterador {}".format(d, res.url, delay, i))