# coding: utf-8
import random

class Character():
    """Classe mère avec les caractéristiques de base des différents combattants fromagers
    attribut de classe: actions
    attributs: nom, vie, attaque, défense, agilité
    methodes: attaques, fuite
    """
    actions = {
        'a': 'attaquer',
        'f': 'fuir'
    }

    def __init__(self, life, attack, defense, agility, name = False):
        self.name = name
        self.life = life
        self.attack = attack
        self.defense = defense
        self.agility = agility

    def attacks(self, target):
        """Fonction qui permet au personnage d'attaquer un autre personnage.
        Si la cible ne peut pas éviter l'attaque, elle perd de la vie.
        """
        print("{} attaque violemment {}".format(self.name, target.name))

        # Offre une chance à la cible d'éviter l'attaque
        # Exemple: un fromage avec 50 d'agilité a 1/2 chance d'éviter l'attaque

        if random.randrange(0,100) <= target.agility:
            print("{} a esquivé l'attaque".format(target.name))
            return False
        
        # Soustraire à la vie de la cible l'attaque du personnage moins la défense de la cible divisée par 5

        target.life -= self.attack - (target.defense/5)

        # Faire en sorte que les fromages ne peuvent pas avoir de vie dans le négatif

        if target.life < 0:
            target.life = 0
        print("{} a maintenant {} de vie".format(target.name, target.life))

    def escape(self):
        """Fonction permettant au personnage d'essayer de s'échapper et de quitter le combat"""

        # Diminuer les chances de s'échapper en fonction de l'agilité du personnage

        agi = round(self.agility/5)
        if random.randrange(0,100) <= agi:
            return True
        return False

    def make_action(self, action, ennemy):
        """Fonction permettant d'exécuter la méthode correspondante sur la base d'une chaîne d'action"""
        if action not in self.actions:
            print('Cette action est impossible')
            return False
        if action == 'a':
            self.attacks(ennemy)
        elif action == 'f':
            if self.escape():

                # Si la fuite est réussie, nous créons une exception car le combat est sur le point de prendre fin.

                print("Vous réussissez à fuir au dernier moment dans un élan d'agilité fromagère folle")
                raise Exception('L ennemi s échappe')
            else:
                print('Votre ennemi fromager vous rattrape !')
        elif action == 's':
            self.heal()
        return True

    def __str__(self):
        return "{} : vie = {}".format(self.name, self.life)
