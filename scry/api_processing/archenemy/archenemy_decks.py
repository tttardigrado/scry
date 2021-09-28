import random
from dataclasses import dataclass, field
from typing import List
from prompt_toolkit.shortcuts.dialogs import radiolist_dialog
from scry.api_processing.archenemy.scheme import Scheme
from scry.functions.widgets import style


@dataclass()
class ArchenemyDeck:
    """
    Deck of Schemes for the archenemy format
    """
    deck_list: List[Scheme]
    ongoing: List[Scheme] = field(default_factory=list)
    ongoing_index: int = 0
    index: int = 0

    def __post_init__(self):
        self.shuffle()

    def no_ongoing(self) -> None:
        """
        Function ran when there is no ongoing schemes activated
        """
        print(
            """There are no ongoing schemes.
I'm your master and I'm sad!"""
        )

    def shuffle(self) -> None:
        """
        Shuffle the deck and reset the index
        """
        random.shuffle(self.deck_list)
        # reset the index
        self.index = 0

    def remove_ungoing(self) -> None:
        """
        Show a prompt that asks for what ongoing scheme
        the user wants to abandon.
        """
        # if there are no ongoing schemes to abandon
        if not self.ongoing:
            self.no_ongoing()
            return

        # get and format into a list
        # all active ongoing schemes
        values: list = []
        i: int = 0
        for card in self.ongoing:
            # (index in ongoing, name of the scheme)
            values.append((i, card.name))
            i += 1

        # show the dialog with the schemes to abandon
        # index == None -> dialog canceled
        index: int = radiolist_dialog(
            title="Abandon Ongoing Schemes",
            text="Which Scheme Should My Master Abandon?",
            values=values,
            style=style,
        ).run()

        # dialog was not canceled
        if index is not None:
            # "abandon" i.e. remove the selected scheme
            del self.ongoing[index]

    def run_ongoing(self) -> None:
        """
        Run and show the currently active ongoing schemes
        """
        # if there are no ongoing schemes to show
        if not self.ongoing:
            self.no_ongoing()
            return

        # run loop
        while True:
            card: Scheme = self.ongoing[self.ongoing_index]

            # show the card widget
            value: int = card.widget(self.ongoing_index).run()

            if value == 1 and self.ongoing_index > 0:
                # command == Prev
                # can't have an index bellow 0
                self.ongoing_index -= 1

            elif value == 2 and self.ongoing_index < len(self.ongoing) - 1:
                # command == Next
                # can't have an index larger than the number of cards
                self.ongoing_index += 1

            elif value == 3:
                # quit
                break

    def run(self) -> None:
        """
        Run the planechase deck
        """
        while True:
            card: Scheme = self.deck_list[self.index]

            # check if the card is an ongoing scheme
            # check if it has already been added/set in motion
            # only should add non-previously-added and ongoing schemes
            should_be_set_in_motion: bool = (
                card.is_ongoing and not card.has_been_added
            )
            if should_be_set_in_motion:
                # add to the ongoing list
                self.ongoing.append(card)
                # change the status to been set in motion/added
                self.deck_list[self.index].has_been_added = True

            # show the card widget
            value: int = card.widget(self.index).run()

            if value == 1 and self.index > 0:
                # command == Prev
                # can't have an index bellow 0
                self.index -= 1

            elif value == 2 and self.index < len(self.deck_list) - 1:
                # command == Next
                # can't have an index larger than the number of cards
                self.index += 1

            elif value == 3:
                # quit
                break
