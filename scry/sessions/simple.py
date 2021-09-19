from typing import List
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from scry.functions.general import clear_screen
from scry.sessions.scrysession import ScrySession
from scry.api_processing.random import show_random
from scry.api_processing.constants import ScryfallError
from scry.api_processing.simple import show_results


class Simple(ScrySession):
    """
    Simple session for the SolRing app

    Deals with creating the simple prompt and the processing the input

    Simple session allows you to search scryfall for named cards
    """

    def __init__(self) -> None:
        ScrySession.__init__(self)
        # help message
        self.help_msg: str = """Help
search: search scryfall for a card name
    -> search <name> -> searches scryfall for name
    -> search Jace, the mind -> return Jace, the mind sculptor
    -> search red -> returns all cards with red on their names
    -> Tormod -> returns all cards with tormod on their names.
    (search is implied)

random: get a random card from scryfall

momir: get a random creature card with a specific cmc
    -> momir <cmc> -> random creature card with the specified cmc
    -> momor 2 -> random creature  cmc=2
    -> momir 19 -> error (there is no creature with cmc=19)

query: search scryfall for a card that is filteres based on a query string
    -> query <type> <querystr>
    -> query random <querystr> -> get a random card filtered by <querystr>
    -> query search <querystr> -> search for a card filtered by <querystr>
    -> query <querystr> -> search for a card filtered by <querystr>

clear, c: clear the screen
        """

    def make_session(self) -> PromptSession:
        """
        Setup prompt toolkit session for simple search

        Returns:
            PromptSession: session for simple search
        """

        # completer for the simple session
        completer: NestedCompleter = NestedCompleter.from_nested_dict(
            {
                "clear": None,
                "c": None,
                "random": None,
                "search": None,
                "help": None,
                "h": None,
                "query": {"random": {"?q="}, "search": {"?q="}, "?q=": None},
            }
        )

        return PromptSession(completer=completer, complete_while_typing=True)

    def process_input(self, command: str):
        """
        Process the input provided to the prompt

        The commands are: clear | search | random | help | query

        If no command is provided, search is the default

        Args:
            command (str): command provided by the user that will be processed
        """
        # properly format the input
        commands: List[str] = command.lower().split()
        first_word: str = commands[0]

        if first_word in {"clear", "c"}:
            # clears the screen
            clear_screen()

        elif first_word == "query":
            if commands[1] == "random":
                # query for a random card
                show_random("".join(commands[2:]))

            elif commands[1] == "search":
                # query for a card
                show_results("".join(commands[2:]))

            else:
                # query for a card
                show_results("".join(commands[1:]))

        elif first_word == "search":
            # searches for the card name
            show_results("%20".join(commands[1:]))

        elif first_word == "random":
            # get a new random card from scryfall
            show_random()

        elif first_word in {"help", "h"}:
            # get help
            print(self.help_msg)

        else:
            try:
                # searches for the card name
                show_results("%20".join(commands))

            except ScryfallError:
                self.error()

            except Exception:
                self.not_valid()
