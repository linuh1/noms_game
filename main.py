class Card:
    pass


class Player:
    pass


class Noms(Card):
    pass


class Defend(Card):
    pass


class Event(Card):
    pass


class Danger(Card):
    pass


class Trap(Card):
    pass


class Help(Card):
    pass


class HelpOrDanger(Card):
    pass


class Rescue(Card):
    pass


class Universal(Card):
    pass


class CardsOnHands(Player):
    pass


class CardsOnPlayerZone(Player):
    pass


class Action(Player):
    def take_card(self):
        pass

    def play_cards(self):
        pass

    def discard_card(self):
        pass

    def finish_turn(self):
        pass


class


class GamingZone:
    pass


class DiscardPile(GamingZone):
    pass


class Deck(GamingZone):
    pass


class Players(GamingZone):
    pass


class GameEnding(Players):
    pass


def start_game():
