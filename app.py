from flask import Flask
import threading
from lsdk import lsdk as run_main_logic

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

def run_flask_app():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    # Start the main logic in a separate thread
    main_thread = threading.Thread(target=run_main_logic)
    main_thread.start()

    # Run the Flask app
    run_flask_app()
