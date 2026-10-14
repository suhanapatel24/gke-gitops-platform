from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(service="gke-gitops-platform", message="Cloud-native service delivered with GitOps", status="running")

@app.get("/healthz")
def health():
    return jsonify(status="healthy"), 200

@app.get("/readyz")
def ready():
    return jsonify(status="ready"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
