import click
from scry.sessions.simple import Simple
from scry.sessions.dice import Dice
from scry.sessions.game import Game
from scry.sessions.modes import Mode


@click.command()
@click.option(
    "--dice",
    "-d",
    is_flag=True,
    help="Various functions related to dice rolling and choices",
)
@click.option(
    "--simple",
    "-s",
    is_flag=True,
    help="Search for cards by name on scryfall",
)
@click.option(
    "--mode",
    "-m",
    is_flag=True,
    help="Tools for non-standard game modes",
)
def main(dice: bool, simple: bool, mode: bool) -> None:
    """
    Main function for the scry app
    It creates the right session, depending on the flag provided by click,
    Then it loops the session prompt

    Args:
        random (bool): -r flag provided by Click.
            Determines if the session is a random session.
    """
    # Create session
    if dice:
        session = Dice()
    elif simple:
        session = Simple()
    elif mode:
        session = Mode()
    else:
        # create DEFAULT Game session
        session = Game()

    # main loop
    while True:
        # run the session until the user quits
        session.run()


if __name__ == "__main__":
    main()
