# coding: utf-8

from .storyAgent import storyAgent

class Arena(storyAgent):
    """Classe qui représente un champ de bataille au cours de l'histoire et gére les combats
    attributs : player, ennemy
    methods: fighters_enter, fighters_leave, battle
    """

    def __init__(self):

        # Les deux attributs nécessitent les characters objects

        self.player = False
        self.ennemy = False

    def fighters_enter(self, player, ennemy):
        """Fonction permettant de stocker les objets des personnages dans les attributs du joueur et de l'ennemi"""
        self.player = player
        self.ennemy = ennemy

    def fighters_leave(self):
        """Fonction permettant d'effacer les attributs du joueur et de l'ennemi"""
        self.player = False
        self.ennemy = False

    def battle(self):
        """Fonction permettant de demander au joueur une action et de l'exécuter tant que le joueur ou l'ennemi sont en vie"""
        self.transition(2)

        # Tant que les deux personnages sont en vie

        while self.player.life > 0 and self.ennemy.life > 0:
            try:
                action_is_allowed = False

                # Vérifier si le personnage peut faire l'action et l'exécuter

                while not action_is_allowed:
                    print("{} || {}".format(self.player, self.ennemy))
                    action = input('Que souhaites-tu faire {} ? : '.format(self.player.actions)).lower()
                    action_is_allowed = self.player.make_action(action, self.ennemy)

            # Si le personnage a réussi à s'échapper

            except Exception as e:
                break

            # Au tour de l'adversaire, s'il n'est pas mort

            if self.ennemy.life > 0:
                self.ennemy.attacks(self.player)
            self.transition(5)

        # Fin du combat

        print('Le combat est terminé. A bientôt vaillant fromage !')
        self.fighters_leave()
