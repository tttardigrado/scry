import random
from typing import List
import re

# expression to match dice rolling.
# ex: 2d6-4 -> roll 2 d6 and subtract 4 to their sum
dice_expr: re.Pattern = re.compile(r"^(\d+)?d(\d+)\+?(\-?\d+)?$")

# expression to match ranges
# ex: 3 -20 -> choose a number between -3 and 20
range_expr: re.Pattern = re.compile(r"^(\-?\d+)\s+(\-?\d+)$")

# sides of a coin
coin_values: List[str] = ["Heads", "Tails"]

# faces of a planar die
planar_values: List[str] = [
    "Blank",
    "Blank",
    "Blank",
    "Blank",
    "Planeswalk",
    "Chaos",
]


def coin() -> str:
    """
    Flip a coin

    Returns:
        str: Flipped side. (Heads or Tails)
    """
    return random.choice(coin_values)


def planar() -> str:
    """
    Roll a planar die

    Returns:
        str: Rolled face. (Blank, Planeswalk or Chaos)
    """
    return random.choice(planar_values)


def dice_range(value: str) -> int:
    """
    Random number from a specified range

    Args:
        value (str): string to be processed and
        get the start and end values of the range

    Raises:
        ValueError: if the str is not valid

    Returns:
        int: random number
    """
    # process string sing regex
    matches = range_expr.match(value)

    if not matches:
        raise ValueError("Range expression is not valid")

    # get the numbers
    first, second = matches.groups()
    first = int(first)
    second = int(second)

    # first must be less than second
    if first > second:
        # swap them
        first, second = second, first

    # choose number
    return random.choice(range(first, second + 1))


def hand(number_of_cards: int) -> int:
    """
    Random card from a hand o <number_of_cards> cards.
    Before calling this function the player should define a number
    for each card in their hand, the card corresponding
    to the returned number should be subjected to the effect that made
    the player call this function

    Example:
        Target player discards a card at random.
        cards in hand == 6
        order the cards from 1 to 6 on the table
        -> hand 6
        -> -> return an integer between 1 and 6 (lets say it returned 4)
        the player discards card 4

    Args:
        number_of_cards (int): number of cards that target
            player has in their hand.

    Returns:
        int: random integer contained within [1, number_of_cards]
    """
    return random.randint(1, number_of_cards)


def choose(value: str) -> str:
    """
    Choose a random value from a provided formated string

    Args:
        value (str): formated string with values separated by |

    Returns:
        str: random value
    """
    # split values
    values_to_choose: List[str] = value.split("|")
    # choose value
    return random.choice(values_to_choose).strip()


def roll_dice(times: int, sides: int, modifier: int) -> int:
    """
    Roll a dice expression

    Args:
        times (int): times/number of dice
        sides (int): number of sides
        modifier (int): value to be added at the end

    Returns:
        int: dice expression result
    """
    result: int = 0

    for i in range(times):
        # roll the die
        value: int = random.randint(1, sides)
        # update result
        result += value
        # print
        # ex: 2: 5
        print(f"{i+1}: {value}")

    # add the modifier
    result += modifier
    # print the modifier
    print(f"modifier: {modifier}")

    return result


def roll(value: str) -> int:
    """
    process a dice expression and roll it

    Args:
        value (str): dice expression

    Raises:
        ValueError: when the dice expression is not valid

    Returns:
        int: result of the dice expression
    """
    # use regex to match the dice expression
    matches = dice_expr.match(value)

    # non valid expression
    if not matches:
        raise ValueError("Dice expression is not valid")

    # get the values and convert then to integers
    times_to_roll, sides, value_modifier = matches.groups()
    times_to_roll = int(times_to_roll or 1)  # 1 is default
    sides = int(sides)
    value_modifier = int(value_modifier or 0)  # 0 is defalt

    return roll_dice(times_to_roll, sides, value_modifier)
