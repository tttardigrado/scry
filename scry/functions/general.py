from os import system
from typing import Any
import webbrowser
from textwrap import wrap


def clear_screen() -> None:
    """
    Utility function for clearing the console screen.
    """
    _ = system("clear")


def open_on_browser(url: str) -> None:
    """
    Utility function that opens an url on the browser.
    """
    webbrowser.open(url=url, new=2)


def replace_symbols(text: str) -> str:
    """
    Utility function that replaces mana symbols/costs by emoji.

    Args:
        text (str): text in which the symbols should be replaced

    Returns:
        str: input text with the symbols replaced
    """
    return (
        text.replace("{W}", "🌞")
        .replace("{U}", "💧")
        .replace("{B}", "💀")
        .replace("{R}", "🔥")
        .replace("{G}", "🌲")
        .replace("{C}", "⯁")
        .replace("{E}", "⚡")
        .replace("{S}", "❄")
        .replace("{", "(")
        .replace("}", ")")
    )


def setup_query(query: str) -> str:
    """
    Process a query and make it viable for the scryfall search

    Args:
        query (str): query string that will filter the results

    Returns:
        str: processed query string
    """
    if query and (not query.startswith("?q=")):
        query = "?q=" + query

    return query


def wrap_txt(text: str, width: int = 60, separator: str = "\n") -> str:
    """
    Wrap a text string.

    Args:
        text (str): (multi-line) string that should be wrapped.
        width (int, optional): maximum width of the strings. Defaults to 60.

    Returns:
        str: Wrapped string
    """
    # split the string into various lines
    # if the string is a multi-line string
    lines: list[str] = text.split("\n")

    # wrap every line to the max width
    wrapped: str = ""
    for line in lines:
        # add the current line after wrapping it
        wrapped += separator.join(wrap(line, width))
        # add line separator
        wrapped += separator

    return wrapped


def pprint_dice(value: Any) -> None:
    print(f"\n——— {value} ———\n")
