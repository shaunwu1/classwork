from flask import Flask, request, jsonify
from pymodm import connect
from pymodm import MongoModel, fields
from PatientModel import Patient
import logging

db = {}

app = Flask(__name__)

def init_server():
    logging.basicConfig(filename = "server.log", filemode='w')
    connect("mongodb+srv://shaunwu1:shaunwu200@bme547.auwrcbj.mongodb.net/"
            "health_db_2023?retryWrites=true&w=majority")
    
def add_patient_to_db(patient_id, patient_name, blood_type):
    # new_patient = {"id": id,
    #                "name": name,
    #                "blood_type": blood_type,
    #                "tests": []}
    # db[id] = new_patient
    # print(db)
    new_patient = Patient(patient_id = patient_id,
                          patient_name = patient_name,
                          blood_type = blood_type)
    saved_patient = new_patient.save()
    return saved_patient

def add_test(patient_id, test_name, test_result):
    # test = {"id": id,
    #         "test_name": test_name,
    #         "test_result": test_result}
    # db[id]["tests"].append((test_name, test_result))
    # print(db)
    x = Patient.objects.raw({"_id": patient_id}.first())
    x.tests.append((test_name, test_result))
    x.save()

@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    in_data = request.get_json()
    answer = new_patient_driver(in_data)
    return jsonify(answer)

def new_patient_driver(in_data):
    validation = validate_input_data(in_data)
    if validation is not True:
        return validation, 400
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    return "Patient successfully added", 200


def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


@app.route("/add_test", methods = ["POST"])
def post_add_test():
    in_data = request.get_json()
    answer, status_code = add_test_driver(in_data)
    return jsonify(answer), status_code

def does_patient_exist_in_db(id):
    if id in db:
        return True
    else:
        return False

def add_test_driver(in_data):
    validation = validate_input_data_add_test(in_data)
    if validation is not True:
        return validation, 400
    does_id_exist = does_patient_exist_in_db(in_data["id"])
    if does_id_exist is False:
        return "Patient id {} does not exist in database".format(in_data["id"]), 400
    add_test(in_data["id"], in_data["test_name"], in_data["test_result"])
    return "Test successfully added", 200


def validate_input_data_add_test(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results_driver(patient_id):
    print(patient_id)
    answer, status = get_results_driver(patient_id)
    return jsonify(answer), status

def get_results_driver(patient_id):
    validation = validate_patient_id_from_get(patient_id)
    if validation is not True:
        return validation, 400
    patient = db[int(patient_id)]
    print(patient)
    return patient["tests"], 200

def validate_patient_id_from_get(patient_id):
    try:
        patient_num = int(patient_id)
    except ValueError:
        print("Error")
        return "Patient_id should be an integer"
    if does_patient_exist_in_db(patient_num) is False:
        return "Patient_id of {} does not exist in database".format(patient_num)
    return True

if __name__ == '__main__':
    app.run()