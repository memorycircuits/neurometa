from enum import Enum
from typing import Annotated, Final, TypeAlias

from pydantic import AfterValidator

from neurometa.fly import DrosophilaBrainStructure
from neurometa.human import HumanBrainStructure


def validate_brain_structure_enum(value: str):
    if all(value not in bse for bse in (HumanBrainStructure, DrosophilaBrainStructure)):
        raise ValueError(f"Brain structure {value} is not a valid brain structure.")
    return value


BrainStructure: TypeAlias = Annotated[str, AfterValidator(validate_brain_structure_enum)]


class Neurotransmitter(Enum):
    ACETYLCHOLINE = "acetylcholine"
    ADENOSINE = "adenosine"
    ADENOSINE_TRIPHOSPHATE = "adenosine triphosphate"
    ADRENOCORTICOTROPIC_HORMONE = "adrenocorticotropic hormone"
    AGOUTI_RELATED_PEPTIDE = "agouti related peptide"
    ANANDAMIDE = "anandamide"
    ARACHIDONOYLGLYCEROL = "arachidonoylglycerol"
    ARACHIDONOYLGLYCEROL_2 = "arachidonoylglycerol 2"
    ARACHIDONYL_GLYCERYL_ETHER = "arachidonyl glyceryl ether"
    ARACHIDONYL_GLYCERYL_ETHER_2 = "arachidonyl glyceryl ether 2"
    ARGININE = "arginine"
    ASPARTATE = "aspartate"
    BOMBESIN = "bombesin"
    BRADYKININ = "bradykinin"
    CALCITONIN = "calcitonin"
    CALCITONIN_GENE_RELATED_PEPTIDE = "calcitonin gene related peptide"
    CARBON_MONOXIDE = "carbon monoxide"
    CHOLECYSTOKININ = "cholecystokinin"
    CHROMOGRANIN_A = "chromogranin a"
    COCAINE_AND_AMPHETAMINE_REGULATED_TRANSCRIPT = "cocaine and amphetamine regulated transcript"
    COPEPTIN = "copeptin"
    CORTICOTROPIN_RELEASING_HORMONE = "corticotropin releasing hormone"
    DOPAMINE = "dopamine"
    DYNORPHINS = "dynorphins"
    D_SERINE = "d serine"
    ENDOMORPHINS = "endomorphins"
    ENDORPHINS = "endorphins"
    ENKEPHALINS = "enkephalins"
    EPINEPHRINE = "epinephrine"
    GALANIN = "galanin"
    GALANIN_LIKE_PEPTIDE = "galanin like peptide"
    GAMMA_AMINOBUTYRIC_ACID = "gamma aminobutyric acid"
    GASTRIN = "gastrin"
    GASTRIN_RELEASING_PEPTIDE = "gastrin releasing peptide"
    GLUCAGON = "glucagon"
    GLUCAGON_LIKE_PEPTIDE_1 = "glucagon like peptide 1"
    GLUCAGON_LIKE_PEPTIDE_2 = "glucagon like peptide 2"
    GLUTAMATE = "glutamate"
    GLYCINE = "glycine"
    GONADOTROPIN_RELEASING_HORMONE = "gonadotropin releasing hormone"
    GROWTH_HORMONE_INHIBITING_HORMONE = "growth hormone inhibiting hormone"
    GROWTH_HORMONE_RELEASING_HORMONE = "growth hormone releasing hormone"
    GUANOSINE = "guanosine"
    HISTAMINE = "histamine"
    HYDROGEN_SULFIDE = "hydrogen sulfide"
    INOSINE = "inosine"
    KISSPEPTIN = "kisspeptin"
    MELANIN_CONCENTRATING_HORMONE = "melanin concentrating hormone"
    MELANOCYTE_STIMULATING_HORMONES = "melanocyte stimulating hormones"
    MORPHINE = "morphine"
    MOTILIN = "motilin"
    NEOENDORPHINS = "neoendorphins"
    NEUROKININ_A = "neurokinin a"
    NEUROKININ_B = "neurokinin b"
    NEUROMEDIN_B = "neuromedin b"
    NEUROMEDIN_U = "neuromedin u"
    NEUROPEPTIDE_B = "neuropeptide b"
    NEUROPEPTIDE_FF = "neuropeptide ff"
    NEUROPEPTIDE_K = "neuropeptide k"
    NEUROPEPTIDE_S = "neuropeptide s"
    NEUROPEPTIDE_Y = "neuropeptide y"
    NEUROPHYSIN_I = "neurophysin i"
    NEUROPHYSIN_II = "neurophysin ii"
    NICOTINAMIDE_ADENINE_DINUCLEOTIDE = "nicotinamide adenine dinucleotide"
    NITRIC_OXIDE = "nitric oxide"
    NOCICEPTIN_ORPHANIN_FQ = "nociceptin orphanin fq"
    NOREPINEPHRINE = "norepinephrine"
    N_ACETYLASPARTYLGLUTAMATE = "n acetylaspartylglutamate"
    N_ARACHIDONOYL_DOPAMINE = "n arachidonoyl dopamine"
    N_METHYLPHENETHYLAMINE = "n methylphenethylamine"
    N_METHYLTRYPTAMINE = "n methyltryptamine"
    OCTOPAMINE = "octopamine"
    OREXIN_A = "orexin a"
    OREXIN_B = "orexin b"
    OXYTOCIN = "oxytocin"
    PANCREATIC_POLYPEPTIDE = "pancreatic polypeptide"
    PARATHYROID_HORMONE_RELATED_PROTEIN = "parathyroid hormone related protein"
    PEPTIDE_YY = "peptide yy"
    PHENETHYLAMINE = "phenethylamine"
    PITUITARY_ADENYLATE_CYCLASE_ACTIVATING_PEPTIDE = "pituitary adenylate cyclase activating peptide"
    PROLACTIN_RELEASING_PEPTIDE = "prolactin releasing peptide"
    PROOPIOMELANOCORTIN = "proopiomelanocortin"
    PYROGLUTAMYLATED_RFAMIDE_PEPTIDE = "pyroglutamylated rfamide peptide"
    SECRETIN = "secretin"
    SEROTONIN = "serotonin"
    SOMATOSTATIN = "somatostatin"
    SUBSTANCE_P = "substance p"
    SYNEPHRINE = "synephrine"
    THYROTROPIN_RELEASING_HORMONE = "thyrotropin releasing hormone"
    TRYPTAMINE = "tryptamine"
    TYRAMINE = "tyramine"
    URIDINE = "uridine"
    UROCORTIN = "urocortin"
    VASOACTIVE_INTESTINAL_PEPTIDE = "vasoactive intestinal peptide"
    VASOPRESSIN = "vasopressin"
    VIRODHAMINE = "virodhamine"


NEUROTRANSMITTER_ALIAS_MAP: Final[dict] = {
    "arginine": Neurotransmitter.ARGININE,
    "arg": Neurotransmitter.ARGININE,
    "r": Neurotransmitter.ARGININE,
    "aspartate": Neurotransmitter.ASPARTATE,
    "asp": Neurotransmitter.ASPARTATE,
    "d": Neurotransmitter.ASPARTATE,
    "glutamate": Neurotransmitter.GLUTAMATE,
    "glu": Neurotransmitter.GLUTAMATE,
    "glut": Neurotransmitter.GLUTAMATE,
    "e": Neurotransmitter.GLUTAMATE,
    "gamma-aminobutyric acid": Neurotransmitter.GAMMA_AMINOBUTYRIC_ACID,
    "gaba": Neurotransmitter.GAMMA_AMINOBUTYRIC_ACID,
    "glycine": Neurotransmitter.GLYCINE,
    "gly": Neurotransmitter.GLYCINE,
    "g": Neurotransmitter.GLYCINE,
    "d-serine": Neurotransmitter.D_SERINE,
    "ser": Neurotransmitter.D_SERINE,
    "s": Neurotransmitter.D_SERINE,
    "acetylcholine": Neurotransmitter.ACETYLCHOLINE,
    "ach": Neurotransmitter.ACETYLCHOLINE,
    "dopamine": Neurotransmitter.DOPAMINE,
    "da": Neurotransmitter.DOPAMINE,
    "norepinephrine": Neurotransmitter.NOREPINEPHRINE,
    "noradrenaline": Neurotransmitter.NOREPINEPHRINE,
    "ne": Neurotransmitter.NOREPINEPHRINE,
    "nad": Neurotransmitter.NOREPINEPHRINE,
    "na": Neurotransmitter.NOREPINEPHRINE,
    "epinephrine": Neurotransmitter.EPINEPHRINE,
    "adrenaline": Neurotransmitter.EPINEPHRINE,
    "epi": Neurotransmitter.EPINEPHRINE,
    "ad": Neurotransmitter.EPINEPHRINE,
    "serotonin": Neurotransmitter.SEROTONIN,
    "5-ht": Neurotransmitter.SEROTONIN,
    "5-hydroxytryptamine": Neurotransmitter.SEROTONIN,
    "histamine": Neurotransmitter.HISTAMINE,
    "h": Neurotransmitter.HISTAMINE,
    "phenethylamine": Neurotransmitter.PHENETHYLAMINE,
    "pea": Neurotransmitter.PHENETHYLAMINE,
    "n-methylphenethylamine": Neurotransmitter.N_METHYLPHENETHYLAMINE,
    "nmpea": Neurotransmitter.N_METHYLPHENETHYLAMINE,
    "tyramine": Neurotransmitter.TYRAMINE,
    "tyr": Neurotransmitter.TYRAMINE,
    "octopamine": Neurotransmitter.OCTOPAMINE,
    "oct": Neurotransmitter.OCTOPAMINE,
    "synephrine": Neurotransmitter.SYNEPHRINE,
    "syn": Neurotransmitter.SYNEPHRINE,
    "tryptamine": Neurotransmitter.TRYPTAMINE,
    "n-methyltryptamine": Neurotransmitter.N_METHYLTRYPTAMINE,
    "nmt": Neurotransmitter.N_METHYLTRYPTAMINE,
    "anandamide": Neurotransmitter.ANANDAMIDE,
    "aea": Neurotransmitter.ANANDAMIDE,
    "2-arachidonoylglycerol": Neurotransmitter.ARACHIDONOYLGLYCEROL_2,
    "2-ag": Neurotransmitter.ARACHIDONOYLGLYCEROL_2,
    "2-arachidonyl glyceryl ether": Neurotransmitter.ARACHIDONYL_GLYCERYL_ETHER_2,
    "2-age": Neurotransmitter.ARACHIDONYL_GLYCERYL_ETHER_2,
    "n-arachidonoyl dopamine": Neurotransmitter.N_ARACHIDONOYL_DOPAMINE,
    "nada": Neurotransmitter.N_ARACHIDONOYL_DOPAMINE,
    "virodhamine": Neurotransmitter.VIRODHAMINE,
    "adenosine": Neurotransmitter.ADENOSINE,
    "ado": Neurotransmitter.ADENOSINE,
    "guanosine": Neurotransmitter.GUANOSINE,
    "guo": Neurotransmitter.GUANOSINE,
    "uridine": Neurotransmitter.URIDINE,
    "uro": Neurotransmitter.URIDINE,
    "inosine": Neurotransmitter.INOSINE,
    "ino": Neurotransmitter.INOSINE,
    "nitric oxide": Neurotransmitter.NITRIC_OXIDE,
    "no": Neurotransmitter.NITRIC_OXIDE,
    "carbon monoxide": Neurotransmitter.CARBON_MONOXIDE,
    "co": Neurotransmitter.CARBON_MONOXIDE,
    "hydrogen sulfide": Neurotransmitter.HYDROGEN_SULFIDE,
    "h2s": Neurotransmitter.HYDROGEN_SULFIDE,
}


class NeuroanatomicalDirection(Enum):
    ANTERIOR = "anterior"
    ANTERIOR_DORSAL = "anterior dorsal"
    ANTERIOR_VENTRAL = "anterior ventral"
    CAUDAL = "caudal"
    DISTAL = "distal"
    DISTAL_CAUDAL = "distal caudal"
    DISTAL_ROSTRAL = "distal rostral"
    DORSAL = "dorsal"
    DORSAL_LATERAL = "dorsal lateral"
    DORSAL_MEDIAL = "dorsal medial"
    INFERIOR = "inferior"
    INFERIOR_DISTAL = "inferior distal"
    INFERIOR_PROXIMAL = "inferior proximal"
    LATERAL = "lateral"
    LATERAL_INFERIOR = "lateral inferior"
    LATERAL_SUPERIOR = "lateral superior"
    MEDIAL = "medial"
    MEDIAL_INFERIOR = "medial inferior"
    MEDIAL_SUPERIOR = "medial superior"
    POSTERIOR = "posterior"
    POSTERIOR_DORSAL = "posterior dorsal"
    POSTERIOR_VENTRAL = "posterior ventral"
    PROXIMAL = "proximal"
    PROXIMAL_CAUDAL = "proximal caudal"
    PROXIMAL_ROSTRAL = "proximal rostral"
    ROSTRAL = "rostral"
    SUPERIOR = "superior"
    SUPERIOR_DISTAL = "superior distal"
    SUPERIOR_PROXIMAL = "superior proximal"
    VENTRAL = "ventral"
    VENTRAL_LATERAL = "ventral lateral"
    VENTRAL_MEDIAL = "ventral medial"
    NULL = "null"


class GeneExpression(Enum):
    KNOCK_OUT = "knock-out"
    KNOCK_IN = "knock-in"
    KNOCK_DOWN = "knock-down"
    KNOCK_SIDEWAYS = "knock-sideways"
    OVEREXPRESSION = "overexpression"


class NeuronPolarity(Enum):
    UNIPOLAR = "unipolar"  # Neurons with a single process
    BIPOLAR = "bipolar"  # Neurons with two processes (one axon, one dendrite)
    ANAXONIC = "anaxonic"  # Neurons without a clear axon
    PSEUDOUNIPOLAR = "pseudounipolar"  # Neurons with a single process that divides into two branches
    MULTIPOLAR = "multipolar"  # Neurons with one axon and multiple dendrites


class NeuronType(Enum):
    BASKET = "basket"  # Inhibitory interneurons in the brain
    BETZ = "betz"  # Large pyramidal neurons in the primary motor cortex
    LUGARO = "lugaro"  # Neurons in the cerebellar cortex
    MEDIUM_SPINY = "medium spiny"  # Principal neurons of the striatum
    PURKINJE = "purkinje"  # Large neurons in the cerebellar cortex
    PYRAMIDAL = "pyramidal"  # Neurons with pyramid-shaped cell bodies in the cerebral cortex
    RENSHAW = "renshaw"  # Interneurons in the spinal cord
    UNIPOLAR_BRUSH = "unipolar brush"  # Neurons found in the cerebellum
    GRANULE = "granule"  # Small neurons in the cerebellum and olfactory bulb
    MOTOR = "motor"  # Neurons that send impulses to muscles
    SPINDLE = "spindle"  # Sensory neurons in muscles
    FAN = "fan"  # A type of neuron (need more specific context)
    STELLATE = "stellate"  # Star-shaped interneurons in the cerebral cortex
    CHANDELIER = "chandelier"  # A type of inhibitory interneuron in the cerebral cortex
    GOLGI = "golgi"  # Inhibitory interneurons in the cerebellum
    MARTINOTTI = "martinotti"  # Interneurons found throughout the cerebral cortex
    CAJAL_RETZIUS = "cajal_retzius"  # Early-developing neurons in the marginal zone of the cortex
