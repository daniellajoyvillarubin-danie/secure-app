from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200


    @app.route('/add', methods=['POST'])
    def add_numbers():
        data = request.get_json()

            if not data:
                    return jsonify({"error": "Missing JSON payload"}), 400

                        if 'a' not in data or 'b' not in data:
                                return jsonify({"error": "Both 'a' and 'b' are required"}), 400

                                    try:
                                            a = float(data['a'])
                                                    b = float(data['b'])
                                                        except ValueError:
                                                                return jsonify({"error": "Inputs must be numeric"}), 400

                                                                    result = a + b

                                                                        return jsonify({"result": result}), 200


                                                                        if __name__ == '__main__':
                                                                            app.run(host='0.0.0.0', port=5000)