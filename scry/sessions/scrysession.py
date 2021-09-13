class ScrySession:
    """
    Base class for Scry Sessions
    """

    def __init__(self) -> None:
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

        # completer for the simple session
        completer: NestedCompleter = NestedCompleter.from_nested_dict(
            {
                "clear": None,
                "c": None,
                "random": None,
                "search": None,
                "help": None,
                "h": None,
                "momir": None,
                "query": {"random": {"?q="}, "search": {"?q="}, "?q=": None},
            }
        )

        return PromptSession(completer=completer, complete_while_typing=True)

    def process_simple_input(self, command: str):
        """
        Process the input provided to the prompt

        The commands are: clear | search | random | help | momir | query

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

        elif first_word == "momir":
            # get a new random card from scryfall wit a specific cmc
            # this command is called momir because it could be usefull for
            # people using the momir vig vanguard or playin the momir format
            show_momir(int(commands[1]))

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