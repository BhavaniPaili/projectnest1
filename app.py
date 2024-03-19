from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['Movie']
collection = db['newsletter']

@app.route("/")
def project123():
    return render_template("project123.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/newsletter")
def newsletter():
    return render_template("newsletter.html")

@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        data = request.json

        if 'email' not in data:
            return jsonify({'message': 'Missing required fields'}), 400

        email = data['email']

        # Insert email into the MongoDB collection
        collection.insert_one({'email': email})

        return jsonify({'message': 'Data stored successfully'}), 200
    except Exception as e:
        print('Error:', e)
        return jsonify({'message': 'Data failed to store in the backend.'}), 500

if __name__ == '__main__':
    app.run(debug=True)