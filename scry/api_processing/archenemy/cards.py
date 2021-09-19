from scry.api_processing.archenemy.scheme import Scheme

AllInGoodTime: Scheme = Scheme(
    name="All in Good Time",
    text="When you set this scheme in motion, take an extra turn after this one. Schemes can't be set in motion that turn.",
    lore="Take a moment. Ponder the depths of your insignificance.",
)

BeholdThePowerOfDestruction: Scheme = Scheme(
    name="Behold the Power of Destruction",
    text="When you set this scheme in motion, destroy all nonland permanents target opponent controls.",
    lore="I’d call that a successful first test. Golem! Rearm the Doom Citadel!",
)

EmbraceMyDiabolicalVision: Scheme = Scheme(
    name="Embrace My Diabolical Vision",
    text="When you set this scheme in motion, each player shuffles their hand and graveyard into their library. You draw seven cards, then each other player draws four cards.",
    lore="My vision is for the good of everyone. Mostly me.",
)

FeedTheMachine: Scheme = Scheme(
    name="Feed the Machine",
    text="When you set this scheme in motion, target opponent chooses self or others. If that player chooses self, the player sacrifices two creatures. If the player chooses others, each of your other opponents sacrifices a creature.",
    lore="Even you have a purpose. Your blood will oil the gears.",
)

IDelightInYourConvulsions: Scheme = Scheme(
    name="I Delight in Your Convulsions",
    text="When you set this scheme in motion, each opponent loses 3 life. You gain life equal to the life lost this way.",
    lore="I can’t imagine what you’re feeling right now, but I’ll try my best.",
)

IKnowAllISeeAll: Scheme = Scheme(
    is_ongoing=True,
    name="I Know All, I See All",
    text="Untap all permanents you control during each opponent’s untap step.",
    abandon="At the beginning of each end step, if three or more cards were put into your graveyard this turn from anywhere, abandon this scheme.",
)

IgniteTheCloneforge: Scheme = Scheme(
    name="Ignite the Cloneforge!",
    text="When you set this scheme in motion, create a token that’s a copy of target permanent an opponent controls.",
    lore="Heroes innovate. Villains duplicate.",
)

IntroductionsAreInOrder: Scheme = Scheme(
    name="Introductions Are in Order",
    text="""When you set this scheme in motion, choose one —

• Search your library for a creature card, reveal it, put it into your hand, then shuffle.

• You may put a creature card from your hand onto the battlefield.""",
    lore="Meet my newest minion. Come now, don’t be shy—shake her pincer.",
)

TheIronGuardianStirs: Scheme = Scheme(
    name="The Iron Guardian Stirs",
    text="When you set this scheme in motion, create a 4/6 colorless Golem artifact creature token.",
    lore="It would be disappointing if you were unable to overcome this simplest of defenses. Hilarious, but disappointing.",
)

MyGeniusKnowsNoBounds: Scheme = Scheme(
    name="My Genius Knows No Bounds",
    text="When you set this scheme in motion, you may pay (X). If you do, you gain X life and draw X cards.",
    lore="I can see … everything. The beginning and the end of time. The raw edges of reality. And now I see exactly how to kill you.",
)

NothingCanStopMeNow: Scheme = Scheme(
    is_ongoing=True,
    name="Nothing Can Stop Me Now",
    text="If a source an opponent controls would deal damage to you, prevent 1 of that damage.",
    abandon="At the beginning of each end step, if you’ve been dealt 5 or more damage this turn, abandon this scheme.",
)

ThePiecesAreComingTogether: Scheme = Scheme(
    name="The Pieces Are Coming Together",
    text="When you set this scheme in motion, draw two cards. Artifact spells you cast this turn cost (2) less to cast.",
    lore="Cretins build machines. I construct destiny.",
)

RealmsBefittingMyMajesty: Scheme = Scheme(
    name="Realms Befitting My Majesty",
    text="When you set this scheme in motion, search your library for up to two basic land cards, put them onto the battlefield tapped, then shuffle.",
    lore="Look around you. All you behold is mine to rule. It’s the natural way.",
)

YourFateIsThriceSealed: Scheme = Scheme(
    name="Your Fate Is Thrice Sealed",
    text="When you set this scheme in motion, reveal the top three cards of your library. Put all land cards revealed this way onto the battlefield and the rest into your hand.",
    lore="I can’t abide laziness. Arise, forces of nature, and serve your master!",
)

YourPunyMindsCannotFathom: Scheme = Scheme(
    name="Your Puny Minds Cannot Fathom",
    text="When you set this scheme in motion, draw four cards. You have no maximum hand size until your next turn.",
    lore="I have seen far beyond this imperfect world, into a tomorrow that doesn’t include you.",
)

ADisplayOfMyDarkPower: Scheme = Scheme(
    name="A Display of My Dark Power",
    text="When you set this scheme in motion, until your next turn, whenever a player taps a land for mana, that player adds one mana of any type that land produced.",
    lore="What would you say is my greatest attribute? Is it my gluttonous lust for power?",
)

AllShallSmolderInMyWake: Scheme = Scheme(
    name="All Shall Smolder in My Wake",
    text="When you set this scheme in motion, destroy up to one target artifact, up to one target enchantment, and up to one target nonbasic land.",
    lore="It’s my goal to find the melting point of every substance.",
)

ApproachMyMoltenRealm: Scheme = Scheme(
    name="Approach My Molten Realm",
    text="When you set this scheme in motion, until your next turn, if a source would deal damage, it deals double that damage instead.",
    lore="It’s a dragon-infested lavascape of notorious peril. Make yourselves at home.",
)

ChooseYourChampion: Scheme = Scheme(
    name="Choose Your Champion",
    text="When you set this scheme in motion, target opponent chooses a player. Until your next turn, only you and the chosen player can cast spells and attack with creatures.",
    lore="It seems the fate of the world rests on your shoulders, feeble child.",
)

DancePatheticMarionette: Scheme = Scheme(
    name="Dance, Pathetic Marionette",
    text="When you set this scheme in motion, each opponent reveals cards from the top of their library until they reveal a creature card. Choose one of the revealed creature cards and put it onto the battlefield under your control. Put all other cards revealed this way into their owners’ graveyards.",
)

EveryHopeShallVanish: Scheme = Scheme(
    name="Every Hope Shall Vanish",
    text="When you set this scheme in motion, each opponent reveals their hand. Choose a nonland card from each of those hands. Those players discard those cards.",
    lore="Oh, I think I will get away with this.",
)

EveryLastVestigeShallRot: Scheme = Scheme(
    name="Every Last Vestige Shall Rot",
    text="When you set this scheme in motion, you may pay (X). If you do, put each nonland permanent target player controls with mana value X or less on the bottom of its owner’s library.",
    lore="May bloodberries grow from your remains.",
)

EvilComesToFruition: Scheme = Scheme(
    name="Evil Comes to Fruition",
    text="When you set this scheme in motion, create seven 0/1 green Plant creature tokens. If you control ten or more lands, create seven 3/3 green Elemental creature tokens instead.",
    lore="The plants justify the means.",
)

IBaskInYourSilentAwe: Scheme = Scheme(
    is_ongoing=True,
    name="I Bask in Your Silent Awe",
    text="Each opponent can’t cast more than one spell each turn.",
    abandon="At the beginning of your upkeep, if no opponent cast a spell since your last turn ended, abandon this scheme.",
)

ICallOnTheAncientMagics: Scheme = Scheme(
    name="I Call on the Ancient Magics",
    text="When you set this scheme in motion, each other player searches their library for a card, reveals it, and puts it into their hand. Then you search your library for two cards and put them into your hand. Each player shuffles.",
)

IntoTheEarthenMaw: Scheme = Scheme(
    name="Into the Earthen Maw",
    text="When you set this scheme in motion, exile up to one target creature with flying, up to one target creature without flying, and all cards from up to one target opponent’s graveyard.",
    lore="You may even see them again. Full digestion takes three hundred years.",
)

KnowNaughtButFire: Scheme = Scheme(
    name="Know Naught but Fire",
    text="When you set this scheme in motion, it deals damage to each opponent equal to the number of cards in that player’s hand.",
    lore="Cranial explosions for everyone. Still planning to outthink my dragons?",
)

LooSkywardAndDespair: Scheme = Scheme(
    name="Look Skyward and Despair",
    text="When you set this scheme in motion, create a 5/5 red Dragon creature token with flying.",
    lore="Today I take the reins of destiny itself. Today the Draconic Apocalypse is upon you.",
)

MayCivilizationCollapse: Scheme = Scheme(
    name="May Civilization Collapse",
    text="When you set this scheme in motion, target opponent chooses self or others. If that player chooses self, that player sacrifices two lands. If the player chooses others, each of your other opponents sacrifices a land.",
    lore="This should halt the spread of your insolence.",
)

MortalFleshIsWeak: Scheme = Scheme(
    name="Mortal Flesh Is Weak",
    text="When you set this scheme in motion, each opponent’s life total becomes the lowest life total among your opponents.",
    lore="I certainly would have accepted my offer of eternal life. But if you choose death instead, who am I to argue?",
)

MyCrushingMasterstroke: Scheme = Scheme(
    name="My Crushing Masterstroke",
    text="When you set this scheme in motion, gain control of all nonland permanents your opponents control until end of turn. Untap those permanents. They gain haste until end of turn. Each of them attacks its owner this turn if able.",
)

MyUndeadHordeAwakens: Scheme = Scheme(
    is_ongoing=True,
    name="My Undead Horde Awakens",
    text="At the beginning of your end step, you may put target creature card from an opponent’s graveyard onto the battlefield under your control.",
    abandon="When a creature put onto the battlefield with this scheme dies, abandon this scheme.",
)

MyWishIsYourCommand: Scheme = Scheme(
    name="My Wish Is Your Command",
    text="When you set this scheme in motion, each opponent reveals their hand. You may choose a noncreature, nonland card revealed this way and cast it without paying its mana cost.",
    lore="Indulge me. Just one spell. One potentially fatal spell gone horribly awry.",
)

NatureDemandsAnOffering: Scheme = Scheme(
    name="Nature Demands an Offering ",
    text="When you set this scheme in motion, target opponent chooses a creature you don’t control and puts it on top of its owner’s library, then repeats this process for an artifact, an enchantment, and a land. Then the owner of each permanent chosen this way shuffles.",
)

NatureShieldsItsOwn: Scheme = Scheme(
    is_ongoing=True,
    name="Nature Shields Its Own",
    text="Whenever a creature attacks and isn’t blocked, if you’re the defending player, create a 0/1 green Plant creature token that’s blocking that creature.",
    abandon="When four or more creatures attack you, abandon this scheme at end of combat.",
)

OnlyBloodEndsYourNightmares: Scheme = Scheme(
    name="Only Blood Ends Your Nightmares",
    text="When you set this scheme in motion, each opponent sacrifices a creature. Then each opponent who didn’t sacrifice a creature discards two cards.",
    lore="But nothing will end your regret.",
)

RootsOfAllEvil: Scheme = Scheme(
    name="Roots of All Evil",
    text="When you set this scheme in motion, create five 1/1 green Saproling creature tokens.",
    lore="I assure you, these are not the kind that thrive on sunlight and water.",
)

RottedOnesLaySiege: Scheme = Scheme(
    name="Rotted Ones, Lay Siege",
    text="When you set this scheme in motion, for each opponent, create a 2/2 black Zombie creature token that attacks that player each combat if able.",
    lore="Don’t come back until you’ve got brains in your teeth.",
)

SurrenderYourThoughts: Scheme = Scheme(
    name="Surrender Your Thoughts",
    text="When you set this scheme in motion, target opponent chooses self or others. If that player chooses self, that player discards four cards. If the player chooses others, each of your other opponents discards two cards.",
    lore="Or, if you prefer, just surrender.",
)

TheDeadShallServe: Scheme = Scheme(
    name="The Dead Shall Serve",
    text="When you set this scheme in motion, for each opponent, put up to one target creature card from that player’s graveyard onto the battlefield under your control. Each of those creatures attacks its owner each combat if able.",
    lore="Tell your old master I said hello.",
)

TheFateOfTheFlamable: Scheme = Scheme(
    name="The Fate of the Flammable",
    text="When you set this scheme in motion, target opponent chooses self or others. If that player chooses self, this scheme deals 6 damage to that player. If the player chooses others, this scheme deals 3 damage to each of your other opponents.",
)

TheVerySoilShallShake: Scheme = Scheme(
    is_ongoing=True,
    name="The Very Soil Shall Shake",
    text="Creatures you control get +2/+2 and have trample.",
    abandon="When a creature you control dies, abandon this scheme.",
)

ToothClawAndTail: Scheme = Scheme(
    name="Tooth, Claw, and Tail",
    text="When you set this scheme in motion, destroy up to three target nonland permanents.",
    lore="Silence your wailing. This is but a taste of the destruction my pets have in store.",
)

WhichOfYouBurnBrightest: Scheme = Scheme(
    name="Which of You Burns Brightest?",
    text="When you set this scheme in motion, you may pay (X). If you do, this scheme deals X damage to target opponent or planeswalker and each creature that player or that planeswalker’s controller controls.",
    lore="Let that be a lesson to you, your family, and everyone you’ve ever known.",
)

YourWillIsNotYourOwn: Scheme = Scheme(
    name="Your Will Is Not Your Own",
    text="When you set this scheme in motion, gain control of target creature an opponent controls until end of turn. Untap that creature. It gets +3/+3 and gains trample and haste until end of turn.",
    lore="Fool. I’ll show you how to use that thing.",
)

BecauseIHaveWilledIt: Scheme = Scheme(
    is_ongoing=True,
    name="Because I Have Willed It",
    text="Spells you cast cost (1) less to cast.",
    abandon="At the beginning of your opponents’ end step, if they cast four or more spells this turn, abandon this scheme.",
)

BeholdMyGrandeur: Scheme = Scheme(
    name="Behold My Grandeur",
    text="""When you set this scheme in motion, add 💧💀🔥.

When you set this scheme in motion, if you control six or more lands, you may search your library for a card with mana value 6 or greater, reveal it, put it into your hand, then shuffle.""",
)

BowToMyCommand: Scheme = Scheme(
    is_ongoing=True,
    name="Bow to My Command",
    text="""As you set this scheme in motion, choose an opponent.

Creatures the chosen player controls can’t attack you or planeswalkers you control.""",
    abandon="At the beginning of your opponents’ end step, they may tap any number of untapped creatures they control with total power 7 or greater. If they do, abandon this scheme.",
)

ChooseYourDemise: Scheme = Scheme(
    name="Choose Your Demise",
    text="When you set this scheme in motion, look at the top four cards of your library and separate them into a face-down pile and a face-up pile. An opponent chooses one of those piles. Put the cards in that pile into your hand and the rest on the bottom of your library in any order.",
)

DelightInTheHunt: Scheme = Scheme(
    name="Delight in the Hunt",
    text="When you set this scheme in motion, create a 3/3 black Horror creature token and prevent all damage that would be dealt to creatures you control this turn.",
    lore="Pain is a delusion of the weak. I’ll demonstrate.",
)

EveryDreamaNightmare: Scheme = Scheme(
    name="Every Dream a Nightmare",
    text="When you set this scheme in motion, each opponent discards a card. You draw a card for each land card discarded this way.",
    lore="Let me unburden you of these fatuous hopes.",
)

ForEachOfYouAGift: Scheme = Scheme(
    name="For Each of You, a Gift",
    text="When you set this scheme in motion, for each opponent, create a 3/3 black Horror creature token that attacks that player each combat if able.",
    lore="My generosity blesses you all, even the undeserving.",
)

KnowEvil: Scheme = Scheme(
    name="Know Evil",
    text="When you set this scheme in motion, until your next turn, up to one target opponent can’t attack with creatures, up to one target opponent can’t cast creature spells, and up to one target opponent can’t cast noncreature spells. You can’t choose any player as a target more than once.",
)

MakeYourselfUseful: Scheme = Scheme(
    name="Make Yourself Useful",
    text="When you set this scheme in motion, destroy target creature an opponent controls. If a creature is destroyed this way, you gain life equal to its toughness.",
    lore="To think you’ve spent years honing your body only to die like this.",
)

TheMightyWillFall: Scheme = Scheme(
    name="The Mighty Will Fall",
    text="When you set this scheme in motion, choose an opponent with the highest life total among your opponents. That player loses 7 life.",
    lore="Cry out for your comrades so that they may join you in misery.",
)

MyForcesAreInnumerable: Scheme = Scheme(
    is_ongoing=True,
    name="My Forces Are Innumerable",
    text="At the beginning of your end step, create a 3/3 black Horror creature token.",
    abandon="At the beginning of your opponents’ end step, they may sacrifice two creatures. If they do, abandon this scheme.",
)

MyLaughterEchoes: Scheme = Scheme(
    is_ongoing=True,
    name="My Laughter Echoes",
    text="Whenever you set a non-ongoing scheme in motion, you may abandon this scheme. If you do, set that scheme in motion again.",
    lore="Groveling already? I’m just starting to enjoy myself.",
)

NoOneWillHearYourCries: Scheme = Scheme(
    name="No One Will Hear Your Cries",
    text="When you set this scheme in motion, each opponent chooses a creature they control, then sacrifices the rest.",
    lore="Your companions were lucky to have died first.",
)

PayTributeToMe: Scheme = Scheme(
    name="Pay Tribute to Me",
    text="When you set this scheme in motion, each opponent sacrifices a creature. If you control six or more lands, each opponent sacrifices another creature.",
)

PowerWithoutEqual: Scheme = Scheme(
    name="Power Without Equal",
    text="When you set this scheme in motion, draw three cards. You have no maximum hand size until your next turn. If you control six or more lands, you may cast up to three spells from your hand without paying their mana costs.",
)

AReckoningApproaches: Scheme = Scheme(
    name="A Reckoning Approaches",
    text="When you set this scheme in motion, look at the top six cards of your library. You may put a creature card from among them onto the battlefield. Put the rest on the bottom of your library in any order.",
    lore="The gates open to my new era.",
)

ThereIsNoRefuge: Scheme = Scheme(
    name="There Is No Refuge",
    text="When you set this scheme in motion, it deals 3 damage to up to one target creature. Create a 3/3 black Horror creature token.",
    lore="The dunes smell spilled blood.",
)

ThisWorldBelongsToMe: Scheme = Scheme(
    name="This World Belongs to Me",
    text="When you set this scheme in motion, draw two cards. You may play an additional land this turn.",
    lore="Little insects, I have created entire worlds and extinguished twice as many.",
)

WhatsYoursIsNowMine: Scheme = Scheme(
    name="What's Yours Is Now Mine",
    text="When you set this scheme in motion, gain control of target creature an opponent controls and untap it.",
    lore="Vow your allegiance to true power.",
)

WhenWillYouLearn: Scheme = Scheme(
    name="When Will You Learn?",
    text="When you set this scheme in motion, each opponent exiles the top card of their library. You may cast any number of spells from among cards exiled this way without paying their mana costs.",
    lore="Don’t fret, infants. It wouldn’t have worked anyway.",
)
