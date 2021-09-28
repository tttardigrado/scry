from dataclasses import dataclass
from typing import Any
from scry.functions.general import wrap_txt
from scry.functions.widgets import style
from prompt_toolkit import HTML
from prompt_toolkit.shortcuts.dialogs import button_dialog
from prompt_toolkit.application import Application


@dataclass()
class Scheme:
    is_ongoing: bool = False
    name: str = ""
    text: str = ""
    lore: str = ""
    abandon: str = ""
    has_been_added: bool = False

    def __post_init__(self):
        self.text = wrap_txt(self.text)
        self.lore = wrap_txt(self.lore)
        self.abandon = wrap_txt(self.abandon)

    def typeline_str(self) -> str:
        if self.is_ongoing:
            return "<ansired>Ongoing Scheme</ansired>"

        return "<ansired>Scheme</ansired>"

    def lore_str(self) -> str:
        if not self.lore == "":
            return f"\n<ansiblue>{self.lore}</ansiblue>\n— — — — —"

        return " "

    def abandon_str(self) -> str:
        if not self.abandon == "":
            return f"\n<ansired>{self.abandon}</ansired>\n— — — — —"

        return " "

    def widget_text(self) -> str:
        """
        Text for the scheme widget
        """
        text: str = f"""
— — — — —
{self.name}
— — — — —
{self.typeline_str()}
— — — — —
{self.text}
— — — — —"""

        text += self.lore_str()
        text += self.abandon_str()

        return text

    def widget(self, index: int) -> Application[Any]:
        """
        Widget for the Plane card

        Args:
            index (int): index of the card on the deck

        Returns:
            Application: Widget for this card
        """
        return button_dialog(
            title=f"{self.name} — {index}",
            style=style,
            buttons=[("Prev", 1), ("Next", 2), ("Exit", 3)],
            text=HTML(self.widget_text()),
        )
