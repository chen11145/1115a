from flask import Flask, render_template,request
from datetime import datetime
from waitress import serve


@app.route("/")
def index():
    homepage = "<h1>資管二A 411146570 陳彥霖</h1>"
    homepage += "<a href=/mis>我的個人簡介</a><br>"
    homepage += "<a href=/today>MIS相關工作介紹</a><br>"
    homepage += "<a href=/welcome>職涯測驗結果</a><br>"
    homepage += "<a href=/about>求職履歷自傳</a><br>"
    return homepage


@app.route("/ask")
def today(): 
    return render_template("ask.html")



if __name__ == "__main__":
    #app.run()
    serve(app, host='0.0.0.0', port=8080)