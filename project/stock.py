import requests

webhook_id = res['id']
# List webhook
r = requests.get('https://finnhub.io/api/v1/webhook/list?token=c1chfjf48v6vbcpf1ae0')
res = r.json()
print(res)