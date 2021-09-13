class ScryfallError(Exception):
    """
    Error for anything related to scryfall and requests to scryfall

    Args:
        code (int): the code that got returned from the http request.
    """

    def __init__(self, code: int):
        self.code: int = code

    def __str__(self):
        return f"Error: HTTP request to scryfall returned a {self.code}"
