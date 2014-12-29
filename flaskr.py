# -*- coding: utf-8 -*-
"""
    Hack news database display
"""
from GetSaveNews import SaveToDb

from flask import *

#orm setting
from sqlalchemy import Table, MetaData, create_engine, func
from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///hacknews.db")

session = sessionmaker()
session.configure(bind=engine)

#db entity
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Record(Base):
    __tablename__ = 'HNews'
    id = Column(Integer, primary_key=True)
    hid = Column(Integer)
    title = Column(String)
    url = Column(String)

#flask
app = Flask(__name__)
s = session()


@app.route('/list', methods=['GET'])
def list():
    entries = s.query(Record).all()
    counts = s.query(func.count(Record.id)).all()[0][0]
    return render_template('list.html', entries=entries, counts=counts)


@app.route('/parse', methods=['GET'])
def parse():
    #take ages
    SaveToDb()
    return "Parsing..."


if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0',port=4000)

