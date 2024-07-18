# coding: utf-8

from .storyAgent import storyAgent

class Narrator(storyAgent):
    """ Classe qui raconte l'histoire et intéragit avec le joueur.
    class attributs: rôles autorisés et leur traduction
    attributs: aucun
    methodes: tell, choose_character, player_customization
    """

    roles = {
        "cheddar" : "cheddar",
        "mozarella" : "mozarella",
        "gorgonzola" : "gorgonzola",
        "camembert" : "camembert",
        "parmesan" : "parmesan",
        "gruyere" : "gruyere"
    }

    def __init__(self):
        pass

    def tell(self, story):
        """Fonction permettant d'afficher avec une transition chaque phrase d'une liste donnée"""
        if not isinstance(story, list):
            raise ValueError("La méthode tell de la classe narrateur attend une liste comme argument")
        for sentence in story:
            self.transition(3)
            print(sentence)

    def choose_character(self):
        """Fonction permettant au joueur de choisir un type de personnage parmi les rôles.
        Tant que le joueur ne choisit pas un rôle existant, la fonction tourne en boucle.
        """
        self.transition(7)
        print("""Avant de commencer ton aventure fromagère, qui veux-tu incarner ?
- Un cheddar robuste et tranchant, manie son épée de saveur avec une intensité audacieuse
- Une mozarella agile et souple, enveloppe ses adversaires dans ses lianes de douceur
- Un gorgonzola féroce et bleu, attaque avec des éclairs de saveur piquante, laissant ses ennemis étourdis
- Un camembert tel un chevalier de la table ronde, protège le royaume des saveurs crémeuses et terreuses
- Un parmesan dur comme l acier, tranche à travers les rangs ennemis avec sa lame de goût salé
- Un gruyere solide et fiable, défend vaillamment les frontières du palais avec sa saveur douce et noisetée.""")
        while True:
            try:
                player_choice = input('Je veux incarner un : ').lower()

                # Vérifier si player_choice est bien dans la classe des rôles attribut

                player_class = Narrator.roles[player_choice]
                break
            except:
                print('Ce personnage fromager n est pas reconnu')
        return player_class

    def player_customization(self, player):
        """Fonction permettant au joueur de choisir un nom de personnage"""
        self.transition(2)
        name = input("Quel est votre nom de combattant fromager ? : ")
        player.name = name
