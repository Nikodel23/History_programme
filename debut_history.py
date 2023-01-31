from data import*

def nom_de_utilisateur_base():
    nom_de_utilisateur= input("Quelle est le nom de votre hero?")
    return nom_de_utilisateur
    
def ask_for_age ():
    n = input("Quelle age avez vous ?  ")
    return n
 
age = ask_for_age ()
    
def user_too_young (n):
    return n in young_ages

def age_de_utilisateur_base():
    while user_too_young (age):
        age = ask_for_age ()
        pass