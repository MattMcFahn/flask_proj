from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import config

sql_uri = r'postgresql://postgres:' + config.passwords['postgresql'] +'@localhost/personal_portfolio_submissions'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=sql_uri

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key = True)
    email_=db.Column(db.String(220), unique=True)
    name_=db.Column(db.String(220), unique=True)
    comments_=db.Column(db.String(10000), unique=False)
    submission_=db.Column(db.String(220), unique=False)
    
    def __init(self, email_,name_,comments_,submission_):
        self.email_=email_
        self.name_=name_
        self.comments_=comments_
        self.submission_=submission_


@app.route("/")
def home():
    return render_template("home.html", title="Homepage")

@app.route("/blog")
def blog():
    return render_template("blog.html", title="Blog")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/thank_you_contact", methods=['POST'])
def thank_you_contact():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        comments=request.form['contact-message']
        return render_template("thank_you_contact.html", title="Thank you for your submission!", )

@app.route("/thank_you_survey", methods=['POST'])
def thank_you_survey():
    if request.method=='POST':
        submission=request.form['top-language']
        return render_template("thank_you_survey.html", title="Thank you for your submission!", )


if __name__ == "__main__":
    app.run(debug=True)

