from scry.api_processing.archenemy.decks import ArchenemyDeck
import scry.api_processing.archenemy.cards as c
from typing import Dict

BringAboutTheUndeadApocalypse: ArchenemyDeck = ArchenemyDeck(
    [
        c.ChooseYourChampion,
        c.ChooseYourChampion,
        c.DancePatheticMarionette,
        c.TheDeadShallServe,
        c.TheDeadShallServe,
        c.ADisplayOfMyDarkPower,
        c.EveryHopeShallVanish,
        c.EveryHopeShallVanish,
        c.IDelightInYourConvulsions,
        c.IntroductionsAreInOrder,
        c.MortalFleshIsWeak,
        c.MyUndeadHordeAwakens,
        c.OnlyBloodEndsYourNightmares,
        c.OnlyBloodEndsYourNightmares,
        c.RealmsBefittingMyMajesty,
        c.RottedOnesLaySiege,
        c.RottedOnesLaySiege,
        c.SurrenderYourThoughts,
        c.YourFateIsThriceSealed,
        c.YourPunyMindsCannotFathom,
    ]
)

AssembleTheDoomsdayMachine: ArchenemyDeck = ArchenemyDeck(
    [
        c.AllInGoodTime,
        c.BeholdThePowerOfDestruction,
        c.EmbraceMyDiabolicalVision,
        c.FeedTheMachine,
        c.FeedTheMachine,
        c.IDelightInYourConvulsions,
        c.IKnowAllISeeAll,
        c.IKnowAllISeeAll,
        c.IgniteTheCloneforge,
        c.IgniteTheCloneforge,
        c.IntroductionsAreInOrder,
        c.TheIronGuardianStirs,
        c.TheIronGuardianStirs,
        c.MyGeniusKnowsNoBounds,
        c.NothingCanStopMeNow,
        c.ThePiecesAreComingTogether,
        c.ThePiecesAreComingTogether,
        c.RealmsBefittingMyMajesty,
        c.YourFateIsThriceSealed,
        c.YourPunyMindsCannotFathom,
    ]
)

TrambleCivilizationUnderFoot: ArchenemyDeck = ArchenemyDeck(
    [
        c.EveryLastVestigeShallRot,
        c.EveryLastVestigeShallRot,
        c.EvilComesToFruition,
        c.ICallOnTheAncientMagics,
        c.IDelightInYourConvulsions,
        c.IntoTheEarthenMaw,
        c.IntroductionsAreInOrder,
        c.MayCivilizationCollapse,
        c.NatureDemandsAnOffering,
        c.NatureDemandsAnOffering,
        c.NatureShieldsItsOwn,
        c.NatureShieldsItsOwn,
        c.RealmsBefittingMyMajesty,
        c.RootsOfAllEvil,
        c.RootsOfAllEvil,
        c.TheVerySoilShallShake,
        c.YourFateIsThriceSealed,
        c.YourPunyMindsCannotFathom,
        c.YourWillIsNotYourOwn,
        c.YourWillIsNotYourOwn,
    ]
)

ScorchTheWorldWithDragonFire: ArchenemyDeck = ArchenemyDeck(
    [
        c.AllShallSmolderInMyWake,
        c.AllShallSmolderInMyWake,
        c.ApproachMyMoltenRealm,
        c.TheFateOfTheFlamable,
        c.IBaskInYourSilentAwe,
        c.IBaskInYourSilentAwe,
        c.IDelightInYourConvulsions,
        c.IntroductionsAreInOrder,
        c.KnowNaughtButFire,
        c.LooSkywardAndDespair,
        c.LooSkywardAndDespair,
        c.MyCrushingMasterstroke,
        c.MyWishIsYourCommand,
        c.MyWishIsYourCommand,
        c.RealmsBefittingMyMajesty,
        c.ToothClawAndTail,
        c.WhichOfYouBurnBrightest,
        c.WhichOfYouBurnBrightest,
        c.YourFateIsThriceSealed,
        c.YourPunyMindsCannotFathom,
    ]
)

Bolas: ArchenemyDeck = ArchenemyDeck(
    [
        c.BecauseIHaveWilledIt,
        c.BeholdMyGrandeur,
        c.BowToMyCommand,
        c.ChooseYourDemise,
        c.DelightInTheHunt,
        c.EveryDreamaNightmare,
        c.ForEachOfYouAGift,
        c.KnowEvil,
        c.MakeYourselfUseful,
        c.TheMightyWillFall,
        c.MyForcesAreInnumerable,
        c.MyLaughterEchoes,
        c.NoOneWillHearYourCries,
        c.PayTributeToMe,
        c.PowerWithoutEqual,
        c.AReckoningApproaches,
        c.ThereIsNoRefuge,
        c.ThisWorldBelongsToMe,
        c.WhatsYoursIsNowMine,
        c.WhenWillYouLearn,
    ]
)

archenemy_decks: Dict[str, ArchenemyDeck] = {
    "apocalypse": BringAboutTheUndeadApocalypse,
    "doomsday": AssembleTheDoomsdayMachine,
    "tramble": TrambleCivilizationUnderFoot,
    "dragonfire": ScorchTheWorldWithDragonFire,
    "bolas": Bolas,
}
