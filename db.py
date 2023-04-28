#  connecting mysql db to replit using sqlachemy
from sqlalchemy import create_engine, text

import os, random

# FOLLOW FROM THIS DOCUMENT
# https://docs.sqlalchemy.org/en/20/dialects/mysql.html

# we have to create a engine to import mysql database

# we hide our db username, pass string in Db_Connections as we do not want to show this on github
db_connection_string = os.environ['DB_Connections']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{ # ssl is used for more secure connection
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

# getting info out from the DB(engine)
# getting a connection


# making a connection name as conn
# when we come out of the with the connection ends

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     print(result.all()[1])
# any query we make in text is going to return a list of rows or table


# result is of type sqlalchemy.engine.cursor
# result.all() is of list

# convering row into a dictionary and appending in res_dict

def Load_Jobs_From_DB():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    JOBS = []
  
    # print(type(result))
    # to convert DB rows as dict use ._asdict() v imp
    for row in result.all():
       JOBS.append(row._asdict())
      
    return JOBS


def Load_Job_From_DB(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:# since id is the primary key so this will return one row only
      return rows[0]._asdict()

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, Full_name, Email,  Education, Work_Experience, Resume_url) VALUES (:job_id, :Full_name, :Email, :Education, :Work_Experience, :Resume_url)")
    values = {
      'job_id' : job_id,
      'Full_name' : data['Full_name'],
      'Email' : data['Email'],
      'Education' : data['Education'],
      'Work_Experience' : data['Work_Experience'],
      'Resume_url' : data['Resume_url']
    }
    
    conn.execute(query, values)

def add_user_to_db(temp):
  with engine.connect() as conn:
    query = text("INSERT INTO users (user_id, job_id, password) VALUES (:user_id,:job_id, :password)")
    
    values = {
      'user_id' : temp['user_id'],
      'job_id' : random.randint(0,9),
      'password' : temp['password']
    }
    
    conn.execute(query, values)


def update_user_job_id(temp):
  with engine.connect() as conn:
    query = text("UPDATE users SET (job_id = temp['job_id']) WHERE (user_id = temp['user_id']);")
    
    conn.execute(query)
