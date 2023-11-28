import client
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/get_class", methods=["GET"])
def get_class():
    create = classes
    return render_template("information.html", output=create)


if __name__ == "__main__":
    classes = client.create_class()
    app.run(debug=True)
