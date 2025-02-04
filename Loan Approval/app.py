import predictor
from flask import Flask,request,render_template
import numpy as np

app = Flask(__name__)


# ([('no_of_dependents', '0'), ('education', 'ngraduated'),
#  ('self_employed', 'self_employed_yes'), ('income_annum', '4100'), ('loan_amount', '12200'),
#   ('loan_term', '8'), ('cibil_score', '417'), ('residential_assets_value', '2700'),
#  ('commercial_assets_value', '2200'), ('luxury_assets_value', '8800'), ('bank_asset_value', '3300')])


@app.route('/application',methods = ['GET','POST'])
def application():
    if request.method == 'POST':

        data = request.form

        result = predictor.prediction(data=data)  
        # explanations = predictor.rejectionReasons(data = data)
        
        return render_template('application-result.html',
                    prediction = result,

                )
    elif request.method == "GET":
        return render_template('application.html')

if __name__ == '__main__':
    app.run(debug=True)

    