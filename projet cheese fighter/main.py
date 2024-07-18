# coding: utf-8

from game.narrator import Narrator
from game.factory import Factory
from game.arena import Arena

if __name__ == '__main__':

    # Lance un narrateur qui commence à raconter l'histoire

    narrator = Narrator()

    # Lance une arène où des combats vont avoir lieu

    arena = Arena()

    introduction = [
        "Bienvenue, combattant, aux portes d'un monde savoureux et légendaire.",
        "Ici commence ton histoire, laisse-toi guider par le narrateur de cet univers.",
        "Prépare toi à un affrotement épique où les meilleurs fromages s'affrontent pour la suprématie culinaire",
        "Ta légende résonnera pour des siècles et des siècles, ton voyage commence maintenant",
        "Que le meilleur fromage gagne !"
    ]
    narrator.tell(introduction)

    # Permettre à l'utilisateur de choisir son type de personnage et de le récupérer depuis la factory

    choice = narrator.choose_character()
    player = Factory.get_character(choice)
    narrator.player_customization(player)

    # Récupérer un ennemi depuis la factory, pour ce scénario : un camembert

    ennemy = Factory.get_character('camembert')
    ennemy.name = 'Gérard'

    # Exemple d'histoire à raconter par le narrateur

    story = [
        'Tu marches dans les vastes plaines des Terroirs Fromagers',
        'Le soleil est chaud sur ton visage et l herbe fraîche sous tes pieds',
        'Tu entends alors un bruissement sourd, tu te retournes',
        'Tu tombes nez à nez avec un camembert agressif qui te défie en duel',
    ]
    narrator.tell(story)

    # Lance un combat 

    arena.fighters_enter(player, ennemy)
    arena.battle()

    