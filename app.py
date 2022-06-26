import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import urllib.request
import json

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database_path = 'postgresql://postgres:ghostman@localhost:5432/items'
app.config["SQLALCHEMY_DATABASE_URI"] = database_path
db = SQLAlchemy(app)
from models import *
cors =CORS(app)

@app.after_request
def after_request(reponse):
    reponse.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    reponse.headers.add('Access-Control-Allow-Headers', 'GET, POST, PUT, PATCH, DELETE')
    return reponse

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/items")
def items():
    url = "https://dev.shepherd.appoly.io/fruit.json"
    response = urllib.request.urlopen(url)
    data = response.read()
    json_dict = json.loads(data)
    # print(json_dict)
    items = json_dict['menu_items']
    # print(items)

    layer_one=[]
    layer_two=[]
    layer_three=[]
    layer_four=[]

    def get_layer_label():
        for item in items:
            item_one = item['label']
            layer_one.append(item_one)
            create_items = Items(label_one=item_one)
            db.session.add(create_items)
            children_item = item['children']
            for child in children_item:
                item_two = child['label']
                create_items = Items(label_two=item_two)
                db.session.add(create_items)
                layer_two.append(item_two)
                child2 = child['children']
                for childed in child2:
                    item_three = childed['label']
                    create_items = Items(label_three=item_three)
                    db.session.add(create_items)
                    layer_three.append(item_three)
                    child_bearer = childed['children']
                    for child_bear in child_bearer:
                        item_four = child_bear['label']
                        create_items = Items(label_four=item_four)
                        db.session.add(create_items)
                        layer_four.append(item_four)
        db.session.commit()


    get_layer_label()
    # print(layer_one)
    # print(layer_two)
    # print(layer_three)
    # print(layer_four)

    return "success"

@app.route('/labels', methods=['GET'])
def get_label_items():
    ven = Items.query.all()
    new_data = []
    for new_ven in ven:
        label_one = new_ven.label_one
        label_two = new_ven.label_two
        label_three = new_ven.label_three
        label_four = new_ven.label_four

        items_new = {
        "label_one" : label_one,
        "label_two" : label_two,
        "label_three" : label_three,
        "label_four" : label_four,
        }
        new_data.append(items_new)

    print(new_data)
    return jsonify({
        "data":new_data
    })



        
    

