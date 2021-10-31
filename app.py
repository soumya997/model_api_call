from flask import Flask,request
from flask import jsonify
import requests
# from flask_ngrok import run_with_ngrok
app = Flask(__name__)
# run_with_ngrok(app)
url = "http://16cd-34-72-55-62.ngrok.io"
@app.route("/api",methods=['GET'])
def home():
  qs = request.args.get('qs')
  qs_url = qs.replace(' ', '%20')
  ans = requests.get(url+ "/api?qs=" + qs_url)
  return ans

if __name__ == "__main__":
  app.run()
