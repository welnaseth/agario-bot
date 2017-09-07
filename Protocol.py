import requests

ipRequestString = '\n\x0e\n\nUS-Atlanta\x12\x00'.encode('utf-8')
ipResponse = requests.post(url="http://m.agar.io/v2/findServer", data = ipRequestString)

tokenRequestString = '\n\x14\n\x10US-Atlanta:party\x12\x00'.encode('utf-8')
tokenResponse = requests.post(url="http://m.agar.io/v2/createToken", data = tokenRequestString)

print(ipResponse.content)
print(tokenResponse.content)
