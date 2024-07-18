#coding: utf-8

from .character import Character

class Gorgonzola(Character):
    """Classe qui représente le personnage Gorgonzola"""
    def __init__(self, name = False):
        super().__init__(300, 50, 80, 10, name)
