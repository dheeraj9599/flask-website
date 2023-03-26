#  connecting mysql db to replit using sqlachemy
from sqlalchemy import create_engine, text

import os

# FOLLOW FROM THIS DOCUMENT
# https://docs.sqlalchemy.org/en/20/dialects/mysql.html

# we have to create a engine to import mysql database

# we hide our db username, pass string in Db_Connections as we do not want to show this on github
db_connection_string = os.environ['DB_Connections']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
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
    
    for i in result:
       JOBS.append(i)
      
    return JOBS

JOBS = Load_Jobs_From_DB()


