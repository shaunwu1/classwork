from tkinter import filedialog
import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import flask
from flask import Flask, jsonify, request

app = Flask(__name__)
db = {}

def select_image():
    filename = filedialog.askopenfilename(initialdir="images")
    return filename


def convert_image_file_to_base64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def new_image_driver(in_data):
    image = {"net_id": in_data["net_id"],
             "id_no": in_data["id_no"],
             "image_string": in_data["image"]}
    db[in_data["id_no"]] = image
    return "Image successfully uploaded", 200


def get_image_driver(net_id, id_no):
    image = db[id_no]["image_string"]
    return image, 200


def main():
    filename = select_image()
    if filename == "":
        return
    b64_image = convert_image_file_to_base64_string(filename)
    print(b64_image)


@app.route("/add_image", methods=["POST"])
def post_add_image():
    in_data = request.get_json()
    answer, stat_code = new_image_driver(in_data)
    return jsonify(answer), stat_code


@app.route("/get_image/<net_id>/<id_no>", methods=["GET"])
def get_image(net_id, id_no):
    answer, stat_code = get_image_driver(net_id, id_no)
    return jsonify(answer), stat_code

if __name__ == "__main__":
    main()