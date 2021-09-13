from os import system
import webbrowser


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
    if query and (not query.startswith("?q=")):
        query = "?q=" + query

    return query
