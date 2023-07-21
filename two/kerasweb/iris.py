from flask import Flask,render_template,request
from keras.models import load_model
import numpy as np

app = Flask(__name__)

# http://호스트:포트/주소
# hyper text transfer protocol

@app.route('/',methods=['GET'])
def main():
    return render_template('iris/input.html')

@app.route('/iris_result',methods=['POST'])
def iris_result():
    flowers = ['setosa', 'versicolor', 'virginica']
    # 신경망 모형 불러오기
    model = load_model('c:/workspace/hw_study3/data/iris/iris.h5')

    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    d = float(request.form['d'])

    # 2차원 배열로 학습시켰기 때문에 2차원 배열로 만들기
    test_set = [[a, b, c, d]]

    pred=model.predict(test_set)
    n=np.argmax(pred,axis=1)
    result=flowers[n[0]]
    return render_template('iris/iris_result.html', result=result,a=a,b=b,c=c,d=d)

if __name__ == '__main__':
    # 플라스크 앱 실행
    app.run(port=8000, threaded=False)