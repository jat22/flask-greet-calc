# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)

@app.route('/add')
def addition():
	a = int(request.args.get('a'))
	b = int(request.args.get('b'))
	result = add(a, b)

	return f'<h3>{a} + {b} = {str(result)}</h3>'

@app.route('/subtract')
def subtraction():
	a = int(request.args.get('a'))
	b = int(request.args.get('b'))
	result = sub(a,b)

	return f'<h3>{a} - {b} = {str(result)}</h3>'

@app.route('/mult')
def multiply():
	a = int(request.args.get('a'))
	b = int(request.args.get('b'))
	result = mult(a,b)

	return f'<h3>{a} x {b} = {str(result)}</h3>'

@app.route('/div')
def divide():
	a = int(request.args.get('a'))
	b = int(request.args.get('b'))
	result = div(a,b)

	return f'<h3>{a} / {b} = {str(result)}</h3>'


operators = {
	'add' : add,
	'sub' : sub,
	'mult' : mult,
	'div' : div
}

@app.route('/math/<operator>')
def math(operator):
	a = int(request.args.get('a'))
	b = int(request.args.get('b'))
	result = operators[operator](a,b)

	return str(result)
