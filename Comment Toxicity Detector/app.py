from flask import Flask,request,render_template
from tensorflow.keras.models import load_model
from myutils import vectorizer,processPrediction

app = Flask(__name__)


model = load_model('./model/model.h5')


@app.route('/')
def mainPage():
    return render_template('mainPage.html')

@app.route('/detect',methods = ['POST'])
def detect():
    comment = request.headers.get('comment')
    vectorized_text = vectorizer([comment])
    prediction = model.predict(vectorized_text)
    return {'result':processPrediction(prediction=prediction)}


if __name__ == '__main__':
    app.run(debug=True)