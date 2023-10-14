from enum import Enum, auto


class Neurotransmitter(Enum):
    ARGININE = auto()
    ASPARTATE = auto()
    GLUTAMATE = auto()
    GAMMA_AMINOBUTYRIC_ACID = auto()
    GLYCINE = auto()
    D_SERINE = auto()
    ACETYLCHOLINE = auto()
    DOPAMINE = auto()
    NOREPINEPHRINE = auto()
    EPINEPHRINE = auto()
    SEROTONIN = auto()
    HISTAMINE = auto()
    PHENETHYLAMINE = auto()
    N_METHYLPHENETHYLAMINE = auto()
    TYRAMINE = auto()
    OCTOPAMINE = auto()
    SYNEPHRINE = auto()
    TRYPTAMINE = auto()
    N_METHYLTRYPTAMINE = auto()
    ANANDAMIDE = auto()
    ARACHIDONOYLGLYCEROL = auto()
    ARACHIDONYL_GLYCERYL_ETHER = auto()
    N_ARACHIDONOYL_DOPAMINE = auto()
    VIRODHAMINE = auto()
    ADENOSINE = auto()
    ADENOSINE_TRIPHOSPHATE = auto()
    NICOTINAMIDE_ADENINE_DINUCLEOTIDE = auto()
    BOMBESIN = auto()
    GASTRIN_RELEASING_PEPTIDE = auto()
    NEUROMEDIN_B = auto()
    BRADYKININ = auto()
    CALCITONIN = auto()
    CALCITONIN_GENE_RELATED_PEPTIDE = auto()
    CORTICOTROPIN_RELEASING_HORMONE = auto()
    UROCORTIN = auto()
    GALANIN = auto()
    GALANIN_LIKE_PEPTIDE = auto()
    GASTRIN = auto()
    CHOLECYSTOKININ = auto()
    CHROMOGRANIN_A = auto()
    ADRENOCORTICOTROPIC_HORMONE = auto()
    PROOPIOMELANOCORTIN = auto()
    MELANOCYTE_STIMULATING_HORMONES = auto()
    VASOPRESSIN = auto()
    OXYTOCIN = auto()
    NEUROPHYSIN_I = auto()
    NEUROPHYSIN_II = auto()
    COPEPTIN = auto()
    NEUROMEDIN_U = auto()
    NEUROPEPTIDE_B = auto()
    NEUROPEPTIDE_S = auto()
    NEUROPEPTIDE_Y = auto()
    PANCREATIC_POLYPEPTIDE = auto()
    PEPTIDE_YY = auto()
    ENKEPHALINS = auto()
    ARACHIDONYL_GLYCERYL_ETHER_2 = auto()
    URIDINE = auto()
    GUANOSINE = auto()
    DYNORPHINS = auto()
    NEOENDORPHINS = auto()
    ENDORPHINS = auto()
    ENDOMORPHINS = auto()
    MORPHINE = auto()
    NOCICEPTIN_ORPHANIN_FQ = auto()
    OREXIN_A = auto()
    OREXIN_B = auto()
    PARATHYROID_HORMONE_RELATED_PROTEIN = auto()
    KISSPEPTIN = auto()
    NEUROPEPTIDE_FF = auto()
    PROLACTIN_RELEASING_PEPTIDE = auto()
    PYROGLUTAMYLATED_RFAMIDE_PEPTIDE = auto()
    SECRETIN = auto()
    MOTILIN = auto()
    GLUCAGON = auto()
    GLUCAGON_LIKE_PEPTIDE_1 = auto()
    GLUCAGON_LIKE_PEPTIDE_2 = auto()
    VASOACTIVE_INTESTINAL_PEPTIDE = auto()
    GROWTH_HORMONE_RELEASING_HORMONE = auto()
    PITUITARY_ADENYLATE_CYCLASE_ACTIVATING_PEPTIDE = auto()
    INOSINE = auto()
    ARACHIDONOYLGLYCEROL_2 = auto()
    SOMATOSTATIN = auto()
    GROWTH_HORMONE_INHIBITING_HORMONE = auto()
    NEUROKININ_A = auto()
    NEUROKININ_B = auto()
    SUBSTANCE_P = auto()
    NEUROPEPTIDE_K = auto()
    AGOUTI_RELATED_PEPTIDE = auto()
    N_ACETYLASPARTYLGLUTAMATE = auto()
    COCAINE_AND_AMPHETAMINE_REGULATED_TRANSCRIPT = auto()
    GONADOTROPIN_RELEASING_HORMONE = auto()
    THYROTROPIN_RELEASING_HORMONE = auto()
    MELANIN_CONCENTRATING_HORMONE = auto()
    NITRIC_OXIDE = auto()
    CARBON_MONOXIDE = auto()
    HYDROGEN_SULFIDE = auto()


NEUROTRANSMITTER_ALIAS_MAP = {
    "arginine": Neurotransmitter.ARGININE,
    "arg": Neurotransmitter.ARGININE,
    "r": Neurotransmitter.ARGININE,
    "aspartate": Neurotransmitter.ASPARTATE,
    "asp": Neurotransmitter.ASPARTATE,
    "d": Neurotransmitter.ASPARTATE,
    "glutamate": Neurotransmitter.GLUTAMATE,
    "glu": Neurotransmitter.GLUTAMATE,
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
