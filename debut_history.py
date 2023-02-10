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
    
def trois_histoires():
    print(text_for_clients)
    action = int(input("Quel est votre action ?"))
    if action == 0:
            print(intro_texte_history_one)
            first_history
    if action == 1:
            print(intro_texte_history_two)
            second_history
    if action == 2:
            print(intro_texte_history_three)
            third_history
    if action == 3:
        exit