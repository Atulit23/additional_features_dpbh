from flask import Flask, jsonify, request
from gradio_client import Client
from flask_cors import CORS  
import json

app = Flask(__name__)
CORS(app) 

client = Client("https://atulit23-realvfake.hf.space/")
phishing_client = Client("https://atulit23-phishingurls.hf.space/")

@app.route('/ai-image', methods=['GET'])
def aiImageDet():
    try:
        url = request.args.get('url')
        if not url:
            return jsonify(error='URL parameter is missing'), 400

        result = client.predict(
            url,
            api_name="/predict"
        )
        print(result)
        return jsonify(json.loads(result))

    except Exception as e:
        return jsonify(error=str(e)), 500
    
@app.route('/phishing', methods=['GET'])
def detectPhishing():
    try:
        url = request.args.get('url')
        if not url:
            return jsonify(error='URL parameter is missing'), 400

        result = phishing_client.predict(
            url,
            api_name="/predict"
        )
        print(result)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
