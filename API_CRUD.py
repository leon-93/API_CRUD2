from flask import Flask
from flask import jsonify
from requests import get,put,delete
from flask_restful import Api, Resource,abort
import pymysql
import json
import requests


app = Flask(__name__)
api = Api(app)

conn  = pymysql.connect(host='localhost',
                             user='root',
                             password='coucou02',
                             database='sakila',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

class Crud(Resource):

    
    
    def get(self):

        cursor.execute('select customer_id,store_id,first_name,last_name,email,active FROM customer')
        film = cursor.fetchall()

        print(film)
        if film is None:
            abort(404)
        return film


    def delete(self):
        cursor.execute('ALTER TABLE film DROP COLUMN store_id,create_date,last_update')
        film = cursor.fetchall()
        if film is None:
            abort(404)
        return film

    def put(self):
         cursor.execute('ALTER TABLE film ADD article')
         film = cursor.fetchall()
         
        
         return film


api.add_resource(Crud, '/')


if __name__ == '__main__':
    app.run(debug=True)
