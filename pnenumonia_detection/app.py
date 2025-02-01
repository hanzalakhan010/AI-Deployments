import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Load your pre-trained model
model = load_model('model/pneumonia_model_1.h5')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_image(img_path):
    # Resize and preprocess the image to match model input
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust size to your model's input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize (if your model expects [0,1])
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        
        # Preprocess and predict
        img_array = preprocess_image(save_path)
        prediction = model.predict(img_array)
        probability = float(prediction[0][0])  # For binary classification (sigmoid output)
        
        # Example: Pneumonia detection (adjust classes to your use case)
        result = "Pneumonia Detected" if probability > 0.5 else "Normal"
        return render_template('index.html', 
                               result=result, 
                               probability=probability, 
                               img_path=save_path)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0')