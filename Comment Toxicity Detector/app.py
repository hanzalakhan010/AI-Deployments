# from flask import Flask,request,render_template
from joblib import load
# from tensorflow.keras.models import load_model

# from pathlib import Path

# print(Path('./models/model.joblib').is_file())


# app = Flask(__name__)

vectorizer = load('./models/vectorizer.joblib')

# model = tf.keras.model.load_model('./models/model.h5')



# @app.route('/')
# def mainPage():
#     return render_template('mainPage.html')

# @app.route('/detect',methods = ['POST'])
# def detect():
#     comment = request.headers.get('comment')
#     vectorized_text = vectorizer([comment])
#     prediction = model.predict(vectorized_text)
#     return prediction


# if __name__ == '__main__':
#     app.run(debug=True)