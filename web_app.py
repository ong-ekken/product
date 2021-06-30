from songogram import send_songogram
from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('', 'index.html')


@app.route('/API/1.0.0/songogram', methods=['GET'])
def songogram():
    for item in request.args.values():
        if item == "":
            return jsonify({'status': 422,'error': 'Unprocessable Entity', 'message': 'Missing Input'})
    result = analyze(request.args.get('sentence'))
    if result['status'] == 201:
        return send_from_directory('', 'analysis.html')
    return result


if __name__ == "__main__":
    app.run()
