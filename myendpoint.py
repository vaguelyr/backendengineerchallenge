from flask import Flask, request, redirect
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
	with open('index.html' , 'r') as f:
		return f.read()

@app.route("/api/supervisors")
def supervisors():
	r = requests.get('https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers')
	data = json.loads(r.text)
	jd = json.loads(r.text)
	jd_sorted = sorted(jd, key=lambda k: ((k['jurisdiction']),(k["lastName"]),(k["firstName"])))
	#print(jd_sorted)
	ret = ""
	for item in jd_sorted:
		j = item['jurisdiction']
		if (j.isnumeric()):
			continue
		l = item['lastName']
		f = item['firstName']
		
		#ret +=('"{' + j + "} - {" + l + "}, {" + f + '}"\n <br>' )
		ret +=('' + j + " - " + l + ", " + f + '\n <br>' )
	return ret



@app.route('/api/submit',methods = ['POST'])
def submit():
	print(request.form)
	firstName = request.form['firstName']	
	lastName = request.form['lastName']	
	email = request.form.get('email')
	phone = request.form.get('phone')
	superv = request.form.get('superv')
	if (email == None):
		email = "n/a"
	if (phone == None):
		phone = "n/a"
	if (superv == None):
		superv = "n/a"
	print("got\nfirstName: " + firstName + "\nlastName: " + lastName + "\nemail: " + email + "\nphone: " + phone + "\nsuperv: " + superv) 
	return redirect('/')

