from dataclasses import dataclass
from typing import List, Union
from scry.api_processing.planes import Plane
from scry.api_processing.phenomenon import Phenomenon
from random import shuffle

Planechase_Card = Union[Plane, Phenomenon]


@dataclass()
class Planechase:
    """
    Planechase deck for the planechase format
    """
    deck: List[Planechase_Card]
    length: int
    index: int

    def shuffle(self) -> None:
        """
        Shuffle the deck and reset the index
        """
        shuffle(self.deck)
        # reset the index
        self.index = 0

    def run(self) -> None:
        """
        Run the planechase deck
        """
        while True:
            value: int = self.deck[self.index].widget(self.index).run()

            if value == 1 and self.index > 0:
                # command == Prev
                # can't have an index bellow 0
                self.index -= 1

            elif value == 2 and self.index < self.length - 1:
                # command == Next
                # can't have an index larger than the number of cards
                self.index += 1

            elif value == 3:
                # quit
                break


deck: List[Planechase_Card] = [
    Plane(
        name="Academy at Tolaria West",
        plane="Dominaria",
        text="At the beginning of your end step, if you have no cards in hand, draw seven cards.",
        chaos="discard your hand."
    ),
    Plane(
        name="Agyrem",
        plane="Ravnica",
        text="""Whenever a white creature dies, return it to the battlefield under its owner’s control at the beginning of the next end step.
Whenever a nonwhite creature dies, return it to its owner’s hand at the beginning of the next end step.""",
        chaos="creatures can’t attack you until a player planeswalks."
    ),
    Plane(
        name="Akoum",
        plane="Zendikar",
        text="Players may cast enchantment spells as though they had flash.",
        chaos="destroy target creature that isn’t enchanted."
    ),
    Plane(
        name="Aretopolis",
        plane="Kephalai",
        text="""When you planeswalk to Aretopolis or at the beginning of your upkeep, put a scroll counter on Aretopolis, then you gain life equal to the number of scroll counters on it.
When Aretopolis has ten or more scroll counters on it, planeswalk.""",
        chaos="put a scroll counter on Aretopolis, then draw cards equal to the number of scroll counters on it."
    ),
    Plane(
        name="Astral Arena",
        plane="Kolbahan",
        text="""No more than one creature can attack each combat.
No more than one creature can block each combat.""",
        chaos="Astral Arena deals 2 damage to each creature."
    ),
    Plane(
        name="Bant",
        plane="Alara",
        text="All creatures have exalted. (Whenever a creature attacks alone, it gets +1/+1 until end of turn for each instance of exalted among permanents its controller controls.)",
        chaos="put a divinity counter on target green, white, or blue creature. That creature has indestructible for as long as it has a divinity counter on it."
    ),
    Plane(
        name="Bloodhill Bastion",
        plane="Equilor",
        text="Whenever a creature enters the battlefield, it gains double strike and haste until end of turn.",
        chaos="exile target nontoken creature you control, then return it to the battlefield under your control."
    ),
    Plane(
        name="Celestine Reef",
        plane="Luvion",
        text="Creatures without flying or islandwalk can’t attack.",
        chaos="until a player planeswalks, you can’t lose the game and your opponents can’t win the game."
    ),
    Plane(
        name="Cliffside Market",
        plane="Mercadia",
        text="When you planeswalk to Cliffside Market or at the beginning of your upkeep, you may exchange life totals with target player.",
        chaos="exchange control of two target permanents that share a card type."
    ),
    Plane(
        name="Edge of Malacol",
        plane="Belenon",
        text="If a creature you control would untap during your untap step, put two +1/+1 counters on it instead.",
        chaos="untap each creature you control."
    ),
    Plane(
        name="Eloren Wilds",
        plane="Shandalar",
        text="Whenever a player taps a permanent for mana, that player adds one mana of any type that permanent produced.",
        chaos="target player can’t cast spells until a player planeswalks."
    ),
    Plane(
        name="Feeding Grounds",
        plane="Muraganda",
        text="""Red spells cost (1) less to cast.
Green spells cost (1) less to cast.""",
        chaos="put X +1/+1 counters on target creature, where X is that creature’s mana value."
    ),
    Plane(
        name="Fields of Summer",
        plane="Moag",
        text="Whenever a player casts a spell, that player may gain 2 life.",
        chaos="you may gain 10 life."
    ),
    Plane(
        name="Furnace Layer",
        plane="New Phyrexia",
        text="When you planeswalk to Furnace Layer or at the beginning of your upkeep, select target player at random. That player discards a card. If that player discards a land card this way, they lose 3 life.",
        chaos="you may destroy target nonland permanent."
    ),
    Plane(
        name="Gavony",
        plane="Innistrad",
        text="All creatures have vigilance.",
        chaos="creatures you control gain indestructible until end of turn."
    ),
    Plane(
        name="Glen Elendra",
        plane="Lorwyn",
        text="At end of combat, you may exchange control of target creature you control that dealt combat damage to a player this combat and target creature that player controls.",
        chaos="gain control of target creature you own."
    ),
    Plane(
        name="Glimmervoid Basin",
        plane="Mirrodin",
        text="Whenever a player casts an instant or sorcery spell with a single target, that player copies that spell for each other spell, permanent, card not on the battlefield, and/or player the spell could target. Each copy targets a different one of them.",
        chaos="choose target creature. Each player except that creature’s controller creates a token that’s a copy of that creature."
    ),
    Plane(
        name="Goldmeadow",
        plane="Lorwyn",
        text="Whenever a land enters the battlefield, that land’s controller creates three 0/1 white Goat creature tokens.",
        chaos="create a 0/1 white Goat creature token."
    ),
    Plane(
        name="Grand Ossuary",
        plane="Ravnica",
        text="Whenever a creature dies, its controller distributes a number of +1/+1 counters equal to its power among any number of target creatures they control.",
        chaos="each player exiles all creatures they control and creates X 1/1 green Saproling creature tokens, where X is the total power of the creatures they exiled this way. Then planeswalk."
    ),
    Plane(
        name="Grixis",
        plane="Alara",
        text="Blue, black, and/or red creature cards in your graveyard have unearth. The unearth cost is equal to the card’s mana cost. (Pay the card’s mana cost: Return it to the battlefield. The creature gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)",
        chaos="put target creature card from a graveyard onto the battlefield under your control."
    ),
    Plane(
        name="Grove of the Dreampods",
        plane="Fabacin",
        text="When you planeswalk to Grove of the Dreampods or at the beginning of your upkeep, reveal cards from the top of your library until you reveal a creature card. Put that card onto the battlefield and the rest on the bottom of your library in a random order.",
        chaos="return target creature card from your graveyard to the battlefield."
    ),
    Plane(
        name="Hedron Fields of Agadeem",
        plane="Zendikar",
        text="Creatures with power 7 or greater can’t attack or block.",
        chaos="create a 7/7 colorless Eldrazi creature token with annihilator 1. (Whenever it attacks, defending player sacrifices a permanent.)"
    ),
    Plane(
        name="Horizon Boughs",
        plane="Pyrulea",
        text="All permanents untap during each player’s untap step.",
        chaos="you may search your library for up to three basic land cards, put them onto the battlefield tapped, then shuffle."
    ),
    Plane(
        name="Immersturm",
        plane="Valla",
        text="Whenever a creature enters the battlefield, that creature’s controller may have it deal damage equal to its power to any target of their choice.",
        chaos="exile target creature, then return it to the battlefield under its owner’s control."
    ),
    Plane(
        name="Isle of Vesuva",
        plane="Dominaria",
        text="Whenever a nontoken creature enters the battlefield, its controller creates a token that’s a copy of that creature.",
        chaos="destroy target creature and all other creatures with the same name as that creature."
    ),
    Plane(
        name="Izzet Steam Maze",
        plane="Ravnica",
        text="Whenever a player casts an instant or sorcery spell, that player copies it. The player may choose new targets for the copy.",
        chaos="instant and sorcery spells you cast this turn cost {3} less to cast."
    ),
    Plane(
        name="Jund",
        plane="Alara",
        text="Whenever a player casts a black, red, or green creature spell, it gains devour 5. (As the creature enters the battlefield, its controller may sacrifice any number of creatures. The creature enters the battlefield with five times that many +1/+1 counters on it.)",
        chaos="create two 1/1 red Goblin creature tokens."
    ),
    Plane(
        name="Kessig",
        plane="Innistrad",
        text="Prevent all combat damage that would be dealt by non-Werewolf creatures.",
        chaos="each creature you control gets +2/+2, gains trample, and becomes a Werewolf in addition to its other types until end of turn."
    ),
    Plane(
        name="Kharasha Foothills",
        plane="Mongseng",
        text="Whenever a creature you control attacks a player, for each other opponent, you may create a token that’s a copy of that creature, tapped and attacking that opponent. Exile those tokens at the beginning of the next end step.",
        chaos="you may sacrifice any number of creatures. If you do, Kharasha Foothills deals that much damage to target creature."
    ),
    Plane(
        name="Kilnspire District",
        plane="Ravnica",
        text="When you planeswalk to Kilnspire District or at the beginning of your precombat main phase, put a charge counter on Kilnspire District, then add {R} for each charge counter on it.",
        chaos="you may pay {X}. If you do, Kilnspire District deals X damage to any target."
    ),
    Plane(
        name="Krosa",
        plane="Dominaria",
        text="All creatures get +2/+2.",
        chaos="you may add {W}{U}{B}{R}{G}."
    ),
    Plane(
        name="Lair of the Ashen Idol",
        plane="Azgol",
        text="At the beginning of your upkeep, sacrifice a creature. If you can’t, planeswalk.",
        chaos="any number of target players each create a 2/2 black Zombie creature token."
    ),
    Plane(
        name="Lethe Lake",
        plane="Arkhos",
        text="At the beginning of your upkeep, mill ten cards.",
        chaos="target player mills ten cards."
    ),
    Plane(
        name="Llanowar",
        plane="Dominaria",
        text="All creatures have “{T}: Add {G}{G}.”",
        chaos="untap all creatures you control."
    ),
    Plane(
        name="Minamo",
        plane="Kamigawa",
        text="Whenever a player casts a spell, that player may draw a card.",
        chaos="each player may return a blue card from their graveyard to their hand."
    ),
    Plane(
        name="Mirrored Depths",
        plane="Karsus",
        text="Whenever a player casts a spell, that player flips a coin. If the player loses the flip, counter that spell.",
        chaos="target player reveals the top card of their library. If it’s a nonland card, you may cast it without paying its mana cost."
    ),
    Plane(
        name="Mount Keralia",
        plane="Regatha",
        text="""At the beginning of your end step, put a pressure counter on Mount Keralia.
When you planeswalk away from Mount Keralia, it deals damage equal to the number of pressure counters on it to each creature and each planeswalker.""",
        chaos="prevent all damage that planes named Mount Keralia would deal this game to permanents you control."
    ),
    Plane(
        name="Murasa",
        plane="Zendikar",
        text="Whenever a nontoken creature enters the battlefield, its controller may search their library for a basic land card, put it onto the battlefield tapped, then shuffle.",
        chaos="target land becomes a 4/4 creature that’s still a land."
    ),
    Plane(
        name="Naar Isle",
        plane="Wildfire",
        text="At the beginning of your upkeep, put a flame counter on Naar Isle, then Naar Isle deals damage to you equal to the number of flame counters on it.",
        chaos="Naar Isle deals 3 damage to target player or planeswalker."
    ),
    Plane(
        name="Naya",
        plane="Alara",
        text="You may play any number of lands on each of your turns.",
        chaos="target red, green, or white creature you control gets +1/+1 until end of turn for each land you control."
    ),
    Plane(
        name="Nephalia",
        plane="Innistrad",
        text="At the beginning of your end step, mill seven cards. Then return a card at random from your graveyard to your hand.",
        chaos="return target card from your graveyard to your hand."
    ),
    Plane(
        name="Norn's Dominion",
        plane="New Phyrexia",
        text="When you planeswalk away from Norn’s Dominion, destroy each nonland permanent without a fate counter on it, then remove all fate counters from all permanents.",
        chaos="you may put a fate counter on target permanent."
    ),
    Plane(
        name="Onakke Catacomb",
        plane="Shandalar",
        text="All creatures are black and have deathtouch.",
        chaos="creatures you control get +1/+0 and gain first strike until end of turn."
    ),
    Plane(
        name="Orochi Colony",
        plane="Kamigawa",
        text="Whenever a creature you control deals combat damage to a player, you may search your library for a basic land card, put it onto the battlefield tapped, then shuffle.",
        chaos="target creature can’t be blocked this turn."
    ),
    Plane(
        name="Orzhova",
        plane="Ravnica",
        text="When you planeswalk away from Orzhova, each player returns all creature cards from their graveyard to the battlefield.",
        chaos="for each opponent, exile up to one target creature card from that player’s graveyard."
    ),
    Plane(
        name="Otaria",
        plane="Dominaria",
        text="Instant and sorcery cards in graveyards have flashback. The flashback cost is equal to the card’s mana cost. (Its owner may cast the card from their graveyard for its mana cost. Then they exile it.)",
        chaos="take an extra turn after this one."
    ),
    Plane(
        name="Panopticon",
        plane="Mirrodin",
        text="""When you planeswalk to Panopticon, draw a card.
At the beginning of your draw step, draw an additional card.""",
        chaos="draw a card."
    ),
    Plane(
        name="Pools of Becoming",
        plane="Bolas’s Meditation Realm",
        text="At the beginning of your end step, put the cards in your hand on the bottom of your library in any order, then draw that many cards.",
        chaos="reveal the top three cards of your planar deck. Each of the revealed cards’ {CHAOS} abilities triggers. Then put the revealed cards on the bottom of your planar deck in any order."
    ),
    Plane(
        name="Prahv",
        plane="Ravnica",
        text="""If you cast a spell this turn, you can’t attack with creatures.
If you attacked with creatures this turn, you can’t cast spells.""",
        chaos="you gain life equal to the number of cards in your hand."
    ),
    Plane(
        name="Quicksilver Sea",
        plane="Mirrodin",
        text="When you planeswalk to Quicksilver Sea or at the beginning of your upkeep, scry 4. (Look at the top four cards of your library, then put any number of them on the bottom of your library and the rest on top in any order.)",
        chaos="reveal the top card of your library. You may play it without paying its mana cost."
    ),
    Plane(
        name="Raven's Run",
        plane="Shadowmoor",
        text="All creatures have wither. (They deal damage to creatures in the form of -1/-1 counters.)",
        chaos="put a -1/-1 counter on target creature, two -1/-1 counters on another target creature, and three -1/-1 counters on a third target creature."
    ),
    Plane(
        name="Sanctum of Serra",
        plane="Serra’s Realm",
        text="When you planeswalk away from Sanctum of Serra, destroy all nonland permanents.",
        chaos="you may have your life total become 20."
    ),
    Plane(
        name="Sea of Sand",
        plane="Rabiah",
        text="""Players reveal each card they draw.
Whenever a player draws a land card, that player gains 3 life.
Whenever a player draws a nonland card, that player loses 3 life.""",
        chaos="put target permanent on top of its owner’s library."
    ),
    Plane(
        name="Selesnya Loft Gardens",
        plane="Ravnica",
        text="""If an effect would create one or more tokens, it creates twice that many of those tokens instead.
If an effect would put one or more counters on a permanent, it puts twice that many of those counters on that permanent instead.""",
        chaos="until end of turn, whenever you tap a land for mana, add one mana of any type that land produced."
    ),
    Plane(
        name="Shiv",
        plane="Dominaria",
        text="All creatures have “{R}: This creature gets +1/+0 until end of turn.”",
        chaos="create a 5/5 red Dragon creature token with flying."
    ),
    Plane(
        name="Skybreen",
        plane="Kaldheim",
        text="""Players play with the top card of their libraries revealed.
Spells that share a card type with the top card of a library can’t be cast.""",
        chaos="target player loses life equal to the number of cards in their hand."
    ),
    Plane(
        name="Sokenzan",
        plane="Kamigawa",
        text="All creatures get +1/+1 and have haste.",
        chaos="untap all creatures that attacked this turn. After this main phase, there is an additional combat phase followed by an additional main phase."
    ),
    Plane(
        name="Stairs to Infinity",
        plane="Xerex",
        text="""Players have no maximum hand size.
Whenever you roll the planar die, draw a card.""",
        chaos="reveal the top card of your planar deck. You may put it on the bottom of your planar deck."
    ),
    Plane(
        name="Stensia",
        plane="Innistrad",
        text="Whenever a creature deals damage to one or more players for the first time each turn, put a +1/+1 counter on it.",
        chaos="each creature you control gains “{T}: This creature deals 1 damage to target player or planeswalker” until end of turn."
    ),
    Plane(
        name="Stronghold Furnace",
        plane="Rath",
        text="If a source would deal damage to a permanent or player, it deals double that damage to that permanent or player instead.",
        chaos="Stronghold Furnace deals 1 damage to any target."
    ),
    Plane(
        name="Takenuma",
        plane="Kamigawa",
        text="Whenever a creature leaves the battlefield, its controller draws a card.",
        chaos="return target creature you control to its owner’s hand."
    ),
    Plane(
        name="Talon Gates",
        plane="Dominaria",
        text="Any time you could cast a sorcery, you may exile a nonland card from your hand with X time counters on it, where X is its mana value. If the exiled card doesn’t have suspend, it gains suspend. (At the beginning of its owner’s upkeep, they remove a time counter. When the last is removed, the player casts it without paying its mana cost. If it’s a creature, it has haste.)",
        chaos="remove two time counters from each suspended card you own."
    ),
    Plane(
        name="Tazeem",
        plane="Zendikar",
        text="Creatures can’t block.",
        chaos="draw a card for each land you control."
    ),
    Plane(
        name="Tember City",
        plane="Kinshala",
        text="Whenever a player taps a land for mana, Tember City deals 1 damage to that player.",
        chaos="each other player sacrifices a nonland permanent."
    ),
    Plane(
        name="The Aether Flues",
        plane="Iquatana",
        text="When you planeswalk to The Aether Flues or at the beginning of your upkeep, you may sacrifice a creature. If you do, reveal cards from the top of your library until you reveal a creature card, put that card onto the battlefield, then shuffle all other cards revealed this way into your library.",
        chaos="you may put a creature card from your hand onto the battlefield."
    ),
    Plane(
        name="The Dark Barony",
        plane="Ulgrotha",
        text="Whenever a nonblack card is put into a player’s graveyard from anywhere, that player loses 1 life.",
        chaos="each opponent discards a card."
    ),
    Plane(
        name="The Eon Fog",
        plane="Equilor",
        text="Players skip their untap steps.",
        chaos="untap all permanents you control."
    ),
    Plane(
        name="The Fourth Sphere",
        plane="Phyrexia",
        text="At the beginning of your upkeep, sacrifice a nonblack creature.",
        chaos="create a 2/2 black Zombie creature token."
    ),
    Plane(
        name="The Great Forest",
        plane="Lorwyn",
        text="Each creature assigns combat damage equal to its toughness rather than its power.",
        chaos="creatures you control get +0/+2 and gain trample until end of turn."
    ),
    Plane(
        name="The Hippodrome",
        plane="Segovia",
        text="All creatures get -5/-0.",
        chaos="you may destroy target creature if its power is 0 or less."
    ),
    Plane(
        name="The Maelstrom",
        plane="Alara",
        text="When you planeswalk to The Maelstrom or at the beginning of your upkeep, you may reveal the top card of your library. If it’s a permanent card, you may put it onto the battlefield. If you revealed a card but didn’t put it onto the battlefield, put it on the bottom of your library.",
        chaos="return target permanent card from your graveyard to the battlefield."
    ),
    Plane(
        name="The Zephyr Maze",
        plane="Kyneth",
        text="""Creatures with flying get +2/+0.
Creatures without flying get -2/-0.""",
        chaos="target creature gains flying until end of turn."
    ),
    Plane(
        name="Trail of the Mage-Rings",
        plane="Vryn",
        text="Instant and sorcery spells have rebound. (The spell’s controller exiles the spell as it resolves if they cast it from their hand. At the beginning of that player’s next upkeep, they may cast that card from exile without paying its mana cost.)",
        chaos="you may search your library for an instant or sorcery card, reveal it, put it into your hand, then shuffle."
    ),
    Plane(
        name="Truga Jungle",
        plane="Ergamon",
        text="All lands have '{T}: Add one mana of any color.'",
        chaos="reveal the top three cards of your library. Put all land cards revealed this way into your hand and the rest on the bottom of your library in any order."
    ),
    Plane(
        name="Turri Island",
        plane="Ir",
        text="Creature spells cost {2} less to cast.",
        chaos="reveal the top three cards of your library. Put all creature cards revealed this way into your hand and the rest into your graveyard."
    ),
    Plane(
        name="Undercity Reaches",
        plane="Ravnica",
        text="Whenever a creature deals combat damage to a player, its controller may draw a card.",
        chaos="you have no maximum hand size for the rest of the game."
    ),
    Plane(
        name="Velis Vel",
        plane="Lorwyn",
        text="""Each creature gets +1/+1 for each other creature on the battlefield that shares at least one creature type with it. (For example, if two Elemental Shamans and an Elemental Spirit are on the battlefield, each gets +2/+2.)""",
        chaos="target creature gains all creature types until end of turn."
    ),
    Plane(
        name="Windriddle Palaces",
        plane="Belenon",
        text="""Players play with the top card of their libraries revealed.
You may play lands and cast spells from the top of any player’s library.""",
        chaos="each player mills a card."
    ),
    Phenomenon(
        name="Chaotic Aether",
        text="When you encounter Chaotic Aether, each blank roll of the planar die is a CHAOS roll until a player planeswalks away from a plane."
    ),
    Phenomenon(
        name="Interplanar Tunnel",
        text="When you encounter Interplanar Tunnel, reveal cards from the top of your planar deck until you reveal five plane cards. Put a plane card from among them on top of your planar deck, then put the rest of the revealed cards on the bottom in a random order."
    ),
    Phenomenon(
        name="Morphic Tide",
        text="When you encounter Morphic Tide, each player shuffles all permanents they own into their library, then reveals that many cards from the top of their library. Each player puts all artifact, creature, land, and planeswalker cards revealed this way onto the battlefield, then does the same for enchantment cards, then puts all cards revealed this way that weren’t put onto the battlefield on the bottom of their library in any order."
    ),
    Phenomenon(
        name="Mutual Epiphany",
        text="When you encounter Mutual Epiphany, each player draws four cards."
    ),
    Phenomenon(
        name="Planewide Disaster",
        text="When you encounter Planewide Disaster, destroy all creatures."
    ),
    Phenomenon(
        name="Reality Shaping",
        text="When you encounter Reality Shaping, starting with you, each player may put a permanent card from their hand onto the battlefield."
    ),
    Phenomenon(
        name="Spatial Merging",
        text="When you encounter Spatial Merging, reveal cards from the top of your planar deck until you reveal two plane cards. Simultaneously planeswalk to both of them. Put all other cards revealed this way on the bottom of your planar deck in any order."
    ),
    Phenomenon(
        name="Time Distortion",
        text="When you encounter Time Distortion, reverse the game’s turn order. (For example, if play had proceeded clockwise around the table, it now goes counterclockwise.)"
    ),
]

shuffle(deck)

planar_deck: Planechase = Planechase(
    deck=deck,
    length=len(deck),
    index=0,
)
