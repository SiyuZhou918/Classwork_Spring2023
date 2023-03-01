import requests

# out_data = {"user": "sz274", "message": "Hi! This is Siyu here."}
# r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=out_data)
# print(r.status_code)
# print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/nh170")
print(r.text)
