from dataclasses import dataclass
from scry.functions.general import wrap_txt
from scry.functions.widgets import style
from prompt_toolkit import HTML
from prompt_toolkit.shortcuts.dialogs import (
    button_dialog,
    Application,
)


@dataclass()
class Plane:
    """
    Plane card for the planechase format
    """
    name: str = ""
    plane: str = ""
    text: str = ""
    chaos: str = ""

    def __post_init__(self):
        self.text = wrap_txt(self.text)
        self.chaos = wrap_txt(self.chaos, width=40)

    def widget_text(self) -> str:
        """
        Text for the plane widget
        """
        return f"""
— — — — —
{self.name}
— — — — —
<ansired>Plane — {self.plane}</ansired>
— — — — —
{self.text}
— — — — —
Whenever you roll ꩜ , {self.chaos}
— — — — —
"""

    def widget(self, index: int) -> Application:
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
