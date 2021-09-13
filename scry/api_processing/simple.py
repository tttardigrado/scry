from functions.general import setup_query
from api_processing.constants import ScryfallError
from api_processing.results import Results, dict_to_list_of_cards
from functions.widgets import style
import requests


def simple_search(query: str) -> dict:
    query = query.strip().replace(" ", "%20")

    r = requests.get("https://api.scryfall.com/cards/search" + query)

    if r.status_code == 404:
        raise ScryfallError(r.status_code)

    else:
        return r.json()


def show_results(query: str) -> None:
    # process the query string
    query = setup_query(query)

    # get the results from scryfall
    results: dict = simple_search(query)

    # turn the result dict to a Results object
    r: Results = Results(dict_to_list_of_cards(results))

    # show the resultson the screen
    card: int = 0
    if r.length() > 1:
        widget = r.widget(style)
        card = widget.run()

    try:
        # show the chosen card
        # or the only returned card
        r.show_card(card)
    except TypeError:
        pass
