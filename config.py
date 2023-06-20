import os

base_path = os.getcwd()

CSV_path = os.path.join(base_path, r'CSV_Files/cleaned_medical_insurance_data.csv')

MODEL_path = os.path.join(base_path, r'artifacts/linear_reg_model.pkl')

PROJECT_path = os.path.join(base_path, r'artifacts/project_data.json')

PORT_numner = 8080