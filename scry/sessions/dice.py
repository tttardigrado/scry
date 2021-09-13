from sessions.scrysession import ScrySession
from typing import List
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from functions.general import clear_screen
from functions.dice import coin, planar, dice_range, choose, roll


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

clear, c: clear the screen
    """

    def make_session(self) -> PromptSession:
        """
        Setup prompt toolkit session for dice

        Returns:
            PromptSession: session for dice
        """

        # completer for the dice session
        completer: WordCompleter = WordCompleter(
            [
                "roll",
                "coin",
                "planar",
                "choose",
                "range",
                "clear",
                "c",
                "help",
                "h",
            ]
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
            print(coin(), "\n")

        elif first_word == "planar":
            # roll planar die
            # blank, planeswalk, chaos
            print(planar(), "\n")

        elif first_word == "choose":
            # choose one of the values provided by the user
            print(choose(" ".join(command_list[1:])), "\n")

        elif first_word == "range":
            # choose a number from a specified range
            print(dice_range(" ".join(command_list[1:])), "\n")

        elif first_word == "roll":
            # roll a die
            print(roll(" ".join(command_list[1:])), "\n")

        elif first_word in {"clear", "c"}:
            # clear the screen
            clear_screen()

        elif first_word in {"help", "h"}:
            # get help
            print(self.help_msg)

        else:
            self.not_valid()
