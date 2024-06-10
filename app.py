from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors module
import subprocess
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the Flask app

data_dir = "data"  # Default data directory

@app.route('/set-data-dir', methods=['POST'])
def set_data_dir():
    global data_dir
    data_dir = request.json.get('data_dir', data_dir)
    return jsonify({"message": f"Data directory set to {data_dir}"}), 200

@app.route('/update-database', methods=['POST'])
def update_database():
    try:
        reset = request.json.get('reset', False)
        args = ["python3", "populate_database.py"]
        if reset:
            args.append("--reset")
        env = os.environ.copy()
        env['DATA_DIR'] = data_dir
        subprocess.run(args, check=True, env=env)
        return jsonify({"message": "Database updated successfully"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/query', methods=['POST'])
def query():
    try:
        query_text = request.json['query']
        conversation = (request.json.get('conversation', []))
        convo_string = "\n".join([f"{msg['sender']}: {msg['text']}" for msg in conversation])
        env = os.environ.copy()
        env['DATA_DIR'] = data_dir
        args = ["python3", "query_data.py", query_text]
        if conversation != "":
            args.extend(["--conversation", convo_string])

        result = subprocess.run(
            args,
            check=True,
            capture_output=True,
            text=True,
            env=env
        )
        response_text = result.stdout.strip()
        return jsonify({"response": response_text, "conversation": conversation + [{"sender": "bot", "text": response_text}]}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
