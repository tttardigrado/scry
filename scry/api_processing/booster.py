from random import randint
from dataclasses import dataclass
from typing import List, Tuple
from prompt_toolkit.application.application import Application
from prompt_toolkit.styles.style import Style
from prompt_toolkit.shortcuts.dialogs import radiolist_dialog
from scry.api_processing.random import random_card
from scry.api_processing.results import Card, json_to_card
from scry.functions.general import replace_symbols, clear_screen
from scry.functions.widgets import style


@dataclass()
class Booster:
    """
    MTG draft booster containing 15 cards
    """

    set_code: str
    cards: List[Card]
    index: int = 0

    def booster_is_empty(self) -> None:
        """
        Empty booster error message.
        """
        print(
            """Your booster is either empty or full of junk rares :).
Please try to buy a new booster using:
    new draft <3_letter_set_code>"""
        )

    def random_booster_card(self, rarity: str) -> Card:
        """
        Get a random card from a specific set and a specific rarity
        The set code is provided by the booster calss

        Args:
            rarity (str): rarity of the wanted card.
                "c" -> common
                "u" -> uncommon
                "r" -> rare
                "m" -> mythic

        Returns:
            Card: A card object for the card got from scryfall
        """
        # generate the query string
        query: str = f"?q=-type%3Abasic+set%3A{self.set_code}+rarity%3A{rarity}"

        # get a random card
        card_json: dict = random_card(query)

        # convert the card json to a card object
        return json_to_card(card_json)

    def random_booster_basic_land(self) -> Card:
        """
        Get a basic land from the set provided by the Booster class

        Returns:
            Card: A card object for the card got from scryfall
        """
        # generate the query string
        query: str = f"?q=(type%3Aland+type%3Abasic)+set%3A{self.set_code}"

        # get a random card
        card_json: dict = random_card(query)

        # convert the card json to a card object
        return json_to_card(card_json)

    def add_card_to_booster(self, rarity: str) -> None:
        """
        Add a card from a specific rarity to the booster's card list

        Args:
            rarity (str): rarity of the wanted card
        """
        self.cards.append(self.random_booster_card(rarity))

    def add_land_to_booster(self) -> None:
        """
        Add a basic land card to the booster's card list
        """
        self.cards.append(self.random_booster_basic_land())

    def add_mythic_card(self) -> None:
        """
        Add a mythic rare card to the booster
        """
        # m == mythic rare
        self.add_card_to_booster("m")

    def add_rare_card(self) -> None:
        """
        Add a rare card to the booster
        """
        # r == rare
        self.add_card_to_booster("r")

    def add_uncommon_card(self) -> None:
        """
        Add an uncommon card to the booster
        """
        # u == uncommon
        self.add_card_to_booster("u")

    def add_common_card(self) -> None:
        """
        Add a common card to the booster
        """
        # c == common
        self.add_card_to_booster("c")

    def make_booster(self) -> None:
        """
        Get all the cards that should be in a booster

        1 -> mythic/rare
        3 -> uncommons
        10 -> commons
        1 -> basic land
        """

        print("Packaging the booster...")
        # in draft boosters you have a 1 in 8 chance of pulling a mythic
        # get a random number to check if the card should be mythic
        is_mythic: bool = randint(1, 8) == 1

        if is_mythic:
            try:
                # mythic rare card
                self.add_mythic_card()
            except Exception:
                # some sets don't have mythics
                # in that case all rares should be simple rare cards
                self.add_rare_card()

        else:
            # normal rare card
            self.add_rare_card()

        # add all -- 3 -- uncommon cards
        for _ in range(3):
            self.add_uncommon_card()

        print("Buying the booster...")
        # add all -- 10 -- common cards
        for _ in range(10):
            self.add_common_card()

        print("Opening the booster...")
        # add -- 1 -- land card
        self.add_land_to_booster()

    def reset_booster(self, set_code: str) -> None:
        """
        Reset the booster

        Args:
            set_code (str): 3 letter code of the set.
                AFR -> Adventures in the forgotten realms
                MH2 -> Modern Horizons 2
        """
        self.index = 0
        self.cards = []
        self.set_code = set_code
        self.make_booster()

    def widget(self, style: Style) -> Application:
        """
        Widget for the Booster class

        Args:
            style (Style): style for this widget

        Returns:
            Application: widget for the booster
        """
        title: str = f"{self.set_code.upper()} --- Booster"

        # for every card in the booster add it to the options
        # Rarity - Name - Cost
        values: list = []
        i: int = 0
        for card in self.cards:
            rarity: str = card.rarity[0].upper()
            values.append(
                (
                    i,
                    replace_symbols(
                        f"{rarity} - {card.name} - {card.cost}",
                    ),
                )
            )
            i += 1

        return radiolist_dialog(title=title, values=values, style=style)

    def loop(self, card_buttons: List[Tuple[str, int]]) -> None:
        """
        Keep showing and executing the requested actions until he quits
        """
        while True:
            # get the current card
            card: Card = self.cards[self.index]

            # run that card's widget
            value: int = card.widget(btn=card_buttons).run()

            # process the input from the widget
            if value == 1 and self.index > 0:
                # command == Previous
                # can't go under 0
                self.index -= 1

            elif value == 2 and self.index < 14:
                # command == Next
                # can't go over the 15th (index 14) card
                self.index += 1

            elif value == 3:
                # command == Ok
                # exit the booster run loop
                break

            elif value == 4:
                # command == Open
                # open the card on the browser
                card.open_card()

            elif value == 5:
                # command == Download
                # Download the card's image to the current folder
                card.download_card()

    def run(self) -> None:
        """
        Run this Booster
        """

        # can't run empty boosters
        if len(self.cards) == 0:
            self.booster_is_empty()
            return

        # get the index of the starting card
        card_index: int = self.widget(style).run()

        # if there is an index
        if card_index is not None:
            self.index = card_index

            # buttons to be shown on cards that are provided by the booster
            card_buttons: List[Tuple[str, int]] = [
                ("Prev", 1),
                ("Next", 2),
                ("Ok", 3),
                ("Open", 4),
                ("Download", 5),
            ]
            clear_screen()
            self.loop(card_buttons)
