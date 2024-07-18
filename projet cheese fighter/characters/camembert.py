#coding: utf-8

from .character import Character

class Camembert(Character):
    """Classe qui représente le personnage Camembert.
    methods = heal, str"""
    actions: Character.actions.update({'s': 'se soigner'})

    def __init__(self, name = False):
        super().__init__(300, 20, 50, 25, name)
