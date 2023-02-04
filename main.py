"""
Affiche une commande de nourriture pendant 10s puis un formulaire
et enfin la page de résultat
"""
from flask import Flask, render_template, request, jsonify, redirect
from functionsfoods import *

app = Flask(__name__)

@app.route('/')
def home():

    global commande
    commande = generate_commande()

    return render_template("home.html",sandwich = commande[0],
                           sauce = commande[1],vegetables = commande[2],
                           bread = commande[3])

@app.route('/survey', methods=["GET","POST"])
def survey():  

    if request.method == "POST":

        # Réalisation des test
        # Récupére les données depuis le form
        sandwich = request.form["sandwich"]
        sauce = request.form["sauce"]
        vegetables = request.form["vegetables"]
        bread = request.form["bread"]
        
        # Créer une liste command select pour la comparer a la commande
        command_select = []
        # Créer la variables pts
        score = 0

        # Converties les réponses en minuscules
        sandwich = str.lower(sandwich)
        command_select.append(sandwich)
        sauce = str.lower(sauce)
        command_select.append(sauce)
        vegetables = str.lower(vegetables)
        command_select.append(vegetables)
        bread = str.lower(bread)
        command_select.append(bread)


        """print(f"On ta demande de prendre un {commande[0]}, sauce {commande[1]}, {commande[2]} en {commande[3]}")
        print(f"Toi tu as commander un {command_select[0]}, sauce {command_select[1]}, {command_select[2]} en {command_select[3]}")"""
        
        for i in range (0,4):
            
            print(f"Tu devais prendre {commande[i]}, tu as pris {command_select[i]}")
            if command_select[i] == commande[i]:
                print("Ok")
                score += 1
            else:
                print("Sale merde inutile tu peux pas retenir une commande")

        return render_template ("result.html", list_commande = commande, list_commande_select = command_select, score = score)

    return render_template("questionnaire.html")

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

# Redirection pour la pwa
@app.route('/static/home.html')
def redirect_pwa():
    return redirect("https://sunshyne.up.railway.app/", code=302)

if __name__ == "__main__":
    app.run(debug=True)