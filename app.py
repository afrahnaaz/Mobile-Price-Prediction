from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))


@app.route('/',methods=['GET','POST'])
def homePage():
    return render_template('ai.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        try:
            RAM = int(request.form['a'])
            ROM = int(request.form['b'])
            MS = float(request.form['c'])
            PC = int(request.form['d'])
            SC = int(request.form['e'])
            BC = int(request.form['f'])
            features = [RAM, ROM, MS, PC, SC, BC]
            inpData = pd.DataFrame(columns=cols)
            inpData.loc[0] = features
            prediction = model.predict(inpData)[0]
        except:
            prediction = 'Invalid Input'
        return render_template('ai.html', predictiont='Predicted Price is {}'.format(prediction))

if __name__ == '__main__':
    cols=['RAM', 'ROM', 'Mobile_Size', 'Primary_Cam', 'Secondary_Cam',
                'Battery_Power']
    app.run(debug=True)