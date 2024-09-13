from flask import Flask, request
import socket

app = Flask(__name__)

# Global variable to count the number of requests
request_count = 0

@app.route('/')
def index():
    global request_count
    request_count += 1
    host_ip = socket.gethostbyname(socket.gethostname())
    return f"Host IP: {host_ip}<br>Number of requests: {request_count}"

@app.route('/webhook', methods=['POST'])
def webhook():
    print(f"Received webhook data")
    return 'Webhook received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# test 1
# test 2
