from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A 411146570 陳彥霖</h1>"
    homepage += "<a href=/ask>我的個人簡介</a><br>"
    homepage += "<a href=/today>MIS相關工作介紹</a><br>"
    homepage += "<a href=/welcome>職涯測驗結果</a><br>"
    homepage += "<a href=/about>求職履歷自傳</a><br>"
    return homepage


@app.route("/ask")
def ask(): 
    return render_template("ask.html")


@app.route("/today")
def today(): 
    return render_template("today.html") 


@app.route("/welcome")
def welcome(): 
    return render_template("welcome.html") 


@app.route("/about")
def about(): 
    return render_template("about.html")

    <img src='/static/images/logo.png'>

#if __name__ == "__main__":
 #   app.run()
