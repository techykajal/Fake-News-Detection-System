from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing



loaded_model = pickle.load(open('model.pkl', 'rb'))
dataframe = pd.read_csv(r'C:\Users\Kajal\Desktop\Projects\Fake_News\Fake-News-Detection-System\Data Pre-processing\Cleaned_Data.csv')

tf_vector = TfidfVectorizer(sublinear_tf=True)
tf_vector.fit(dataframe['Processed_Content'])

X_text = tf_vector.transform(dataframe['Processed_Content'].ravel())
y_values = np.array(dataframe['label'].ravel())


le = preprocessing.LabelEncoder()
le.fit(y_values).transform(y_values)

x_train,x_test,y_train,y_test = train_test_split(X_text,y_values,test_size=0.2,random_state=0)

app = Flask(__name__)

def fake_news_det(news):
    input_data = [news]
    vectorized_input_data = tf_vector.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        pred = fake_news_det(message)
        print(pred)
        return render_template('index.html', prediction=pred)
    else:
        return render_template('index.html', prediction="Something went wrong")

if __name__ == '__main__':
    app.run(debug=True)