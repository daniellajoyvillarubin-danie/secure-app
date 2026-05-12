from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200


@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()

    try:
        a = int(data.get('a'))
        b = int(data.get('b'))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

    return jsonify({"result": a + b}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
