class BMIClassifier:
    def __init__(self):
        self.patients = []
        self.overweight_patients = []
        self.overweight_patients_count = 0
        self.last_patient = {}

    def add_patients(self, patients: list):
        """
        Adds the patients to the list of patients.
        :param patients: list of dictionaries with the data of the patients
        :return:
        """
        for patient in patients:
            self.last_patient = patient
            self._classify_patient()
            self.patients.append(self.last_patient)
            self._add_overweight_patient()

    def export_data(self, file_name: str):
        """
        Creates a csv comma separated file with the data of the patients.
        :param file_name: string with name of the file with no extension
        :return:
        """
        with open("data/" + file_name + ".csv", "w") as file:
            for number, patient in enumerate(self.patients):
                if number == 0:
                    file.write(f"{patient.keys()}\n")
                file.write(f"{patient['Gender']},{patient['HeightCm']},{patient['WeightKg']},{patient['BMI']},"
                           f"{patient['BMI Category']},{patient['Health Risk']}\n")

    def _classify_patient(self):
        """
        Classifies the patient based on the BMI value.
        :return:
        """
        # 1. Technical assignment first point
        # Calculate the BMI of the patient
        bmi = round(self.last_patient["WeightKg"] / (self.last_patient["HeightCm"] / 100) ** 2, 1)
        self.last_patient["BMI"] = bmi
        if bmi <= 18.4:
            self.last_patient["BMI Category"] = "Underweight"
            self.last_patient["Health Risk"] = "Malnutrition risk"
        elif 18.5 <= bmi <= 24.9:
            self.last_patient["BMI Category"] = "Normal weight"
            self.last_patient["Health Risk"] = "Low risk"
        elif 25 <= bmi <= 29.9:
            self.last_patient["BMI Category"] = "Overweight"
            self.last_patient["Health Risk"] = "Enhanced risk"
        elif 30 <= bmi <= 34.9:
            self.last_patient["BMI Category"] = "Moderately obese"
            self.last_patient["Health Risk"] = "High risk"
        elif 35 <= bmi <= 39.9:
            self.last_patient["BMI Category"] = "Severely obese"
            self.last_patient["Health Risk"] = "High risk"
        elif bmi >= 40:
            self.last_patient["BMI Category"] = "Very severely obese"
            self.last_patient["Health Risk"] = "Very high risk"

    def _add_overweight_patient(self):
        """
        Adds overweight patients to the list of overweight patients and adds one to overweight patients count if new
        patient is overweight.
        :return:
        """
        if self.last_patient["BMI"] >= 25:
            self.overweight_patients.append(self.last_patient)
            self.overweight_patients_count += 1
    """    
    def _count_overweight_patient(self):
        # 2. Technical assignment second point
        # Count the number of overweight patients
        if self._last_patient["BMI Category"] == "Overweight" \
                or self._last_patient["BMI Category"] == "Moderately obese" \
                or self._last_patient["BMI Category"] == "Severely obese" \
                or self._last_patient["BMI Category"] == "Very severely obese":
            self.overweight_patients_count += 1
            # easy if using dictionary["BMI"] >= 25 as condition
    """