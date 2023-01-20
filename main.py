from flask import Flask, render_template, request

# Créer l'app
app = Flask(__name__)

# Création des routes/urls
# Url de base : Acceuil
@app.route('/', methods=["GET","POST"])
def index():

    if request.method == "POST":
        print(request.form["name"])

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) # host="0.0.0.0", 