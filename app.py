# from flask import Flask,request
# from flask import jsonify
# import requests
# # from flask_ngrok import run_with_ngrok
# app = Flask(__name__)
# # run_with_ngrok(app)
# url = "http://652f-104-199-206-225.ngrok.io"
# @app.route("/api",methods=['GET'])
# def home():
#   qs = request.args.get('qs')
#   qs_url = qs.replace(' ', '%20')
#   ans = requests.get(url+ "/api?qs=" + qs_url)
  
#   return ans.json()



# if __name__ == "__main__":
#   app.run()
from flask import Flask,request
from flask import jsonify
import requests
# from flask_ngrok import run_with_ngrok
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)
# run_with_ngrok(app)
url = "http://652f-104-199-206-225.ngrok.io"
@app.route("/api",methods=['GET'])
@cross_origin(supports_credentials=True)
def home():
  qs = request.args.get('qs')
  qs_url = qs.replace(' ', '%20')
  ans = requests.get(url+ "/api?qs=" + qs_url)
  # print(type(ans))
  # print(ans.text["result"])
  # print(type(ans.text))
  # var = ans.txt
  # print(var.split(''))
  # return jsonify({'result' : ans.text})
  # print(ans.json())
  return ans.json()
   

if __name__ == "__main__":
  # app.config['DEBUG'] = True
  app.run()
