import json

from flask import Flask, request, jsonify
from ctypes import cdll, c_int
lib = cdll.LoadLibrary('./libcompute.so')

app = Flask(__name__)

@app.route('/api/add', methods=['POST'])
def add():            
    try:
        x = int(request.form['x'])
        y = int(request.form['y'])
        num = lib.add(c_int(x), c_int(y))
                
        return jsonify({'answer': num})
    except KeyError as err:
        return jsonify({'err': 'invalid POST, json missing params'})    
    except Exception as err:
        return jsonify({'err': err})


if __name__ == '__main__':
    app.run(port=3030)
