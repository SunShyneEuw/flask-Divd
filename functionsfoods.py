"""
Ensembles de fonctions pour générer des commandes a partir des listes
"""
from listefood import *
import random

def generate_commande():

    commande_list = []

    sandwich_choice = random.choice(sandwich_list)
    commande_list.append(sandwich_choice)
   

    sauce_choice = random.choice(sauce_list)
    commande_list.append(sauce_choice)

    vegetables_choice = random.choice(vegetables_list)
    commande_list.append(vegetables_choice)

    bread_choice = random.choice(bread_type_list)
    commande_list.append(bread_choice)

    return commande_list