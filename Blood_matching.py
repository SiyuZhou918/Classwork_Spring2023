import requests

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/sz274")

print(r.status_code)
print(r.text)


r1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M7")
print(r1.status_code)
print(r1.text)

r2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F6")
print(r2.status_code)
print(r2.text)

if r1.text == r2.text:
    print("match")
else:
    print("mismatch")


out_data = {"Name": "sz274", "Match":  "No"}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)
print(r.status_code)
print(r.text)