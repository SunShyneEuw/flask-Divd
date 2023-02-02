from __main__ import app
from flask import Flask, render_template, request, redirect

# Création des routes/urls
# Url de base : Acceuil
@app.route('/', methods=["GET","POST"])
def index():

    if request.method == "POST":

        # Définie les pts du joueur
        pts_player = 0
        # Récupere les données du formulaires et
        # Calcule les pts du joueur
        player_name = request.form["name"]
        print(request.form["name"])

        rep_question_1 = request.form["question-1"]
        print(f"Pour la question 1 : Tu as choisi la reponse {rep_question_1}")
        if rep_question_1 == "1991":

            pts_player += 1

        rep_question_2 = request.form["question-2"]
        print(f"Pour la question 2 : Tu as choisi la reponse {rep_question_2}")
        if rep_question_2 == "Windows 9":

            pts_player += 1

        rep_question_3 = request.form["question-3"]
        print(f"Pour la question 3 : Tu as choisi la reponse {rep_question_3}")
        if rep_question_3 == "Une intelligence artificiel":

            pts_player += 1

        rep_question_4 = request.form["question-4"]
        print(f"Pour la question 4 : Tu as choisi la reponse {rep_question_4}")
        if rep_question_4 == "Charles Hull":

            pts_player += 1

        rep_question_5 = request.form["question-5"]
        print(f"Pour la question 5 : Tu as choisi la reponse {rep_question_5}")
        if rep_question_5 == "Utilise le même réseaux":

            pts_player += 1
        
        # Converti int -> str pour éviter une error dans render_tempaltes
        pts_player = str(pts_player)

        return render_template("result-page.html", name = player_name,score = pts_player)

    return render_template("index.html")

# Horloge
@app.route('/horloge')
def clock():

    from datetime import datetime
    now_time = datetime.now()
    now_time = now_time.strftime("%H:%M:%S")
    
    
    return render_template("/clock/home.html", now_time = now_time)

# Accueil de l'app calcul mentaux tables
@app.route('/calcul-mentaux-tables/accueil', methods=["GET","POST"])
def calcul_mentaux_tables_accueil():

    if request.method == "POST":

        # Définie les pts du joueur
        pts_player = 0
        # Récupere les données du formulaires et
        # Calcule les pts du joueur
        player_name = request.form["name"]
        print(request.form["name"])

        

        return render_template("calcul-mentaux-tables/result-page.html", name = player_name)

    return render_template("calcul-mentaux-tables/home.html")

# Redirection pour la pwa
@app.route('/static/index.html')
def redirect_pwa():
    return redirect("https://sunshyne.up.railway.app/", code=302)