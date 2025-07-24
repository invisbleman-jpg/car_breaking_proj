from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num1 = request.form["inp"]
        num2 = (int(num1)/10)*3
        num1 = (int(num1)/10)**2
        num3 = num1+num2
        return render_template("index.html", curtain=f"Bremsweg -> {num1}km/h", curtain2=f"Reaktionsweg -> {num2}km/h", curtain3=f"Anhalteweg -> {num3}km/h")

    return render_template("index.html")