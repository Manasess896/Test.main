from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def status():
    try:
        # Your bot's main logic here
        # For example, if the bot performs a task, you can log success
        logging.info("Main bot is running successfully!")
        return jsonify({"status": "success", "message": "Main bot is running successfully!"})
    except Exception as e:
        logging.error(f"Main bot encountered an error: {e}")
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
