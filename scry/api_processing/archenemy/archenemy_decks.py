import random
from dataclasses import dataclass, field
from typing import List
from prompt_toolkit.shortcuts.dialogs import radiolist_dialog
from scry.api_processing.archenemy.scheme import Scheme
from scry.functions.widgets import style


@dataclass()
class ArchenemyDeck:
    deck_list: List[Scheme]
    ongoing: List[Scheme] = field(default_factory=list)
    ongoing_index: int = 0
    index: int = 0

    def __post_init__(self):
        self.shuffle()

    def no_ongoing(self) -> None:
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
        if not self.ongoing:
            self.no_ongoing()
            return

        values: list = []
        i: int = 0
        for card in self.ongoing:
            values.append((i, card.name))
            i += 1

        index: int = radiolist_dialog(
            title="Abandon Ongoing Schemes",
            text="Which Scheme Should My Master Abandon?",
            values=values,
            style=style,
        ).run()

        if index is not None:
            del self.ongoing[index]

    def run_ongoing(self) -> None:
        if not self.ongoing:
            self.no_ongoing()
            return

        while True:
            card: Scheme = self.ongoing[self.ongoing_index]

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

            if card.is_ongoing and not card.has_been_added:
                self.ongoing.append(card)
                self.deck_list[self.index].has_been_added = True

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
