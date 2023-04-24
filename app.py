# Flask is the class
from flask import Flask, render_template, jsonify, request
from db import Load_Jobs_From_DB, Load_Job_From_DB

app = Flask(__name__)  # __name__ shows how a particular app is invocked

#path after domain name ex- jovian.com/profile , domain - jovian.com/ and url after it use in route


@app.route("/")
def hello_world():
  #passing dynamic contect in html
  JOBS = Load_Jobs_From_DB()
  return { "hello":"bye"}


# to convert DB rows as dict use this v imp
@app.route("/api")
def list_jobs():
  JOBS = Load_Jobs_From_DB()
  return jsonify(JOBS)


# Dynamic route
@app.route("/job/<id>")
def list_specific_job(id):
  JOB = Load_Job_From_DB(id)
  return { "hello":"bye"
    }


@app.route("/job/<id>/apply", methods=['post'])
def apply_for_job(id):
  # data = request.args # only get data from url
  data = request.form  #get data from post method submission
  new_data = jsonify(data)

  return render_template('application_submitted.html', application=new_data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
