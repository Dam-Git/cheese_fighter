#coding: utf-8

import os
import time

class storyAgent():
    """ Classe mère de tous les objets qui font vivre l'histoire comme le narrateur ou l'arène
    attributs : aucun
    methodes : transition
    """
    def __init__(self):
        pass

    def transition(self, waiting_time):
        """Fonction pour faire une pause et rafraichir l'écran"""
        time.sleep(waiting_time)
        os.system('cls||clear')
