import sys, os

## Reis api is commented
'''
from ReisApi import ReisApi
from ReisApi import ReisCompRent
from ReisApi import ReisCompSale
'''
import json
import psycopg2
import psycopg2.extras
from flask import Flask, render_template, Response, redirect,url_for,jsonify
import time
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from flask import request
import requests

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
	return 'This is Addres validation Service home'
	#return render_template('index.html')

@app.route('/address',methods = ['POST', 'GET'])
def address():
	if request.method == 'POST':
		req_data = dict(request.form)#request.args.get('address')
		req_address=req_data["address"]
		address={'sent_address':req_data["address"], 'recieved_address':req_data["address"],'Service_Called':'address validation service'}
		return jsonify(address)#str(req_data)#
	elif request.method == 'GET':
		return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True, threaded=True)