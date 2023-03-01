import requests


out_data = {"name": "Shaun Wu", "net_id": "xw172",
            "e-mail": "xw172@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json = out_data)

out_data = {"name": "lilshaun", "net_id": "xw172",
            "e-mail": "xw172@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json = out_data)

print(r)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)