from flask import Flask, request, render_template
import sklearn
import utils
import config

app = Flask(__name__)


@app.route('/')
def index():
    gender = ['female', 'male']
    smoker = ['no', 'yes']
    region = ['southeast', 'southwest', 'northwest', 'northeast']

    gender.insert(0, 'Select Gender')
    region.insert(0, 'Select Region')

    return render_template('index.html', gender=gender, smoker=smoker, region=region)

@app.route('/predict', methods = ['POST'])
def predict():
    user_data = request.form

    prediction = utils.get_prediction(user_data)

    return str(prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= config.PORT_numner)