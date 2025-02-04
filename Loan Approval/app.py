from joblib import load
from flask import Flask,request,render_template
model = load('./models/model_v1.joblib')

app = Flask(__name__)



@app.route('/application')
def application():
    if request.method == 'POST':
        data = request.form
        print(data)
    elif request.method == "GET":
        return render_template('application.html')

if __name__ == '__main__':
    app.run(debug=True)

    