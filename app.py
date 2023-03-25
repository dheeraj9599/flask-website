# Flask is the class
from flask import Flask, render_template, jsonify

app = Flask(__name__) # __name__ shows how a particular app is invocked


JOBS=[
  {
    'id': 1,
    'title': 'Web developer',
    'location': 'bengaluru',
    'salary': 'Rs 1lakh'
  },
  {
    'id': 2,
    'title': 'Software engineer',
    'location': 'bengaluru',
    'salary': 'Rs 1.5lakh'
  },
  {
    'id': 3,
    'title': 'Data analyst',
    'location': 'noida',
    'salary': 'Rs 1.3lakh'
  }
]

#path after domain name ex- jovian.com/profile , domain - jovian.com/ and url after it use in route

@app.route("/")
def hello_world():
  #passing dynamic contect in html
  return render_template('home.html', jobs=JOBS, comp_name="DK")


@app.route("/api/jobs")
def list_jobs():
  #return the json content of jobs
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)