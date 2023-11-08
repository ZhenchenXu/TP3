#crée le 31 Août
#crée par Zhenchen Xu
#une programme

#variables
import time
import random
global healtH
health=20
global victories
victories=0
global defeats
defeats=0
global playing
playing=True
global battles
battles=0
global sauter
sauter=False
global winstreak
winstreak = 0
speedrun = 1


#fonctions

#les statistiques
def statistique():
    print('''Votre Statistique:
Santé: ''' + str(health))
    print('Combats: ' + str(battles))
    print('Victories: ' + str(victories))
    print('Defeats: ' + str(defeats))
    print('winstreak: ' + str(winstreak))

#le affichage pour le guide
def guide_affichage():
    print('''_________________________________________________________
 |                                                        |
|  Pour réussir un combat, il faut que la valeur du dé     |
 | lancé soit supérieure à la force de l’adversaire. Dans |
|  ce cas, le niveau de vie de l’usager est augmenté de la |
|  force de l’adversaire.                                 |
 |                                                         |
 | Une défaite a lieu lorsque la valeur du dé lancé par   |
 | l’usager est inférieure ou égale à la force de         |
|  l’adversaire. Dans ce cas, le niveau de vie de l’usager|
 | est diminué de la force de l’adversaire.                |
 |                                                        |
|  La partie se termine lorsque les points de vie de       |
|  l’usager tombent sous 0.                              |
 |                                                        |
|  L’usager peut combattre ou éviter chaque adversaire,    |
 | dans le cas de l’évitement, il y a une pénalité de     |
|  1 point de vie.                                         |
 |_________________________________________________________|''')


speedrun = int(input('Voulez-vous speedrun mode (1 pour oui 2 pour non):'))
if speedrun == 1:
    speedrun = 0
    print('speed run mode activated')
    time.sleep(1)
else:
    print('normal speed mode activated')
    time.sleep(1)



#mot de bienvenue et explication de règlement
print('Bonjour et bievenue à Door Ennemies. Vous êtes dans un couloir sans fin rempli de porte. Derrière chaque porte sera un menace à ta vie. Voici un manuel qui peut t\'aider.')
time.sleep(3)

#le guide en visuel
print('''_____________________
|                    |
|         G          |
|         U          |
|         I          |
|         D          |
|         E          |
| ___________________|
''')

#animation décorative
for i in range(3):
    print("PRESS Enter pour ouvrir le guide", end='')
    time.sleep(0.5)
    print('\r', end='')
    time.sleep(0.5)
input('PRESS Enter pour ouvrir le guide')

#le guide de en haut
guide_affichage()

#animation pour obliger l'utilisateur d'attendre un peu avant de commencer le jeu
for i in range(10):
    print("PRESS Enter commencer le jeu", end='')
    time.sleep(0.5)
    print('\r', end='')
    time.sleep(0.5)

input('PRESS Enter pour commencer le jeu')
avoid = None

#le main loop pour le jeu
while playing:
    run = False
    if not sauter:
        statistique()
        input('Press Enter pour continuer vers une porte')
        detection = int(winstreak)
        if detection%3 == 0 and detection != 0:
            print('Ton rumeur de succès a été entendu par un grand monstre')
            strength = random.randint(12, 20)
            time.sleep(speedrun)
            print('Le boss est de niveau ' + str(strength) + '!')
            time.sleep(speedrun)
        else:
            print("Tu as choisi une porte qui était ouverte, et a entré dedans la salle")
            strength = random.randint(2, 10)
            time.sleep(speedrun)
            print('Il y a un monstre! Le niveau du montre est ' + str(strength))
            time.sleep(speedrun)
        print('Voulez-vous quitter la salle ou combattre cette monstre? 1 pour quitter, 2 pour combattre,')
        print("3 pour relire les instructions du jeu.")
        Devoid = input(str('Rappel toi que quitter la salle va te coûter un point de santé... Ton choix?: '))
        time.sleep(speedrun)
    else:
        print('Voulez-vous quitter la salle ou combattre cette monstre? 1 pour quitter, 2 pour combattre,')
        print("3 pour relire les instructions du jeu.")
        Devoid = input(str('Rappel toi que quitter la salle va te coûter un point de santé... Ton choix?: '))
        time.sleep(speedrun)
        sauter = False
    if Devoid == '3':

        #le joueur veut regarder les règles
        guide_affichage()
        sauter = True
    elif Devoid == '2':

        #le joueur décide d'attaquer
        print('Tu avance vers le monstre et entre en combat avec celui ci!')
        time.sleep(speedrun)
        print('Tu prend une attaque!')
        attaque = random.randint(2, 12)
        time.sleep(speedrun)
        print('Ton attaque était de niveau de force ' + str(attaque))
        time.sleep(speedrun)
        if attaque <= strength:
            print('Malheureusement, ton attaque n\'a pas pu tuer le monstre.')
            battles = battles + 1
            defeats = defeats + 1
            time.sleep(speedrun)
            print('Tu es presque mort mais a réussi de échapper le monstre.')
            time.sleep(speedrun)
            health = health - strength
            print('Santé -' + str(strength))
            time.sleep(speedrun)
            winstreak = 0
        else:
            print('Le monstre a été effacé de l\'existence par ton attaque. ')
            battles = battles + 1
            victories = victories + 1
            winstreak = winstreak + 1
            time.sleep(speedrun)
            print('Le monstre a laissé tomber quelque chose ...')
            time.sleep(speedrun)
            print('Un niveau ' + str(strength) + ' sac médical,')
            time.sleep(speedrun)
            health = health + strength
            print('Santé +' + str(strength))
    else:

        #le joeur ne veut pas combattre
        health = health - 1
        print('Ayant peur du montre, tu as retourné au milieu du couloir...')
        time.sleep(speedrun)
        print('Santé -1')
        time.sleep(speedrun)
        run = True

    #si le joueur a aucun santé
    if health <= 0 and defeats > 0 and run == False:
        print('Tu es rempli de blessures de bataille. Malheureusement, tu saignes trop et tu es mort ')
        time.sleep(speedrun)
        print('Voici ce que vous avez accompli: ')
        time.sleep(speedrun)
        health = 0
        statistique()
        playing = False
    elif health <= 0 and defeats == 0 and run == True:
        print('Pourquoi tu court de tes problème?')
        time.sleep(speedrun)
        print('Regard, maintenant tu es mort à cause de manque d\'énergie à s\'échapper des monstres... ')
        time.sleep(speedrun)
        print('Au revoir! voici les stats ')
        health = 0
        time.sleep(speedrun)
        statistique()
        playing = False
    else:
        if health <= 0:
            print('Tu es épuisé et a voulu dormir...tu va plus jamais réveiller')
            time.sleep(1)
            print('Voici ce que vous avez accompli: ')
            time.sleep(1)
            health = 0
            statistique()
            playing = False
        else:
            print('Tu continue ton adventure dans ce couloir mystérieux...')
            time.sleep(speedrun)



