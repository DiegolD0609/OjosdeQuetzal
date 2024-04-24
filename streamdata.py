from flask import Flask, Response
from flask_cors import CORS

from opperai import Client
from opperai.types import ChatPayload, Message

import time
import json

# Initialize the opperai client with the API key
client = Client(api_key="op-*****")

# Create a new Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for the entire app to accept requests from the specified origin
CORS(app)

def generate_events():
    """Generator function to yield events from the opperai API."""
    # Calls the opperai API to start a chat session that streams responses
    response = client.functions.chat(
        "function/path",  # API endpoint or model to use
        ChatPayload(
            messages=[Message(role="user", content="Tell me a very short story.")],  # Initial message to start the chat
        ),
        stream=True  # Enables streaming responses
    )

    # Loops through each piece of data received from the streaming API
    for data in response: 
        print(data)  # Prints the raw response data for debugging
        data = json.dumps({'data': data.delta})  # Converts the data into JSON format, assuming `data.delta` is the relevant information
        yield f"data: {data}\n\n"  # Yields the data in a format suitable for SSE (Server-Sent Events)

# Defines a route in the Flask app that clients can connect to for receiving streamed events
@app.route('/events')
def stream():
    def event_stream():
        while True:
            # generate some data
            data = "data: {}\n\n".format(json.dumps({"key": "value"}))
            yield data
            time.sleep(1)  # delay between each message

    return Response(event_stream(), mimetype="text/event-stream")

# Checks if this script is executed as the main program and runs the Flask app
if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5001)  # Runs the app with debugging enabled, in threaded mode, on port 5001

