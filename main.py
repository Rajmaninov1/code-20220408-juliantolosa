import json

from fastapi import FastAPI

from bmi_classifier import BMIClassifier

app = FastAPI()

classifier = BMIClassifier()


@app.get("/test_classifier")
async def test_classifier():
    # 3. Technical assignment third point
    # Test the classifier with the data from the json file
    with open('data/json_data.json') as json_file:
        data_list = json.load(json_file)

    classifier.add_patients(data_list)
    return {
        "message": "Classifier is working correctly",
        "status": "success",
        "Patients": classifier.patients,
        "Overweight patients": classifier.overweight_patients,
        "Overweight count": classifier.overweight_patients_count
    }


@app.get("/add_patient")
async def add_patient(gender: str, height: int, weight: int):
    patient_data = [{"Gender": gender, "HeightCm": height, "WeightKg": weight}]
    classifier.add_patients(patient_data)
    return {
        "message": "Patient added correctly",
        "status": "success",
        "data entered": classifier.last_patient,
    }


@app.get("/get_patients")
async def get_patients():
    if len(classifier.patients) > 0:
        return {
            "message": "Patients found",
            "status": "success",
            "data": classifier.patients,
        }
    else:
        return {
            "message": "There is no patients. Add some patients first",
            "status": "error"
        }


@app.get("/get_overweight_patients")
async def export_data():
    if len(classifier.overweight_patients) > 0:
        return {
            "message": "Patients found",
            "status": "success",
            "data": classifier.overweight_patients,
        }
    else:
        return {
            "message": "There is no overweight patients",
            "status": "error"
        }


@app.get("/get_overweight_patients_count")
async def get_overweight_patient_count():
    return {
        "message": "Overweight patients count",
        "status": "success",
        "count": classifier.overweight_patients_count
    }


@app.get("/export_data")
async def export_data():
    if len(classifier.patients) > 0:
        return {
            "message": "Data exported",
            "status": "success",
            "data": classifier.patients,
        }
    else:
        return {
            "message": "No data to export. Add patients first",
            "status": "error"
        }


@app.get("/visualize_exported_data")
async def visualize_exported_data():
    try:
        return {
            "message": "Data exists",
            "status": "success",
            "data": open('data/bmi_classifier_test.csv').readlines(),
        }
    except FileNotFoundError:
        return {
            "message": "No data to visualize",
            "status": "Error. Export data first",
            "error": "FileNotFoundError",
        }
