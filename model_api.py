from flask import Flask,request,jsonify
import joblib
import pandas as  pd

# CREATE THE FLASK APP
app = Flask(__name__)

# CONNECT POST API CALL --> predict() function
@app.route('/predict',methods=['POST'])

def predict():

    # GET JSON REQUEST
    feat_data = request.json

    # CONVERT JSON TO PANDAS DF (col names)
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)

    # PREDICT
    prediction = list(model.predict(df))

    # RETURN THE PREDICTION
    return jsonify({'prediction':str(prediction)})

# LOAD MY MODEL and SETUP COLUMN NAMES
if __name__ == '__main__':
    model = joblib.load('final_model.pkl')
    col_names = joblib.load('col_names.pkl')

    app.run(debug=True)