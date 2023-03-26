# Flask is the class
from flask import Flask, render_template
import json
from db import JOBS
app = Flask(__name__) # __name__ shows how a particular app is invocked

#path after domain name ex- jovian.com/profile , domain - jovian.com/ and url after it use in route

@app.route("/")
def hello_world():
  #passing dynamic contect in html
  
  return render_template('home.html', jobs=JOBS, comp_name="DK")


@app.route("/api/jobs")
def list_jobs():
  #return the json content of jobs
  return json.dumps(JOBS, indent = 4)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)