from enum import IntEnum, auto
from typing import Any, Final

from neurometa.fly import DrosophilaBrainStructure
from neurometa.human import HumanBrainStructure


class ModelAnimal(IntEnum):
    MUS_MUSCULUS = auto()
    RATTUS_NORVEGICUS = auto()
    MERIONES_UNGUICULATUS = auto()
    CAVIA_PORCELLUS = auto()
    MESOCRICETUS_AURATUS = auto()
    MACACA_MULATTA = auto()
    CALLITHRIX_JACCHUS = auto()
    FELIS_CATUS = auto()
    CANIS_LUPUS_FAMILIARIS = auto()
    MUSTELA_PUTORIUS_FURO = auto()
    SUS_SCROFA = auto()
    DANIO_RERIO = auto()
    ORYZIAS_LATIPES = auto()
    XENOPUS_LAEVIS = auto()
    AMBYSTOMA_MEXICANUM = auto()
    GALLUS_GALLUS_DOMESTICUS = auto()
    TAENIOPYGIA_GUTTATA = auto()
    DROSOPHILA_MELANOGASTER = auto()
    CAENORHABDITIS_ELEGANS = auto()
    APLYSIA_CALIFORNICA = auto()
    PROCAMBARUS_CLARKII = auto()


class CulturalModelAnimalName(IntEnum):
    MOUSE = auto()
    RAT = auto()
    GERBIL = auto()
    GUINEA_PIG = auto()
    GOLDEN_HAMSTER = auto()
    RHESUS_MACAQUE = auto()
    MARMOSET = auto()
    CAT = auto()
    DOG = auto()
    FERRET = auto()
    PIG = auto()
    ZEBRAFISH = auto()
    MEDAKA = auto()
    AFRICAN_CLAWED_FROG = auto()
    AXOLOTL = auto()
    CHICKEN = auto()
    ZEBRA_FINCH = auto()
    FRUIT_FLY = auto()
    NEMATODE_WORM = auto()
    SEA_SLUG = auto()
    CRAYFISH = auto()


ANIMAL_SPECIES_TO_BRAIN_STRUCTURE: Final[dict[ModelAnimal, Any]] = {
    ModelAnimal.MUS_MUSCULUS: HumanBrainStructure,
    ModelAnimal.RATTUS_NORVEGICUS: HumanBrainStructure,
    ModelAnimal.DROSOPHILA_MELANOGASTER: DrosophilaBrainStructure,
}


animal_species_to_cultural_name = {
    ModelAnimal.MUS_MUSCULUS: CulturalModelAnimalName.MOUSE,
    ModelAnimal.RATTUS_NORVEGICUS: CulturalModelAnimalName.RAT,
    ModelAnimal.MERIONES_UNGUICULATUS: CulturalModelAnimalName.GERBIL,
    ModelAnimal.CAVIA_PORCELLUS: CulturalModelAnimalName.GUINEA_PIG,
    ModelAnimal.MESOCRICETUS_AURATUS: CulturalModelAnimalName.GOLDEN_HAMSTER,
    ModelAnimal.MACACA_MULATTA: CulturalModelAnimalName.RHESUS_MACAQUE,
    ModelAnimal.CALLITHRIX_JACCHUS: CulturalModelAnimalName.MARMOSET,
    ModelAnimal.FELIS_CATUS: CulturalModelAnimalName.CAT,
    ModelAnimal.CANIS_LUPUS_FAMILIARIS: CulturalModelAnimalName.DOG,
    ModelAnimal.MUSTELA_PUTORIUS_FURO: CulturalModelAnimalName.FERRET,
    ModelAnimal.SUS_SCROFA: CulturalModelAnimalName.PIG,
    ModelAnimal.DANIO_RERIO: CulturalModelAnimalName.ZEBRAFISH,
    ModelAnimal.ORYZIAS_LATIPES: CulturalModelAnimalName.MEDAKA,
    ModelAnimal.XENOPUS_LAEVIS: CulturalModelAnimalName.AFRICAN_CLAWED_FROG,
    ModelAnimal.AMBYSTOMA_MEXICANUM: CulturalModelAnimalName.AXOLOTL,
    ModelAnimal.GALLUS_GALLUS_DOMESTICUS: CulturalModelAnimalName.CHICKEN,
    ModelAnimal.TAENIOPYGIA_GUTTATA: CulturalModelAnimalName.ZEBRA_FINCH,
    ModelAnimal.DROSOPHILA_MELANOGASTER: CulturalModelAnimalName.FRUIT_FLY,
    ModelAnimal.CAENORHABDITIS_ELEGANS: CulturalModelAnimalName.NEMATODE_WORM,
    ModelAnimal.APLYSIA_CALIFORNICA: CulturalModelAnimalName.SEA_SLUG,
    ModelAnimal.PROCAMBARUS_CLARKII: CulturalModelAnimalName.CRAYFISH,
}

cultural_name_to_animal_species = {v: k for k, v in animal_species_to_cultural_name.items()}
