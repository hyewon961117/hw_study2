from flask import Flask, Markup, render_template, request
app = Flask(__name__)

@app.route('/gugu',methods=['GET'])
def main():
    return render_template('gugu/gugu.html')
    # 탬플릿을 가지고 html을 생성 () 링크 출력

@app.route('/gugu_result', methods=['POST'])
def gugu_result():
    dan = int(request.form['dan']) # gugu.html의 name과 같아야함
    result=''
    for i in range(1,10):
        result += '{}x{}={}<br>'.format(dan,i,dan*i)
    #html 태그 <br> 를 인식하게 하는 함수
    result=Markup(result)
    return render_template('gugu/gugu_result.html', result=result)

if __name__ == '__main__':
    # thread 스레드 - 작업단위
    # single thread 프로그램 1개에 작업단위 1개 - 순서가 중요한 경우
    # multi thread 프로그램 1개에 작업단위 여러개 - 속도가 중요한경우
    #threaded를 True로 설정하면 신경망 모형을 불러오는 코드에서 에러가 발생하므로 False로 설정
    app.run(port=8000, threaded=False)