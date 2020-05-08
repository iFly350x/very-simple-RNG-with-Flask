import random
from flask import Flask, request, render_template, url_for

app = Flask(__name__)
app.debug = True

def generateNum(minimum,maximum,amount):
	numbers = [random.randint(minimum, maximum) for _ in range(amount)]
	Sum = sum(numbers)
	return numbers, Sum
	
@app.route('/', methods=["POST", "GET"])
def home():	
	if request.method == 'POST':
		minimum = request.form['minimum']
		maximum = request.form['maximum']
		amount = request.form["amount"]
		data = generateNum(int(minimum),int(maximum),int(amount))
		generateNum(int(minimum), int(maximum), int(amount))
		return render_template("responce.html", listNum=data[0], sum=data[1])
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run()