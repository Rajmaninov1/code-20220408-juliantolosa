# BMI Classifier

___

Created by [Julian Tolosa (Rajmaninov1)](https://github.com/rajmaninov1)

___

To run the program you have two options:

- Docker (With FastAPI)
- Local (Python test script only)

### Docker

If you want to run the program with FastAPI in a Docker container on 80, you have 
to use the following commands:

~~~bash
docker build -t bmi_classifier .
~~~

~~~bash
docker run -d -p 80:80 --name bmi_classifier bmi_classifier
~~~

#### List of working urls

- http://localhost:80/test_classifier
- http://localhost:80/add_patient?gender=Male&height=167&weight=62
- http://localhost:80/get_patients
- http://localhost:80/get_overweight_patients
- http://localhost:80/get_overweight_patients_count
- http://localhost:80/export_data
- http://localhost:80/visualize_exported_data

### Local

If you want to run the program locally, you have to use the following command:

~~~bash
python bmi_classifier.py
~~~

