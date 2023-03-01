import requests


r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/xw172")
print(r.text)
a = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F6")
print(a.text)
b = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M8")
print(b.text)

if a.text == b.text:
    answer = "Yes"
else:
    answer = "No"

out_data = {"Name": "xw172", "Match": answer}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                  json = out_data)
print(r.text)

