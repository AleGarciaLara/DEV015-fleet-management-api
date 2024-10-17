from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy 
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = SQLAlchemy(app)

class Taxi(db.Model):
    __tablename__ = 'taxis'
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String, nullable=False)
    
@app.route('/taxis', methods=['GET'])
def get_taxis():
    taxis = Taxi.query.all()
    taxis_list = [{'id': taxi.id, 'plate': taxi.plate} for taxi in taxis]
    return jsonify(taxis_list)
@app.route('/')
def hello_world():
    
    data = {
        "message": "Holi world!",
    }
    return jsonify(data)


