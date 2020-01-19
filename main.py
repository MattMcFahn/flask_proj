from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
import config
from send_email import email_comments
from smtplib import SMTPRecipientsRefused

from survey_summaries import survey_summary_barchart
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io



sql_uri = r'postgres://ojsogizyxpmsht:2b62fd599fbac77125c5991edccf4d10f811fce0e72f9765597bfb8fac10d5df@ec2-174-129-255-15.compute-1.amazonaws.com:5432/d4ou5ir17dk44p?sslmode=require'
#old_uri = r'postgresql://postgres:' + config.passwords['postgresql'] +'@localhost/personal_portfolio_submissions'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=sql_uri

db = SQLAlchemy(app)

class CommentsData(db.Model):
    __tablename__="contact_data"
    id=db.Column(db.Integer, primary_key = True)
    email_=db.Column(db.String(220), unique=False)
    name_=db.Column(db.String(220), unique=False)
    comments_=db.Column(db.String(10000), unique=False)

    def __init__(self, email_,name_,comments_):
        self.email_=email_
        self.name_=name_
        self.comments_=comments_

class SurveyData(db.Model):
    __tablename__="survey_data"
    id=db.Column(db.Integer, primary_key = True)
    submission_=db.Column(db.String(220), unique=False)

    def __init__(self, submission_):
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

        data=CommentsData(name, email, comments)
        db.session.add(data)
        db.session.commit()

        email_comments(email, comments)
        return render_template("thank_you_contact.html", title="Thank you for your submission!")


@app.route("/survey_results", methods=['GET', 'POST'])
def thank_you_survey():
    if request.method=='POST':
        submission=request.form['top-language']

        data=SurveyData(submission)
        db.session.add(data)
        db.session.commit()
        # Code to select avg height
        return render_template("survey_results.html", title="Thank you for your submission!")
    if request.method=='GET':
        # Code to select avg height
        return render_template("survey_results.html", title="Survey Results")

@app.route("/plot/temp")
def plot_temp():
    fig = survey_summary_barchart()
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


if __name__ == "__main__":
    app.run(debug=True)
