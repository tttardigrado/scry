from scry.api_processing.results import Card, json_to_card
from scry.api_processing.constants import ScryfallError
from scry.functions.general import setup_query
import requests


def random_card(query: str = "") -> dict:
    """
    Get a random card from scryfall

    Args:
        query (str, optional): query string to provide to the scryfall api.
            Defaults to ""

    Raises:
        ScryfallError: raised if the status code of the request is a 404

    Returns:
        dict: random card got from scryfall
    """

    # create the random search url
    url: str = "https://api.scryfall.com/cards/random/" + query

    # request random card to scryfall
    r = requests.get(url)

    # check if the request was/was not successfull
    if r.status_code == 404:
        raise ScryfallError(r.status_code)

    else:
        # return the card got from scryfall
        return r.json()


def show_momir(cmc: int) -> None:
    """
    Get and display a random creature card with a specified cmc
    It's called momir, because the momir basic format is based on
    getting random creatures with a specific cmc.

    Args:
        cmc (int): converted mana cost of the card
    """
    # cmc%3D{cmc}
    #   -> query string for a specific cmc
    #
    # type%3Acreature
    #   -> query string for a creature card
    show_random(f"?q=type%3Acreature+legal%3Avintage+cmc%3D{cmc}")


def show_random(query: str = "") -> None:
    """
    Get and display a random card from scryfall

    Args:
        query (str, optional): a string providing filters for scryfall.
        Defaults to "".
    """
    # process the query string
    query = setup_query(query)

    # get a random card
    card_json: dict = random_card(query)

    # convert the card json to a card object
    card: Card = json_to_card(card_json)

    # show the card
    card.show()
