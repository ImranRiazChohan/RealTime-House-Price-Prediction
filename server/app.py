from flask import Flask
from flask import jsonify,request
import utlis

app=Flask(__name__)

@app.route("/")
def Home():
    return "Hello world"

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': utlis.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    totalsqft = float(request.form['totalsqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify({
        'estimated_price': utlis.get_estimated_price(location,totalsqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__=="__main__":
    utlis.load_save_utils()
    app.run(debug=True)
