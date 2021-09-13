from prompt_toolkit import PromptSession
from functions.widgets import prompt_txt, style, bottom_toolbar

class ScrySession:
    """
    Base class for Scry Sessions
    """

    def __init__(self) -> None:
        self.session = self.make_session()
        # determine the SolRing toolbar text
        self.bottom_toolbar: str = bottom_toolbar
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
        A session prompt will be shown the resulting input will be processed
        """
        # create and show prompt
        text: str = self.session.prompt(
            prompt_txt,
            bottom_toolbar=self.bottom_toolbar,
            complete_while_typing=True,
            style=style,
        )

        if text:
            # process the input
            try:
                self.process_input(text)
            except Exception:
                self.not_valid()

    def make_session(self) -> PromptSession:
        """
        Setup prompt toolkit session for simple search

        Returns:
            PromptSession: session for simple search
        """

        return PromptSession(complete_while_typing=True)

    def process_input(self, command: str):
        """
        Process the input provided to the prompt

        If no command is provided, search is the default

        Args:
            command (str): command provided by the user that will be processed
        """
        pass