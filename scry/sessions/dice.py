from typing import List
from prompt_toolkit import PromptSession
from prompt_toolkit.completion.nested import NestedCompleter
from scry.functions.general import clear_screen, pprint_dice
from scry.functions.dice import (
    coin,
    planar,
    dice_range,
    choose,
    roll,
    hand,
    roll_adv,
    roll_dis,
)
from scry.sessions.scrysession import ScrySession


class Dice(ScrySession):
    """
    Dice session for the SolRing app

    Deals with Roling dice, flipping coins, choosing values...
    """

    def __init__(self) -> None:
        ScrySession.__init__(self)
        self.help_msg: str = """Help
roll: roll a die
    -> roll xdy+z -> roll x y-sided die and add z
    -> d6 -> roll 1 6 sided dice
    -> 5d8 -> roll 5 8 sided die
    -> 3d4+2 -> roll 3 4 sided die and add 2
    -> 6d20-2 -> roll 6 20 sided die and subtract 2

coin: flip a coin
    -> heads or tails

planar: roll a planar die
    -> 4 blanks, 1 chaos, 1 planeswalk

choose: choose a value from a provided list
    -> choose xxx | yyy | zzz -> return one of xxx, yyy, zzz.
    -> | separates the values
    -> choose me | you | they | your self | my self
    -> choose 1 | 10 | 55 | 100
    -> choose 20 | try | 55 | test | roll

range: return a number between a provided range
    -> range <first> <second> -> return <first> < number < <second>
    -> range 1 10 -> one of: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    -> range 5 1 -> one of: 1, 2, 3, 4, 5
    -> range 1 -2 -> one of: -2, -1, 0, 1
    -> range -1, -3 -> one of: -3, -2, -1

hand: choose a random card from target player's hand
    -> hand <number_of_cards> -> returns a number within [1, number_of_cards]
    -> hand 7 -> one of: 1, 2, 3, 4, 5, 6, 7
    -> hand -1 -> not valid

clear, c: clear the screen
    """

    def make_session(self) -> PromptSession:
        """
        Setup prompt toolkit session for dice

        Returns:
            PromptSession: session for dice
        """

        # completer for the dice session
        completer: NestedCompleter = NestedCompleter.from_nested_dict(
            {
                "roll": {"adv", "advantage", "dis", "disadvantage"},
                "adv": None,
                "advantage": None,
                "dis": None,
                "disadvantage": None,
                "hand": None,
                "coin": None,
                "planar": None,
                "choose": None,
                "range": None,
                "clear": None,
                "c": None,
                "help": None,
                "h": None,
            }
        )

        return PromptSession(completer=completer)

    def process_input(self, command: str) -> None:
        """
        Process the input provided to the prompt

        The commands are: roll | coin | planar | choose | range | clear | help

        Args:
            command (str): command provided by the user that will be processed
        """
        # properly format the input
        command_list: List[str] = command.split()
        first_word: str = command_list[0]

        if first_word == "coin":
            # flip a coin
            # heads or tails
            pprint_dice(coin())

        elif first_word == "planar":
            # roll planar die
            # blank, planeswalk, chaos
            pprint_dice(planar())

        elif first_word == "hand":
            # choose one card from hand
            pprint_dice(hand(int(command_list[1])))

        elif first_word == "choose":
            # choose one of the values provided by the user
            pprint_dice(choose(" ".join(command_list[1:])))

        elif first_word == "range":
            # choose a number from a specified range
            pprint_dice(dice_range(" ".join(command_list[1:])))

        elif first_word == "roll":
            mode: str = command_list[1]

            if mode in {"adv", "advantage"}:
                # roll with advantage
                # advantage means that 2 dice are rolled
                # and the largest one is considered
                pprint_dice(roll_adv("".join(command_list[2:])))

            elif mode in {"dis", "disadvantage"}:
                # roll with disadvantage
                # disadvantage means that 2 dice are rolled
                # and the smallest one is considere
                pprint_dice(roll_dis("".join(command_list[2:])))

            else:
                # roll a die
                pprint_dice(roll("".join(command_list[1:])))

        elif first_word in {"adv", "advantage"}:
            # roll with advantage
            # advantage means that 2 dice are rolled
            # and the largest one is considered
            pprint_dice(roll_adv("".join(command_list[1:])))

        elif first_word in {"dis", "disadvantage"}:
            # roll with advantage
            # advantage means that 2 dice are rolled
            # and the largest one is considered
            pprint_dice(roll_adv("".join(command_list[1:])))

        elif first_word in {"clear", "c"}:
            # clear the screen
            clear_screen()

        elif first_word in {"help", "h"}:
            # get help
            print(self.help_msg)

        else:
            self.not_valid()
