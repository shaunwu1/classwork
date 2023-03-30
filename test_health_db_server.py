from pymodm import connect
from PatientModel import Patient

connect("mongodb+srv://shaunwu1:shaunwu200@bme547.auwrcbj.mongodb.net/"
            "health_db_2023?retryWrites=true&w=majority")

def test_add_patient_to_db():
    from health_db_server import add_patient_to_db
    patient_id = 234
    patient_name = "Test"
    blood_type = "O+"
    answer = add_patient_to_db(patient_id, patient_name, blood_type)
    assert answer.patient_id == patient_id

def test_add_test():
    from health_db_server import add_test
    patient_id = 123
    patient_name = "Test"
    patient_blood_type = "O+"
    from health_db_server import add_patient_to_db
    add_patient_to_db(patient_id, patient_name, patient_blood_type)
    test_name = "HDL"
    test_value = 150
    
    
    
    add_test(patient_id, test_name, test_value)
    
    
    from health_db_server import db
    answer = db[patient_id]["tests"][-1]
    expected = (test_name, test_value)
    db.clear()
    assert answer == expected

