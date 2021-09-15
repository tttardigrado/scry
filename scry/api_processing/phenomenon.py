from dataclasses import dataclass
from functions.widgets import style
from functions.general import wrap_txt
from prompt_toolkit import HTML
from prompt_toolkit.shortcuts.dialogs import (
    button_dialog,
    Application,
)


@dataclass()
class Phenomenon:
    """
    Phenomenon card class for the planechase format
    """
    name: str = ""
    text: str = ""

    def __post_init__(self):
        # wrap the text
        self.text = wrap_txt(self.text)

    def widget_text(self) -> str:
        """
        The text that should be displayed on the widget for a phenomenon card

        Returns:
            str: text for the phenomenon widget
        """
        return f"""
— — — — —
{self.name}
— — — — —
<ansired>Phenomenon</ansired>
— — — — —
{self.text}
— — — — —
"""

    def widget(self, index: int) -> Application:
        """
        The terminal widget for a phenomenon card

        Args:
            index (int): index of the card on the planar deck

        Returns:
            Application: card widget
        """
        return button_dialog(
            title=f"{self.name} — {index}",
            style=style,
            buttons=[("Prev", 1), ("Next", 2), ("Exit", 3)],
            text=HTML(self.widget_text()),
        )
