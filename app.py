from flask import Flask, request
import socket
import json

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
   print(f"Received webhook data", flush=True)
   webhook_data = request.get_json()


   if webhook_data:
       # Extract only repository name and pusher name
       repository_name = webhook_data.get('repository', {}).get('name', 'Unknown repository')
       pusher_name = webhook_data.get('pusher', {}).get('name', 'Unknown pusher')


       # Store only the repository name and pusher name
       filtered_data = {
           'repository_name': repository_name,
           'pusher_name': pusher_name
       }


       # Save the filtered data to a JSON file
       with open('/opt/simpleFlask/webhook_data.json', 'w') as f:
           json.dump(filtered_data, f, indent=4)


       return 'Webhook received and filtered data saved', 200


   return 'Webhook received but no data', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# test 1
# test 2
# test 3
# test 4
# test json1
# test json2
