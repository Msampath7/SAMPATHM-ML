from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__,template_folder='templates')

with open('modelj.pkl', 'rb') as m:
    model = pickle.load(m)
# Your machine learning model training code and necessary imports

@app.route('/',methods=['GET','POST'])


def index():
    if request.method == 'POST':
        fixed_acidity = float(request.form['fixed_acidity'])
        volatile_acidity = float(request.form['volatile_acidity'])
        citric_acid = float(request.form['citric_acid'])
        residual_sugars = float(request.form['residual_sugars'])
        chlorides = float(request.form['chlorides'])
        free_sulpher = float(request.form['free_sulpher'])
        total_sulpher = float(request.form['total_sulpher'])
        density=float(request.form['density'])
        ph = float(request.form['ph'])
        sulphates=float(request.form['sulphates'])
        alcohol = float(request.form['alcohol'])

    # Repeat for other features

    # Make prediction
        input_data = [fixed_acidity, volatile_acidity, citric_acid,residual_sugars,chlorides,free_sulpher,total_sulpher,density,ph,sulphates,alcohol] # Use the received data
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        prediction = model.predict(input_data_reshaped)

    # Interpret prediction
        if prediction[0] == 1:
            result = 'Good Quality Wine'
        else:
            result = 'Bad Quality Wine'

        return render_template('index.html', result=result)
        
    return render_template('index.html')

    # Retrieve form data
    

if __name__ == "__main__":
    app.run(debug=True) 
