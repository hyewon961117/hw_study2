from flask import Flask, render_template, request
from keras.models import load_model
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('ozone/input.html')

@app.route('/result', methods=['POST'])
def result():
    model = load_model('c:/workspace/hw_study3/data/ozone/ozone.h5')
    scaler = joblib.load('c:/workspace/hw_study3/data/ozone/scaler.model')
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    test_set = [[a,b,c]]
    test_set = scaler.transform(test_set)
    rate = model.predict(test_set)
    if rate[0][0] >= 0.5:
        result='충분'
    else:
        result='부족'
    return render_template('ozone/result.html',
                           rate='{:.2f}%'.format(rate[0][0]*100),
                           result=result, a=a, b=b, c=c)

if __name__ == '__main__':
    # 웹브라우저에서 실행할 때 http://localhost로 하면 느림
    # http://127.0.0.1로 할 것
    app.run(port=8000, threaded=False)