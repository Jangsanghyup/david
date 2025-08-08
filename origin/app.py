from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def home():
    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '
    return render_template('index.html', computername=hostname)

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/test1')
def test1():
    return render_template('test1.html')

@app.route("/test2")
def test2():
    return render_template('test2.html')

if __name__ == '__main__':
    app.run(debug=True)




    # if __debug__:
#     print("Debug mode is ON")
# else:
#     print("Debug mode is OFF")

# __debug__ 플래그란?
# Python에는 기본적으로 __debug__라는 내장 상수가 있으며, 이는 다음과 같이 작동합니다:

# 기본적으로 __debug__ == True입니다.

# Python을 최적화 모드(-O) 로 실행하면 __debug__ == False가 됩니다.

# python -O app.py