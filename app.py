from flask import Flask 
import socket 

app = Flask(__name__)

@app.route("/")
def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return f"The IP address is: {ip} and deployed from jenkins Pipeline"

@app.route("/nayana")
def say_hello():
    return "Hello Ankuj Sir, I have deployed from Jenkins Pipeline and pushed the image to my Docker Hub as well"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
