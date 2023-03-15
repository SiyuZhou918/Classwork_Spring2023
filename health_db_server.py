"""
Created on Fri Mar  3 13:07:58 2023

@author: poojap

Database = Dictionary
keys -> ids for the patients
value: dict
{1: {"id": 1, "name": "Pooja", "bloodtype": "O+"},
 2 : {"id": 1, "name": "Pooja", "bloodtype": "O+"},
 3: {"id": 1}, "name": "Pooja", "bloodtype": "O+", "tests": []}o
 }
"""

from flask import Flask, request, jsonify

db = {}

app = Flask(__name__)
def add_patient_to_db(ids, name, blood_type):
    new_patient = {"id": ids,
                   "name": name,
                   "blood_type": blood_type}
    db[ids] = new_patient


@app.route("/new_patient", methods = ["POST"])
def post_new_patient():
    # get input data
    in_data = request.get_json()
    answer, status_cdoe = new_patient_driver(in_data)
    return jsonify(answer), status_code
    # Call other functions to do the work
    # Return a response


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
    does_id_exist = does_patient
    
def new_patient_driver(in_data):
    # vALIDATE INPUT
    validation = validate_input_data(in_data)
    if validation is not True:
        return validation, 400
    # DO the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # Return an answer
    return "Patient Succesffully added", 200


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


if __name__ =="__main__":
    app.run()

    



