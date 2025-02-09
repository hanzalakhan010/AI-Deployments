import predictor
from flask import Flask,request,render_template
import numpy as np

app = Flask(__name__)


# ([('no_of_dependents', '0'), ('education', 'ngraduated'),
#  ('self_employed', 'self_employed_yes'), ('income_annum', '4100'), ('loan_amount', '12200'),
#   ('loan_term', '8'), ('cibil_score', '417'), ('residential_assets_value', '2700'),
#  ('commercial_assets_value', '2200'), ('luxury_assets_value', '8800'), ('bank_asset_value', '3300')])
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/application',methods = ['GET','POST'])
def application():
    if request.method == 'POST':

        data = request.form

        prediction = predictor.prediction(data)

        return render_template('application-result.html',
                    prediction = prediction.get("prediction"),
                    probab = prediction.get("probab"),
                    explanations = prediction.get('explanations')
                )
    elif request.method == "GET":
        return render_template('application.html')
@app.route('/dashboard')
def dasboard():
    return render_template('manager_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0')

    