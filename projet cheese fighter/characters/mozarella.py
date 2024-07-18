#coding: utf-8

from .character import Character

class Mozarella(Character):
    """Classe qui représente le personnage Mozarella"""
    def __init__(self, name = False):
        super().__init__(300, 40, 70, 20, name)
