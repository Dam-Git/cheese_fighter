# coding: utf-8

class Factory():
    """Classe agissant comme une fabrique de patterns qui produit des personnages basés sur le nom de la classe de la chaîne"""

    @classmethod
    def get_character(self, class_name):
        """Methode qui retourne un objet d'un personnage spécifique basé sur un nom de classe"""
        if class_name == "cheddar":
            from characters.cheddar import Cheddar
            return Cheddar()
        elif class_name == "mozarella":
            from characters.mozarella import Mozarella
            return Mozarella()
        elif class_name == "gorgonzola":
            from characters.gorgonzola import Gorgonzola
            return Gorgonzola()
        elif class_name == "camembert":
            from characters.camembert import Camembert
            return Camembert()
        elif class_name == "parmesan":
            from characters.parmesan import Parmesan
            return Parmesan()
        elif class_name == "gruyere":
            from characters.gruyere import Gruyere
            return Gruyere()
