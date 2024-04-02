from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    render_template('index.html', content="Hello World!")

@app.route('/get_my_ip', methods=['GET'])
def get_my_ip():
    # Get the client's IP address from the request
    ip_addr = request.remote_addr
    return jsonify({'ip': ip_addr}), 200

if __name__ == '__main__':
    app.run()