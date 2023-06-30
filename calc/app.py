from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def do_add():
    """Return the sum of a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def do_sub():
    """Return the difference between a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def do_mult():
    """Return the product of a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return str(result)

@app.route('/div')
def do_div():
    """Return the quotient of a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return str(result)