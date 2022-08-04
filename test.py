import json

from bmi_classifier import BMIClassifier


classifier = BMIClassifier()

with open('data/json_data.json') as json_file:
    data_list = json.load(json_file)

classifier.add_patients(data_list)
print("Classifier is working correctly")
print("\nPatients:", classifier.patients)
print("\nOverweight patients:", classifier.overweight_patients)
print("\nOverweight count:", classifier.overweight_patients_count)
classifier.export_data("bmi_classifier_test")
print("\n\nData exported\n")
print("Data:", open('data/bmi_classifier_test.csv').readlines())
