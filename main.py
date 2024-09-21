from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Path to store user data
userdata_file = 'userdata.json'

# Load or create the userdata file
if not os.path.exists(userdata_file):
    with open(userdata_file, 'w') as f:
        json.dump([], f)

# Helper function to load user data
def load_user_data():
    with open(userdata_file, 'r') as f:
        return json.load(f)

# Helper function to save user data
def save_user_data(data):
    with open(userdata_file, 'w') as f:
        json.dump(data, f, indent=4)

# API to receive and save user data
@app.route('/api/save-user', methods=['POST'])
def save_user():
    data = request.get_json()

    playername = data.get('playername')
    join_time = data.get('join_time')
    robloxuserid = data.get('robloxuserid')

    if not playername or not join_time or not robloxuserid:
        return jsonify({'error': 'Missing data fields!'}), 400

    new_user = {
        'playername': playername,
        'join_time': join_time,
        'robloxuserid': robloxuserid
    }

    user_data = load_user_data()
    user_data.append(new_user)
    save_user_data(user_data)

    return jsonify({'message': 'User data saved!', 'data': new_user}), 200

# API to get all users
@app.route('/api/get-users', methods=['GET'])
def get_users():
    user_data = load_user_data()
    return jsonify(user_data), 200

# Render the HTML page with user data
@app.route('/')
def index():
    user_data = load_user_data()
    return render_template('index.html', users=user_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
