# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest value wins; for example,
# a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have
# a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then
# the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
#
# Hand	 	Player 1	 	Player 2	 	Winner 1	 	5H 5C 6S 7S KD Pair of Fives 2C 3S 8S 8D TD Pair of Eights
# Player 2 2	 	5D 8C 9S JS AC Highest card Ace 2C 5C 7D 8S QH Highest card Queen Player 1 3	 	2D 9C AS AH AC
# Three Aces 3D 6D 7D TD QD Flush with Diamonds Player 2 4	 	4D 6S 9H QH QC Pair of Queens Highest card Nine 3D 6D
# 7H QD QS Pair of Queens Highest card Seven Player 1 5	 	2H 2D 4C 4D 4S Full House With Three Fours 3C 3D 3S 9S 9D
# Full House with Three Threes Player 1 The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the
# last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?
import functools
from dataclasses import dataclass
from enum import IntEnum, auto, StrEnum
from pathlib import Path
from typing import Optional, List, Tuple

INPUT_PATH = Path(__file__).resolve().parent.parent / 'inputs' / 'problem054-poker'
TEST_INPUT_PATH = Path(__file__).resolve().parent.parent / 'inputs' / 'problem054-poker-test'


class CardValue(IntEnum):
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()

    @classmethod
    def from_str(cls, str_repr: str):
        if str_repr == '2':
            return CardValue.TWO
        if str_repr == '3':
            return CardValue.THREE
        if str_repr == '4':
            return CardValue.FOUR
        if str_repr == '5':
            return CardValue.FIVE
        if str_repr == '6':
            return CardValue.SIX
        if str_repr == '7':
            return CardValue.SEVEN
        if str_repr == '8':
            return CardValue.EIGHT
        if str_repr == '9':
            return CardValue.NINE
        if str_repr == 'T':
            return CardValue.TEN
        if str_repr == 'J':
            return CardValue.JACK
        if str_repr == 'Q':
            return CardValue.QUEEN
        if str_repr == 'K':
            return CardValue.KING
        if str_repr == 'A':
            return CardValue.ACE


class Suite(StrEnum):
    H = auto()
    C = auto()
    S = auto()
    D = auto()


@functools.total_ordering
@dataclass
class Card:
    value: CardValue
    suite: Suite
    string_repr: str

    def __lt__(self, other: 'Card') -> bool:
        return self.value < other.value

    @classmethod
    def from_str(cls, str_repr: str) -> 'Card':
        return cls(CardValue.from_str(str_repr[0]), Suite(str_repr[1].lower()), str_repr)

    def __repr__(self):
        return self.string_repr


class GameType(IntEnum):
    HighCard = auto()
    OnePair = auto()
    TwoPairs = auto()
    ThreeOfAKind = auto()
    Straight = auto()
    Flush = auto()
    FullHouse = auto()
    FourOfAKind = auto()
    StraightFlush = auto()
    RoyalFlush = auto()


@functools.total_ordering
@dataclass
class Game:
    game_type: GameType
    best_card_value: Optional[CardValue] = None
    second_best_card_value: Optional[CardValue] = None

    def __lt__(self, other: 'Game'):
        if self.game_type == other.game_type:
            if self.best_card_value == other.best_card_value:
                if self.second_best_card_value is not None and other.second_best_card_value is not None:
                    return self.second_best_card_value < other.second_best_card_value
            return self.best_card_value < other.best_card_value
        return self.game_type < other.game_type

    def __repr__(self) -> str:
        base = f"{self.game_type.name}"
        best_card = f": {self.best_card_value.name}" if self.best_card_value else ""
        second_best_card = f", {self.second_best_card_value.name}" if self.second_best_card_value else ""
        return base + best_card + second_best_card


def is_straight(sorted_hand: List[Card]) -> bool:
    return all(sorted_hand[i].value - sorted_hand[i - 1].value == 1 for i in range(1, 5))


def find_three(sorted_hand: List[Card]) -> Optional[int]:
    """Returns the start index of the three or none"""
    if sorted_hand[0].value == sorted_hand[2].value:
        return 0
    elif sorted_hand[1].value == sorted_hand[3].value:
        return 1
    elif sorted_hand[2].value == sorted_hand[4].value:
        return 2
    else:
        return None


def find_pairs(sorted_hand: List[Card]) -> List[CardValue]:
    """Returns the card values of the pair(s) in ascending order"""
    pairs = []
    for i in range(1, 5):
        if sorted_hand[i].value == sorted_hand[i - 1].value:
            pairs.append(sorted_hand[i].value)
    return pairs


def find_game(sorted_hand: List[Card]) -> Game:
    if len(set(card.suite for card in sorted_hand)) == 1:  # all same suite
        if is_straight(sorted_hand):
            if sorted_hand[0].value == CardValue.TEN:
                return Game(GameType.RoyalFlush)
            else:
                return Game(GameType.StraightFlush, best_card_value=sorted_hand[-1].value)
        else:
            return Game(GameType.Flush, best_card_value=sorted_hand[-1].value)
    elif sorted_hand[0].value == sorted_hand[3].value or sorted_hand[1].value == sorted_hand[4].value:
        return Game(GameType.FourOfAKind, best_card_value=sorted_hand[2].value)
    three_position = find_three(sorted_hand)
    if three_position == 0:
        if sorted_hand[3].value == sorted_hand[4].value:
            return Game(GameType.FullHouse, best_card_value=sorted_hand[0].value,
                        second_best_card_value=sorted_hand[4].value)
        else:
            return Game(GameType.ThreeOfAKind, best_card_value=sorted_hand[0].value)
    elif three_position == 2:
        if sorted_hand[0].value == sorted_hand[1].value:
            return Game(GameType.FullHouse, best_card_value=sorted_hand[2].value,
                        second_best_card_value=sorted_hand[0].value)
        else:
            return Game(GameType.ThreeOfAKind, best_card_value=sorted_hand[2].value)
    elif three_position == 1:
        return Game(GameType.ThreeOfAKind, best_card_value=sorted_hand[1].value)
    if is_straight(sorted_hand):
        return Game(GameType.Straight, best_card_value=sorted_hand[4].value)
    pairs_values = find_pairs(sorted_hand)
    if len(pairs_values) == 2:
        return Game(GameType.TwoPairs, best_card_value=pairs_values[1], second_best_card_value=pairs_values[0])
    if len(pairs_values) == 1:
        return Game(GameType.OnePair, best_card_value=pairs_values[0])
    return Game(GameType.HighCard, best_card_value=sorted_hand[4].value)


def read_hands(file_path: Path) -> List[Tuple[List[Card], List[Card]]]:
    with open(file_path, 'r') as fin:
        matches = []
        for line in fin.readlines():
            cards = []
            for s in line.strip().split(' '):
                card = Card.from_str(s)
                cards.append(card)
            hand1 = cards[0:5]
            hand2 = cards[5:]
            matches.append((hand1, hand2))
    return matches


def solve(input_file: Path = INPUT_PATH) -> int:
    matches = read_hands(input_file)
    wins = 0
    for hand1, hand2 in matches:
        sorted_hand1 = sorted(hand1)
        sorted_hand2 = sorted(hand2)
        print(f"{sorted_hand1} vs {sorted_hand2}")
        game1 = find_game(sorted_hand1)
        game2 = find_game(sorted_hand2)
        if game1 > game2:
            wins += 1
            print(f"1: {game1}, {game2}")
        elif game1 == game2:
            for i, card1 in enumerate(sorted_hand1):
                if card1.value > sorted_hand2[i].value:
                    wins += 1
                    print(f"1: {game1}, {game2}")
                    break
                elif card1.value < sorted_hand2[i].value:
                    print(f"2: {game1}, {game2}")
                    break
        else:
            print(f"2: {game1}, {game2}")
    return wins


if __name__ == '__main__':
    # print(solve(TEST_INPUT_PATH))
    print(solve())
