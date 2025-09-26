from flask import Flask, request, jsonify
from Functions.main import ngMain
app = Flask(__name__)

@app.post("/productionplan")
def productionPlan():
    try: 
        payload = request.get_json(silent=False)
        response = ngMain(payload)
        return jsonify(response), 200

    except Exception:
        return "Error receiving the payload", 400
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=False)

        

