import requests

out_data = {"user": "su44", "message": "hello suraj"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json = out_data)
print(r.text)


r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/xw172")
print(r.text)