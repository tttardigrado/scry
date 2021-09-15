from typing import List
from random import choice
from prompt_toolkit import PromptSession, print_formatted_text
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.formatted_text.html import HTML
from functions.general import clear_screen
from api_processing.planechase import planar_deck
from api_processing.random import show_momir
from api_processing.booster import Booster
from functions.dice import planar
from functions.constants import chaos_effects


class Mode:
    """
    Game modes session for the SolRing app

    Deals with alternative game modes like momir, planechase, archenemy...
    """

    def __init__(self) -> None:
        # create planechase
        self.planechase = planar_deck
        # chaos effects for the CHAOS MAGIC format
        self.chaos_deck: List[str] = chaos_effects
        # draft booster for random booster searches
        self.booster: Booster = Booster(set_code="lea", cards=[], index=0)
        # create the dice session
        self.session: PromptSession = self.mode_session()
        # determine the SolRing toolbar text
        self.bottom_toolbar: str = " SolRing: Scryfall inside your terminal"
        # help message
        self.help_msg: str = "Help"

    def not_valid(self) -> None:
        """
        Function that prints a message when a command is not valid
        """
        print("Not a valid command!")

    def error(self) -> None:
        """
        Function that prints a message when an error occurs
        """
        print("Got an error trying to fetch this card!")

    def run(self) -> None:
        """
        Run the prompt.
        A session prompt will be shown, the resulting input will be processed
        """
        # create and show prompt
        text: str = self.session.prompt(
            ">>> ",
            bottom_toolbar=self.bottom_toolbar,
            complete_while_typing=True,
        )

        if text:
            # process the input
            try:
                self.process_mode_input(text)
            except Exception:
                self.not_valid()

    def mode_session(self) -> PromptSession:
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
                "new": {"planechase", "archenemy", "draft"},
                "clear": None,
                "c": None,
                "help": None,
                "h": None,
            }
        )

        return PromptSession(completer=completer)

    def process_mode_input(self, command: str) -> None:
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
            pass

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
                pass

        elif first_word in {"clear", "c"}:
            # clear the screen
            clear_screen()

        elif first_word in {"help", "h"}:
            # get help
            print(self.help_msg)

        else:
            self.not_valid()
