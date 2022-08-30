from flask import Flask

server = Flask(__name__)


@server.route("/")
def home():
    return "Python running..."

@server.route("/api/v1/liveness")
def liveness():
    return "Liveness"

@server.route("/api/v1/readiness")
def readiness():
    return "Readiness"


if __name__ == "__main__":
    print("server started......")
    server.run(host='0.0.0.0')