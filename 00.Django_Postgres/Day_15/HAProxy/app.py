import os
from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def home():
    name = os.environ.get("name", "")
    return f"Hello Backend Developers! from {name}"
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Run the app on port 5000
