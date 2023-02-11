from flask import Flask,request,jsonify
from utill import Utills
from flask_cors import CORS #imp
prt = 9000
app = Flask(__name__)
CORS(app)

# @app.route('/get_location_names',methods=['GET'])
# def get_location_names():
#     #location lsistt is pass
#     response=jsonify({
#         "location":utill.get_location_names()
#     })
#     response.headers.add("Access-control-Allow-Origin","*")
    
#     return response


@app.route('/getsummary',methods=['POST'])
def predict_home_price():
    _json=request.get_json() #json come from client
    print(_json)
    _data=_json['data']
    ans=Utills.lsa_method(_data)
    response=jsonify({
        'result': ans
    })
    response.headers.add("Access-control-Allow-Origin","*")
    
    return response
    



if __name__ == "__main__":
    app.run(port=prt, debug=True,host='0.0.0.0')


''''
{
  "total_sqft":"1000",
  "location":"st Phase Jp Nagar",
  "bhk":"2",
  "bath":"3"
}
'''