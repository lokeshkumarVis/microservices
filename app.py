import sys, os, urllib.parse
import uuid
## Reis api is commented from use
'''
from ReisApi import ReisApi
from ReisApi import ReisCompRent
from ReisApi import ReisCompSale
import psycopg2
import psycopg2.extras
'''
import json

from flask import Flask, render_template, Response, redirect,url_for,jsonify, request
import time
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import requests

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
	#return 'This is Addres validation Service home'
	return render_template('index.html')

@app.route('/property',methods = ['POST', 'GET'])
def address():
	if request.method == 'POST':
		if request.form:
			req_data = dict(request.form)#request.args.get('address')
			req_address=req_data["address"]
			req_address=req_address[0]
			address=parse_address(req_address)
		elif (request.get_json())!=None:
			req_address = request.get_json()
			address=req_address
		address={'Request':req_address, 'parsed_address':address,'property guid':uuid.uuid4(),'Service_Called':'address validation service'}
		return jsonify(address)#str(req_data)#
	elif request.method == 'GET':
		address=request.args.get("address")
		if address!= None:	
			print(address)
		return render_template('index.html')
def parse_address(address):
	print(address)
	address=address.split(" ")
	address={"StreetAddress": ' '.join(address[:-2]),"CityName": address[-2],"StateCode": address[-1]}
	return address

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True, threaded=True)