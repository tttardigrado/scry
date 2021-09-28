# Scry

**Scry** is your companion for everything *"Magic: the gathering"* inside of your terminal, but this one does not need to be nerfed.

## Tech

* **Languages**: Python
* **Libraries**: Prompt_toolkit, Click, Requests
* **API**: Scryfall

## Instalation

If you alread have *Python* and *pip* installed, simply clone this repo and run the `install.sh` script or run `pip install -e .` on the base folder

---
---

## Use

## Game Session

`$ scry`

* `set`: set a variable to a certain value
    * set <var> <val> -> set the values of the variable <var> to <val>
    * set some_variable 10
    * set anotherVariable 20
    * set yet another_variable 30 -> error

* `get`: get the value of a variable
    *  get var -> prints the value of the var variable

* `list, ls`: list all
    * list vars
    * ls vars -> list all varsiables
    * list notes
    * ls notes -> list all notes

* `delete, del`: deletes a variable
    * delete vars <var>
    * del vars <var> -> delete the variable <var>
    * delete notes <note>
    * del notes <note> -> delete the note with index <note>

* `note`: add a new note
    * note <note_content> -> add <note_content> to the list of notes

* `clear`, c: clear the screen

* `reset`: reset the session

* `edit, e`: execute calculations on a variable and change its value to the result
    * edit  var + x -> add x to the value of the variable
    * edit var - x -> subtract x to the value of the variable
    * edit var / x -> divide the value of the variable by /
    * edit var * x -> multiply the value of the variable by x
    * edit var ^ x -> value of the variable to the power of x

---

## Simple Session

`$ scry -s`

* `search`: search scryfall for a card name
    * search <name> -> searches scryfall for name
    * search Jace, the mind -> return Jace, the mind sculptor
    * search red -> returns all cards with red on their names
    * Tormod -> returns all cards with tormod in their names.
    (search is implied)

* `random`: get a random card from scryfall

* `momir`: get a random creature card with a specific cmc
    * momir <cmc> -> random creature card with the specified cmc
    * momor 2 -> random creature  cmc=2
    * momir 19 -> error (there is no creature with cmc=19)

* `query`: search scryfall for a card that is filteres based on a query string
    * query <type> <querystr>
    * query random <querystr> -> get a random card filtered by <querystr>
    * query search <querystr> -> search for a card filtered by <querystr>
    * query <querystr> -> search for a card filtered by <querystr>

* `clear, c`: clear the screen

---

## Mode Session

`$ scry -m`

* `chaos`: random chaotic effect. Can be beneficial or not. Run it every upkeep

* `planar`: roll a planar die
    * 4 blanks, 1 chaos, 1 planeswalk

* `planechase`: Show the planechase planar deck. Used for the planechase variant

* `archenemy`: Show the archenemy Scheme deck. Used fot the archenemy variant
    * archenemy deck -> shows the current deck
    * archenemy ongoing -> shows the currently activated ongoing schemes
    * archenemy abandon -> radio prompt to abandon an ongoing scheme

* `momir`: get a random creature card with a specific cmc. Used for momir basic
    * momir <cmc> -> random creature with cmc==<cmc>
    * momir 2 -> random creature with cmc==2
    * momir 10 -> random creature with cmc==100
    * momir 14 -> error, there is currently no creature with cmc==14

* `draft`: show thw currently open booster

* `new`: reset a specific game mode
    * new draft <set_code> -> get a new booster for the set with the
        specified <set_code> (3 letter code that identifies it: AFR, KLD, ELD)
    * new planechase -> shuffle and present a new planechase deck
    * new archenemy <deck_name> -> change and suffle a new schemes deck
        * The available decks are:
            * `apocalypse`
            * `doomsday`
            * `tramble`
            * `dragonfire`
            * `bolas`

* `clear, c`: clear the screen

---

### Dice Session

`$ scry -d`

* `roll`: roll a die
    * roll xdy+z -> roll x y-sided die and add z
    * d6 -> roll 1 6 sided dice
    * 5d8 -> roll 5 8 sided die
    * 3d4+2 -> roll 3 4 sided die and add 2
    * 6d20-2 -> roll 6 20 sided die and subtract 2

* `coin`: flip a coin
    * heads or tails

* `planar`: roll a planar die
    * 4 blanks, 1 chaos, 1 planeswalk

* `choose`: choose a value from a provided list
    * choose xxx | yyy | zzz -> return one of xxx, yyy, zzz.
    * | separates the values
    * choose me | you | they | your self | my self
    * choose 1 | 10 | 55 | 100
    * choose 20 | try | 55 | test | roll

* `range`: return a number between a provided range
    * range <first> <second> -> return <first> < number < <second>
    * range 1 10 -> one of: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    * range 5 1 -> one of: 1, 2, 3, 4, 5
    * range 1 -2 -> one of: -2, -1, 0, 1
    * range -1, -3 -> one of: -3, -2, -1

* `hand`: choose a random card from target player's hand
    * hand <number_of_cards> -> returns a number within [1, number_of_cards]
    * hand 7 -> one of: 1, 2, 3, 4, 5, 6, 7
    * hand -1 -> not valid

* `clear, c`: clear the screen

---
---

# TO DO

- [] Create Kitty session file for scry