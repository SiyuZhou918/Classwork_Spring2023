import requests

# server = "https://vcm-21179.vm.duke"

out_data = {"name": "Siyu Zhou", "net_id": "sz274",
            "e-mail": "siyu.zhou@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.status_code)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)
