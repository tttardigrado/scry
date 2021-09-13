from typing import Dict, List
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from functions.general import clear_screen
from functions.widgets import style, prompt_txt
import re


class Game:
    """
    Game session for the SolRing app

    Deals with storing life, experience, energy and any other needed counter
    """

    def __init__(self) -> None:
        # create the dice session
        self.session: PromptSession = self.game_session()

        # determine the SolRing toolbar text
        self.bottom_toolbar: str = " SolRing: Scryfall inside your terminal"

        # values to store
        self.values: Dict[str, float] = {}

        # notes to store
        self.notes: List[str] = []

        # edit regex expression
        self.edit_expr: re.Pattern = re.compile(
            r"^(\w+)\s{0,1}(\+|\-|\*|\/|\^)\s{0,1}(\d*)$"
        )

        # help message
        self.help_msg: str = """Help:

set: set a variable to a certain value
    -> set <var> <val> -> set the values of the variable <var> to <val>
    -> set some_variable 10
    -> set anotherVariable 20
    -> set yet another_variable 30 -> error

get: get the value of a variable
    -> get var -> prints the value of the var variable

list, ls: list all
    -> list vars
    -> ls vars -> list all varsiables
    -> list notes
    -> ls notes -> list all notes

delete, del: deletes a variable
    -> delete vars <var>
    -> del vars <var> -> delete the variable <var>
    -> delete notes <note>
    -> del notes <note> -> delete the note with index <note>

note: add a new note
    -> note <note_content> -> add <note_content> to the list of notes

clear, c: clear the screen

reset: reset the session

edit, e: execute calculations on a variable and change its value to the result
    -> edit  var + x -> add x to the value of the variable
    -> edit var - x -> subtract x to the value of the variable
    -> edit var / x -> divide the value of the variable by /
    -> edit var * x -> multiply the value of the variable by x
    -> edit var ^ x -> value of the variable to the power of x
    """

    def not_valid(self) -> None:
        """
        Function that prints a message when a command is not valid
        """
        print("Not a valid command!")

    def error(self) -> None:
        """
        Function that prints a message when a command an error occurs
        """
        print("That variable does not exist!")

    def run(self) -> None:
        """
        Run the prompt.
        A session prompt will be shown, the resulting input will be processed
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
                self.process_game_input(text)
            except Exception:
                self.not_valid()

    def game_session(self) -> PromptSession:
        """
        Setup prompt toolkit session for dice

        Returns:
            PromptSession: session for dice
        """

        # completer for the GAME session
        completer: NestedCompleter = NestedCompleter.from_nested_dict(
            {
                "set": None,
                "get": None,
                "list": {"notes", "vars"},
                "ls": {"notes", "vars"},
                "delete": {"notes", "vars"},
                "del": {"notes", "vars"},
                "edit": None,
                "e": None,
                "note": None,
                "clear": None,
                "c": None,
                "reset": None,
                "help": None,
                "h": None,
            }
        )

        return PromptSession(completer=completer)

    def reset(self) -> None:
        response: str = input("Are you sure? [Y/N]: ")
        if response.lower() in {"yes", "y"}:
            self.values = {}
            self.notes = []
            print("Done.")
        else:
            print("Canceled.")

    def setter(self, name: str, value: str) -> None:
        self.values[name] = float(value)

    def add_note(self, note: str) -> None:
        self.notes.append(note)

    def getter(self, name: str) -> None:
        try:
            print(self.values[name])
        except KeyError:
            self.error()

    def list_vars(self) -> None:
        for key in self.values:
            print(key, " ─ ", self.values[key])

    def list_notes(self) -> None:
        i: int = 1
        for note in self.notes:
            print(i, " ─ ", note)
            i += 1

    def delete(self, name: str) -> None:
        try:
            del self.values[name]
        except KeyError:
            self.error()

    def delete_note(self, index_str: str) -> None:
        try:
            del self.notes[int(index_str) - 1]
        except ValueError:
            del self.notes[int(float(index_str)) - 1]
        except IndexError:
            self.error()

    def edit(self, name: str, operator: str, value: float) -> None:
        if operator == "+":
            self.values[name] += value
        elif operator == "-":
            self.values[name] -= value
        elif operator == "/":
            self.values[name] /= value
        elif operator == "*":
            self.values[name] *= value
        elif operator == "^":
            self.values[name] **= value
        else:
            self.not_valid()

    def process_edit(self, value: str) -> None:
        # use regex to match the edit expression
        matches = self.edit_expr.match(value)

        # non valid expression
        if not matches:
            raise ValueError("Edit expression is not valid")

        # get the values from the expression
        name, operator, val = matches.groups()

        # run the edit
        self.edit(name, operator, float(val))

    def process_game_input(self, command: str) -> None:
        """
        Process the input provided to the prompt

        The commands are: set|get|list|delete|edit|reset|note|clear|help

        Args:
            command (str): command provided by the user that will be processed
        """
        # properly format the input
        command_list: List[str] = command.split()
        first_word: str = command_list[0]

        if first_word == "set":
            self.setter(command_list[1], command_list[2])

        elif first_word == "get":
            self.getter(command_list[1])

        elif first_word in {"list", "ls"}:
            if command_list[1] == "notes":
                self.list_notes()
            elif command_list[1] == "vars":
                self.list_vars()
            else:
                self.not_valid()

        elif first_word in {"delete", "del"}:
            if command_list[1] == "notes":
                self.delete_note(command_list[2])
            elif command_list[1] == "vars":
                self.delete(command_list[2])
            else:
                self.not_valid()

        elif first_word in {"edit", "e"}:
            self.process_edit("".join(command_list[1:]))

        elif first_word == "note":
            self.add_note(" ".join(command_list[1:]))

        elif first_word in {"clear", "c"}:
            clear_screen()

        elif first_word == "reset":
            self.reset()

        elif first_word in {"help", "h"}:
            print(self.help_msg)

        else:
            self.not_valid()
