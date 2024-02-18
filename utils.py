import config
import pickle
import json
import numpy as np
import pandas as pd

model = pickle.load(open(config.MODEL_path, 'rb'))
project_data = json.load(open(config.PROJECT_path, 'r'))

columns = project_data['Columns']

def get_prediction(data):

    gender           =    data['gender']
    smoker           =    data['smoker']
    region           =    data['region']

    gender = project_data['gender'].get(gender)
    smoker = project_data['smoker'][smoker]

    region = 'region_' + region
    region_index = columns.index(region)

    test_array = np.zeros(len(columns))

    test_array[0] = eval(data['age'])
    test_array[1] = gender
    test_array[2] = eval(data['bmi'])
    test_array[3] = int(eval(data['children']))
    test_array[4] = smoker
    test_array[region_index] = 1

    test_df = pd.DataFrame([test_array], columns=columns)

    predicted_charges = np.around(model.predict(test_df)[0], 3)
    return predicted_charges