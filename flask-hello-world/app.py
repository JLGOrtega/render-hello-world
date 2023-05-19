from flask import Flask
app = Flask(__name__)
import psycopg2
from sqlalchemy import create_engine, text
import pandas as pd

@app.route('/')
def hello_world():
    return 'Hello, World! CHANGED'


@app.route('/db')
def db():
    engine = create_engine("postgresql://postgres:fckGDnStyhzL0Y1BsW0J@containers-us-west-122.railway.app:7954/railway")
    data = pd.read_sql_query(text("SELECT * FROM tabla"), con = engine)

    return data.values.tolist()