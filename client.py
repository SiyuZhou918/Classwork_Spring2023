import requests

server = "http://127.0.0.1:5000"

r = requests.get(server + "/info")
print(r.status_code)
print(r.text)

out_data = {"name":"David", "HDL_value":65}
r = requests.post(server + "/HDl_analysis", json=out_data)
print(r.status_code)
print(r.text)

r = requests.get(server + "/add_two/five/26")
print(r.status_code)
print(r.json())


out_data = {"a":2, "b":-3}
r = requests.post(server + "/add", json=out_data)
print(r.status_code)
print(r.text)