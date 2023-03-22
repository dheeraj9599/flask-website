# Flask is the class
from flask import Flask

app = Flask(__name__) # __name__ shows how a particular app is invocked

#path after domain name ex- jovian.com/profile , domain - jovian.com/ and url after it use in route

@app.route("/")
def hello_world():
  return "hello"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)