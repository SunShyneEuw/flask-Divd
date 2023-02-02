from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

# Créer l'app
app = Flask(__name__)

# Config le path de la db
app.config['SQLALCHEMY_DATABASE_URI'] = 'quiz.db'

# Initialise la db
db = SQLAlchemy(app)

# Import des routes ulrs du du fichier urls
import routes

# Lance l'app
if __name__ == "__main__":
    app.run(debug=True) # host="0.0.0.0",