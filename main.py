class Cards:
# карт всего 70
    pass


class Card(Cards):
# карта может быть на руках, в игровой зоне игрока N, в колоде, в сбросе

    pass


class Player:
# игрок может быть в игре, проигравшим или победителем
# количество игркоков от 2 до 6
# начинает игру с 1 картой Нома в игровой зоне исключая старейшину
# начинает игру с 3 картами на руках исключая карты события
# имеет игровую зону
# имеет пространство для карт на руках
# может выполнять действия с картами во время своего хода
# может смотреть на игровую зону любого другого игрока
# не может выполнять действия с картами вне своего хода
# может наблюдать за сыгранными картами
# может передать ход другому игроку
# может взять карту
# может брать карту только перед разыгрыванием карт, сбросом карт или объявлении о конце хода
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
