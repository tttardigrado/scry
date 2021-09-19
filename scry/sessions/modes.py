from scry.api_processing.archenemy.arch_deck import archenemy_decks
from scry.api_processing.archenemy.decks import ArchenemyDeck
from typing import List
from random import choice
from prompt_toolkit import PromptSession, print_formatted_text
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.formatted_text.html import HTML
from scry.api_processing.planechase import planar_deck
from scry.api_processing.random import show_momir
from scry.api_processing.booster import Booster
from scry.functions.dice import planar
from scry.functions.general import clear_screen
from scry.functions.constants import chaos_effects
from scry.sessions.scrysession import ScrySession


class Mode(ScrySession):
    """
    Game modes session for the SolRing app

    Deals with alternative game modes like momir, planechase, archenemy...
    """

    def __init__(self) -> None:
        ScrySession.__init__(self)

        # create planechase
        self.planechase = planar_deck
        # chaos effects for the CHAOS MAGIC format
        self.chaos_deck: List[str] = chaos_effects
        # scheme deck for the archenemy format
        self.scheme_deck: ArchenemyDeck = archenemy_decks["apocalypse"]
        # draft booster for random booster searches
        self.booster: Booster = Booster(set_code="lea", cards=[], index=0)
        # help message
        self.help_msg: str = """Help
chaos: random chaotic effect. Can be beneficial or not. Run it every upkeep

planar: roll a planar die
    -> 4 blanks, 1 chaos, 1 planeswalk

planechase: Show the planechase planar deck. Used for the planechase variant

archenemy: Show the archenemy Scheme deck. Used fot the archenemy variant
    -> archenemy deck -> shows the current deck
    -> archenemy ongoing -> shows the currently activated ongoing schemes
    -> archenemy abandon -> radio prompt to abandon an ongoing scheme

momir: get a random creature card with a specific cmc. Used for momir basic
    -> momir <cmc> -> random creature with cmc==<cmc>
    -> momir 2 -> random creature with cmc==2
    -> momir 10 -> random creature with cmc==100
    -> momir 14 -> error, there is currently no creature with cmc==14

draft: show thw currently open booster

new: reset a specific game mode
    -> new draft <set_code> -> get a new booster for the set with the
        specified <set_code> (3 letter code that identifies it: AFR, KLD, ELD)
    -> new planechase -> shuffle and present a new planechase deck
    -> new archenemy <deck_name> -> change and suffle a new schemes deck
        -> The available decks are:
            -> apocalypse
            -> doomsday
            -> tramble
            -> dragonfire
            -> bolas

clear, c: clear the screen
    """

    def make_session(self) -> PromptSession:
        """
        Setup prompt toolkit session for game modes

        Returns:
            PromptSession: session for game modes
        """

        # completer for the dice session
        completer: NestedCompleter = NestedCompleter.from_nested_dict(
            {
                "chaos": None,
                "planar": None,
                "planechase": None,
                "momir": None,
                "draft": None,
                "archenemy": {"deck", "ongoing", "abandon"},
                "new": {
                    "planechase": None,
                    "archenemy": {deck for deck in archenemy_decks},
                    "draft": None,
                },
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

        The commands are: planechase | clear | help

        Args:
            command (str): command provided by the user that will be processed
        """
        # properly format the input
        command_list: List[str] = command.split()
        first_word: str = command_list[0]

        if first_word == "planechase":
            # show the current planechase plane
            # allows you to change the plane
            self.planechase.run()

        elif first_word == "momir":
            # get a new random card from scryfall wit a specific cmc
            # this command is called momir because it could be usefull for
            # people using the momir vig vanguard or playin the momir format
            show_momir(int(command_list[1]))

        elif first_word == "draft":
            self.booster.run()

        elif first_word == "archenemy":
            mode: str = command_list[1]

            if mode == "deck":
                self.scheme_deck.run()

            elif mode == "ongoing":
                self.scheme_deck.run_ongoing()

            elif mode == "abandon":
                self.scheme_deck.remove_ungoing()

        elif first_word == "planar":
            # roll a planar die
            print(planar())

        elif first_word == "chaos":
            # print a random chaos effects
            print_formatted_text(HTML(choice(self.chaos_deck)))

        elif first_word == "new":
            mode: str = command_list[1]

            if mode == "planechase":
                # reset an run a new planechase planar deck
                self.planechase.shuffle()
                self.planechase.run()

            elif mode == "draft":
                self.booster.reset_booster(command_list[2])
                self.booster.run()

            elif mode == "archenemy":
                self.scheme_deck = archenemy_decks[command_list[2]]
                self.scheme_deck.shuffle()

        elif first_word in {"clear", "c"}:
            # clear the screen
            clear_screen()

        elif first_word in {"help", "h"}:
            # get help
            print(self.help_msg)

        else:
            self.not_valid()
