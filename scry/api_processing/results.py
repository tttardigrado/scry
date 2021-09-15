import requests
from dataclasses import dataclass, field
from typing import List, Dict
from functions.widgets import style
from functions.general import open_on_browser, replace_symbols, wrap_txt
from prompt_toolkit import HTML
from prompt_toolkit.shortcuts.dialogs import (
    button_dialog,
    radiolist_dialog,
    Application,
)
from prompt_toolkit.styles import Style


card_back_link: str = (
    "https://c1.scryfall.com/file/scryfall-card-backs/large/59/597b79b3-7d77-4261-871a-60dd17403388.jpg?1562636819"
)


def make_legality(legality: dict) -> Dict[str, List[str]]:
    final_legality: Dict[str, List[str]] = {"banned": [], "restricted": []}
    for f in legality:
        if legality[f] == "banned":
            final_legality["banned"].append(f)
        elif legality[f] == "restricted":
            final_legality["restricted"].append(f)
    return final_legality


def make_image_link(card: dict) -> str:
    try:
        return card["image_uris"]["png"]
    except Exception:
        return card_back_link


@dataclass()
class Card:
    name: str = "---"
    cost: str = "---"
    typeline: str = "---"
    text: str = "---"
    lore: str = "---"
    power: int = 0
    toughness: int = 0
    loyalty: int = 0
    artist: str = "---"
    rarity: str = "---"
    set_code: str = "---"
    set_number: int = 0
    legality: Dict[str, List[str]] = field(default_factory=dict)
    url: str = "https://scryfall.com/"
    image: str = ""
    reserved: bool = False

    def is_creature(self) -> bool:
        return "creature" in self.typeline.lower()

    def is_pw(self) -> bool:
        return "planeswalker" in self.typeline.lower()

    def is_banned(self) -> bool:
        return self.legality["banned"] != []

    def is_restricted(self) -> bool:
        return self.legality["restricted"] != []

    def has_legality_restrictions(self) -> bool:

        return self.is_banned() or self.is_restricted()

    def b_n_r_string(self, ban_type: str) -> str:
        formats: str = ", ".join(self.legality[ban_type])
        label: str = ban_type.capitalize()
        return f"<ansired><b>{label}:</b></ansired> {formats}\n"

    def widget_text(self) -> str:
        text: str = f"""
— — — — —
{self.name} — — — {self.cost}

— — — — —
<b>TypeLine: </b>{self.typeline}

— — — — —

{wrap_txt(self.text)}
"""
        if self.lore != "No Flavor Text":
            text += f"<ansiblue>{wrap_txt(self.lore)}</ansiblue>\n"

        text += "— — — — —"
        if self.is_creature():
            text += f"\n<b>P/T:</b> {self.power}/{self.toughness}\n\n— — — — —"
        elif self.is_pw():
            text += f"\n<b>Loyalty:</b> {self.loyalty}\n\n— — — — —"

        text += f"""
<b>Set:</b> {self.set_code}
<b>Number:</b> {self.set_number}
<b>Rarity:</b> {self.rarity}
<b>Artist: </b>{self.artist}

"""
        if self.reserved:
            text += "<b><ansired>Reserved List</ansired></b>\n\n"

        text += "— — — — —\n"

        if self.is_banned():
            text += self.b_n_r_string("banned")

        if self.is_restricted():
            text += self.b_n_r_string("restricted")

        text = replace_symbols(text)
        return text

    def widget(
            self,
            btn: list = [("Ok", 1), ("Open", 2), ("Download", 3)],
    ) -> Application:
        return button_dialog(
            title=self.name,
            style=style,
            buttons=btn,
            text=HTML(self.widget_text()),
        )

    def download_card(self) -> None:
        img_data = requests.get(self.image).content
        with open(self.name + ".png", "wb") as handler:
            handler.write(img_data)

    def open_card(self) -> None:
        open_on_browser(self.url)

    def show(self) -> None:
        value: int = self.widget().run()
        if value == 2:
            self.open_card()
        elif value == 3:
            self.download_card()


def json_to_card(card: dict) -> Card:
    legality: Dict[str, List[str]] = make_legality(card["legalities"])
    return Card(
        name=card.get("name") or "No Name",
        cost=card.get("mana_cost") or "No Cost",
        typeline=card.get("type_line") or "No TypeLine",
        text=card.get("oracle_text") or "No Oracle Text",
        lore=card.get("flavor_text") or "No Flavor Text",
        power=card.get("power") or 0,
        toughness=card.get("toughness") or 0,
        loyalty=card.get("loyalty") or 0,
        artist=card.get("artist") or "No Artist",
        rarity=card.get("rarity") or "C",
        set_code=card.get("set") or "XXX",
        set_number=card.get("collector_number") or 0,
        legality=legality,
        url=card.get("scryfall_uri") or "https://scryfall.com/",
        image=make_image_link(card),
        reserved=card.get("reserved") or False,
    )


def dict_to_list_of_cards(to_convert: dict) -> List[Card]:
    results: List[Card] = []
    for card in to_convert["data"]:
        results.append(json_to_card(card))
    return results


@dataclass()
class Results:
    results: List[Card]

    def length(self) -> int:
        return len(self.results)

    def widget(self, style: Style) -> Application:
        values: list = []

        i: int = 0
        for card in self.results:
            values.append((i, replace_symbols(f"{card.name} --- {card.cost}")))
            i += 1

        return radiolist_dialog(title="Results", values=values, style=style)

    def show_card(self, index: int):
        value: int = self.results[index].widget().run()
        if value == 2:
            open_on_browser(self.results[index].url)
        elif value == 3:
            self.results[index].download_card()
