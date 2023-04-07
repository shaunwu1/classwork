import requests
from image import select_image
from image import convert_image_file_to_base64_string
import base64

server = "http://vcm-21170.vm.duke.edu"


filename = select_image()
image_string = convert_image_file_to_base64_string(filename)


image = {"image": image_string,
            "net_id": "xw172",
            "id_no": 1}
r = requests.post(server + "/add_image", json=image)
print(r.status_code)
print(r.text)


r = requests.get(server + "/get_image/xw172/1")
print(r.status_code)
print(r.text)



def save_b64_image(base64_string):
    image_bytes = base64.b64decode(base64_string)
    with open("sunflower_watermark.jpg", "wb") as out_file:
        out_file.write(image_bytes)
    return


if __name__ == '__main__':
    save_b64_image(r.text)