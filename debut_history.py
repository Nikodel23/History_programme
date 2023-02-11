from data import (all_ages,correct_ages,text_for_clients,intro_texte_history_one,intro_texte_history_two,intro_texte_history_three)

def verification_erronee():
    print ("Le nombre que vous avez tapé est incorrect.")
    return ask_for_age ()

def ask_for_age ():
        n = input("Quelle age avez vous ?")
        if n == correct_ages:
            if age not in all_ages:
                verification_erronee()
        else:
           n = correct_ages
           return n
pass
age = ask_for_age ()

def nom_de_utilisateur_base():
    nom_de_utilisateur= input("Quelle est le nom de votre hero?")
    return nom_de_utilisateur
    nom_de_utilisateur = nom_de_utilisateur_base()



    
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
        
        
def first_history():
    
    pass
    
    
def second_history():
    
    pass
    
def third_history():
    
    pass