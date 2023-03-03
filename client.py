import requests

server = "http://127.0.0.1:5000"

r = requests.get(server + "/info")
print(r.status_code)
print(r.text)

out_data = {"name": "Shaun", "HDL_value":55}
r = requests.post(server + "/HDL_analysis", json=out_data)
print(r.status_code)
print(r.text)


r = requests.get(server +"/add_two/5/26")
print(r.text)
print(r.json())

out_data = {"a": 2, "b": -3}
r = requests.post(server + "/add", json=out_data)
print(r.status_code)
print(r.text)
if r. status_code == 200:
    x = r.json()
    print(x + 2)
