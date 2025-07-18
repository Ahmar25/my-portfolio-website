import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html") # or return "Hello, World!" for test

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Railway's port
    app.run(host="0.0.0.0", port=port)