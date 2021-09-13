from dataclasses import dataclass
from typing import List
from functions.widgets import style
from prompt_toolkit import HTML
from prompt_toolkit.shortcuts.dialogs import (
    button_dialog,
    Application,
)

@dataclass()
class Plane:
    name: str = ""
    plane: str = ""
    text: str = ""
    chaos: str = ""
    
    def widget_text(self) -> str:
        return f"""
— — — — —
{self.name}
— — — — —
<ansired>Plane — {self.plane}</ansired>
— — — — —
{self.text}
— — — — —
Whenever you roll ꩜, {self.chaos}
— — — — —
"""

    def widget(self, index) -> Application:
        return button_dialog(
            title=f"{self.name} — {index}",
            style=style,
            buttons=[("Prev", 1), ("Next", 2), ("Exit", 3)],
            text=HTML(self.widget_text()),
        )