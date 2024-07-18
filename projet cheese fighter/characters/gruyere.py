#coding: utf-8

from .character import Character

class Gruyere(Character):
    """Classe qui représente le personnage Gruyere"""
    def __init__(self, name = False):
        super().__init__(300, 15, 15, 5, name)
