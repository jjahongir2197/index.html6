from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def age():

    if request.method == "POST":

        age = int(request.form["age"])

        if age < 13:
            return "Bola"
        elif age < 18:
            return "O‘smir"
        elif age < 60:
            return "Kattalar"
        else:
            return "Keksa"

    return render_template("index.html")

app.run(debug=True)
