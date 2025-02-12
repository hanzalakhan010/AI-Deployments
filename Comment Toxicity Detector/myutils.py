import numpy as np
from tensorflow.keras.layers import TextVectorization
import pandas as pd
df = pd.read_csv('./datasets/train.csv')

X = df['comment_text']
MAX_FEATURES = 20000

vectorizer = TextVectorization(
    max_tokens = MAX_FEATURES,
    output_sequence_length = 1800,
    output_mode = 'int'
)
vectorizer.adapt(X.values)



def processPrediction(prediction):
    if prediction.shape[1] == 6:
        result = {
            'toxic':True if prediction[0][0]>.5 else False,
            'severe_toxic':True if prediction[0][1]>.5 else False,
            'obscene':True if prediction[0][2]>.5 else False,
            "threat":True if prediction[0][3]>.5 else False,
            "insult":True if prediction[0][4]>.5 else False,
            "identity_hate":True if prediction[0][5]>.5 else False
        }
        return result
    else:
        return False