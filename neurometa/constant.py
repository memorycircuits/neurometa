from enum import Enum, IntEnum, auto


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


class BrainStructure(Enum):
    AMYGDALOID_COMPLEX = "amygdaloid complex"
    ANSA_LENTICULARIS = "ansa lenticularis"
    ARACHNOID_MATER = "arachnoid mater"
    ARBOR_VITAE = "arbor vitae"
    ARCUATE_FASCICULUS = "arcuate fasciculus"
    BASILAR_ARTERY = "basilar artery"
    BASONUCLEUS_AMYGDALA = "basonucleus amygdala"
    BERGMANN_GLIA = "bergmann glia"
    BERNASCONI_VEIN = "bernasconi vein"
    BLOOD_BRAIN_BARRIER = "blood brain barrier"
    BLOOD_VESSELS = "blood vessels"
    BODY_OF_FORNIX = "body of fornix"
    BRACHIUM_CONJUNCTIVUM = "brachium conjunctivum"
    BRAIN_BARRIER_SYSTEM = "brain barrier system"
    CA1 = "ca1"
    CA2 = "ca2"
    CA3 = "ca3"
    CA4 = "ca4"
    CALCARINE_SULCUS = "calcarine sulcus"
    CALLOSAL_SULCUS = "callosal sulcus"
    CALLOSOMARGINAL_ARTERY = "callosomarginal artery"
    CAUDATE = "caudate"
    CAUDATE_NUCLEUS = "caudate nucleus"
    CAVERNOSUS_SINUS = "cavernosus sinus"
    CAVE_OF_RETZIUS = "cave of retzius"
    CENTRAL_ARTERY = "central artery"
    CENTRAL_CANAL = "central canal"
    CENTRAL_LOBULE = "central lobule"
    CENTRAL_NUCLEUS_AMYGDALA = "central nucleus amygdala"
    CEREBELLAR_ARTERY = "cerebellar artery"
    CEREBELLAR_CORTEX = "cerebellar cortex"
    CEREBELLAR_NUCLEI = "cerebellar nuclei"
    CEREBELLAR_TONSIL = "cerebellar tonsil"
    CEREBELLAR_PEDUNCLES = "cerebellar peduncles"
    CEREBELLAR_PEDUNCLES_MIDDLE = "cerebellar peduncles middle"
    CEREBELLAR_VESSELS = "cerebellar vessels"
    CEREBELLAR_WHITE_MATTER = "cerebellar white matter"
    CEREBRAL_AQUEDUCT = "cerebral aqueduct"
    CEREBRAL_ARTERY = "cerebral artery"
    CEREBRAL_ENDOTHELIAL_CELL = "cerebral endothelial cell"
    CEREBRAL_VEIN = "cerebral vein"
    CEREBRAL_VESSELS = "cerebral vessels"
    CEREBROSPINAL_FLUID = "cerebrospinal fluid"
    CHOROIDAL_ARTERY = "choroidal artery"
    CHOROID_PLEXUS = "choroid plexus"
    CHOROID_PLEXUS_EPITHELIUM = "choroid plexus epithelium"
    CHOROID_PLEXUS_VESSELS = "choroid plexus vessels"
    CINGULATE = "cingulate"
    CINGULUM = "cingulum"
    CIRCLE_OF_WILLIS = "circle of willis"
    CIRCUMFLEX_FASCICULUS = "circumflex fasciculus"
    COLICULUS = "coliculus"
    COLSULCUS = "colsulcus"
    COLUMN_OF_FORNIX = "column of fornix"
    COMMISSURE = "commissure"
    COMMISSURE_WHITE_MATTER = "commissure white matter"
    COMMISURE = "commisure"
    COMMUNICATING_ARTERY = "communicating artery"
    CORPUS_CALLOSUM_BODY = "corpus callosum body"
    CORPUS_CALLOSUM_GENU = "corpus callosum genu"
    CORPUS_CALLOSUM_ROSTRUM = "corpus callosum rostrum"
    CORPUS_CALLOSUM_SPLENIUM = "corpus callosum splenium"
    CORTEX = "cortex"
    CORTICAL_NUCLEUS_AMYGDALA = "cortical nucleus amygdala"
    CORTICOSPINAL_TRACT = "corticospinal tract"
    CRUS_CEREBRI = "crus cerebri"
    CRUS_OF_FORNIX = "crus of fornix"
    CULMEN = "culmen"
    CULMEN_VERMIS = "culmen vermis"
    CUNEUS = "cuneus"
    DECLIVE = "declive"
    DECLIVE_VERMIS = "declive vermis"
    DENDRITE = "dendrite"
    DENTATE_GYRUS = "dentate gyrus"
    DENTATE_GYRUS_SULCUS = "dentate gyrus sulcus"
    DENTATE_NUCLEUS = "dentate nucleus"
    DG = "dg"
    DIAGONAL_BAND_OF_BROCA = "diagonal band of broca"
    DURA_MATER = "dura mater"
    EMBOLIFORM_NUCLEUS = "emboliform nucleus"
    ENTORHINAL_CORTEX = "entorhinal cortex"
    EPENDYMAL_CELL = "ependymal cell"
    EPENDYMOGLIA = "ependymoglia"
    FASTIGIAL_NUCLEUS = "fastigial nucleus"
    FASTIGIUM = "fastigium"
    FIBROUS_ASTROCYTE = "fibrous astrocyte"
    FIMBRIA = "fimbria"
    FISSURE_OF_SYLVIUS = "fissure of sylvius"
    FLOCCULONODULAR_LOBE = "flocculonodular lobe"
    FLOCCULUS = "flocculus"
    FOLLICULI = "folliculi"
    FORAMEN_OF_MONRO = "foramen of monro"
    FORCEPS_MAJOR = "forceps major"
    FORCEPS_MINOR = "forceps minor"
    FOURTH_VENTRICLE = "fourth ventricle"
    FRONTAL_GYRUS = "frontal gyrus"
    FRONTAL_SULCUS = "frontal sulcus"
    FRONTOPOLAR_ARTERY = "frontopolar artery"
    FUNICULUSIS = "funiculusis"
    GENICULATE_NUCLEUS = "geniculate nucleus"
    GLOBOSE_NUCLEUS = "globose nucleus"
    GLOBUS_PALLIDUS = "globus pallidus"
    HABENULA = "habenula"
    HABENULAR_COMMISURE = "habenular commisure"
    HIPPOCAMPAL_SULCUS = "hippocampal sulcus"
    HIPPOCAMPUS = "hippocampus"
    HYPOTHALAMIC_COMMISSURE = "hypothalamic commissure"
    HYPOTHALAMIC_COMMISURE = "hypothalamic commisure"
    INDUSEUM_GRISIUM = "induseum grisium"
    INFUNDIBULUM = "infundibulum"
    INTERCALATED_NUCLEUS_AMYGDALA = "intercalated nucleus amygdala"
    INTERIOR_CEREBRAL_VEIN = "interior cerebral vein"
    INTERNAL_CAPSULE_GENU = "internal capsule genu"
    INTERNAL_CAPSULE_LIMB = "internal capsule limb"
    INTERNAL_CAROTID_ARTERY = "internal carotid artery"
    INTERPEDUNCULAR_FOSSA = "interpeduncular fossa"
    INTERPOSITUS_NUCLEUS = "interpositus nucleus"
    INTERVENTRICULAR_FORAMEN = "interventricular foramen"
    INTRALAMINAR_NUCLEUS_THALAMUS = "intralaminar nucleus thalamus"
    LAMINA_TERMINALIS = "lamina terminalis"
    LATERONUCLEUS = "lateronucleus"
    LEMNISCUS = "lemniscus"
    LENTICULAR_FASCICULUS = "lenticular fasciculus"
    LENTICULOSTRIATE_ARTERIES = "lenticulostriate arteries"
    LINGUAL_GYRUS = "lingual gyrus"
    LINGUAL_SULCUS = "lingual sulcus"
    LONGITUDINAL_FASCICULUS = "longitudinal fasciculus"
    LUSHKA_FORAMEN = "lushka foramen"
    MAGENDIE_FORAMEN = "magendie foramen"
    MAMMILLARY_BODY = "mammillary body"
    MAMMILLARY_RECESS = "mammillary recess"
    MASSA_INTERMEDIA = "massa intermedia"
    MEDULLARY_RETICULOSPINAL_TRACT = "medullary reticulospinal tract"
    MEDULLARY_VELUM = "medullary velum"
    MENINGEAL_VESSELS = "meningeal vessels"
    MIDDLE_CEREBRAL_ARTERY = "middle cerebral artery"
    MIDDLE_CEREBRAL_VEIN = "middle cerebral vein"
    MIDDLE_TEMPORAL_GYRUS = "middle temporal gyrus"
    MIDLINE_NUCLEUS_THALAMUS = "midline nucleus thalamus"
    NUCLEUS_AMYGDALA = "nucleus amygdala"
    NUCLEUS_THALAMUS = "nucleus thalamus"
    NUCLUES_ACCUMBENS = "nuclues accumbens"
    OCCIPITAL_GYRUS = "occipital gyrus"
    OCCIPITAL_SINUS = "occipital sinus"
    OCCIPITAL_SULCUS = "occipital sulcus"
    OCCIPITOTEMPORAL_GYRUS = "occipitotemporal gyrus"
    OCCIPITOTEMPORAL_SULCUS = "occipitotemporal sulcus"
    OLFACTORY_SULCUS = "olfactory sulcus"
    OLFACTORY_TRIGONE = "olfactory trigone"
    OLIGODENDROCYTE = "oligodendrocyte"
    OLIVARY_COMPLEX = "olivary complex"
    OLIVOSPINAL_TRACT = "olivospinal tract"
    OPHTHALMIC_ARTERY = "ophthalmic artery"
    OPTIC_CHIASM = "optic chiasm"
    OPTIC_NERVE = "optic nerve"
    OPTIC_RECESS = "optic recess"
    ORBIFRONTAL_GYRUS = "orbifrontal gyrus"
    ORBITOFRONTAL_ARTERY = "orbitofrontal artery"
    ORBITOFRONTAL_CORTEX = "orbitofrontal cortex"
    PARACENTRAL_LOBULE = "paracentral lobule"
    PARAFLOCCULUS = "paraflocculus"
    PARAHIPPOCAMPAL_GYRUS = "parahippocampal gyrus"
    PARAVENTRICULAR_NUCLEUS_THALAMUS = "paraventricular nucleus thalamus"
    PARENCHYMAL_FEET = "parenchymal feet"
    PARIETAL_GYRUS = "parietal gyrus"
    PARIETAL_LOBE = "parietal lobe"
    PARIETAL_LOBULE = "parietal lobule"
    PARIETAL_OPERCULUM = "parietal operculum"
    PARIETO_OCCIPITAL_ARTERY = "parieto occipital artery"
    PARIETO_OCCIPITAL_NOTCH = "parieto occipital notch"
    PARIETO_OCCIPITAL_SULCUS = "parieto occipital sulcus"
    PARS_OPERCULARIS = "pars opercularis"
    PARS_ORBITALIS = "pars orbitalis"
    PARS_TRIANGULARIS = "pars triangularis"
    PEDUNCULOPONTINE_NUCLEUS = "pedunculopontine nucleus"
    PERFORATED_SUBSTANCE = "perforated substance"
    PERICALLOSAL_ARTERY = "pericallosal artery"
    PERIRHINAL_CORTEX = "perirhinal cortex"
    PETROSAL_SINUS = "petrosal sinus"
    PIASTROCYTE = "piastrocyte"
    PIA_MATER = "pia mater"
    PINEALOCYTE = "pinealocyte"
    PINEAL_GYRUS = "pineal gyrus"
    PINEAL_RECESS = "pineal recess"
    PITUICYTE = "pituicyte"
    PITUITARY_GYRUS = "pituitary gyrus"
    PONS = "pons"
    PONTINE_FIBERS = "pontine fibers"
    PONTINE_RETICULOSPINAL_TRACT = "pontine reticulospinal tract"
    POSTCENTRAL_ARTERY = "postcentral artery"
    POSTCENTRAL_GYRUS = "postcentral gyrus"
    PRECENTRAL_ARTERY = "precentral artery"
    PRECENTRAL_GYRUS = "precentral gyrus"
    PRECENTRAL_SULCUS = "precentral sulcus"
    PRECUNEUS = "precuneus"
    PREMOTOR_CORTEX = "premotor cortex"
    PREOPTIC_AREA = "preoptic area"
    PREPYRIFORM_AREA = "prepyriform area"
    PRESUBICULUM = "presubiculum"
    PRIMARY_AUDITORY_CORTEX = "primary auditory cortex"
    PRIMARY_FISSURE = "primary fissure"
    PRIMARY_MOTOR_CORTEX = "primary motor cortex"
    PRIMARY_SENSORY_CORTEX = "primary sensory cortex"
    PRIMARY_SOMATOSENSORY_CORTEX = "primary somatosensory cortex"
    PRIMARY_VISUAL_CORTEX = "primary visual cortex"
    PRIMAR_VISUAL_CORTEX = "primar visual cortex"
    PROSUBICULUM = "prosubiculum"
    PROTOPLASMIC_ASTROCYTE = "protoplasmic astrocyte"
    PULVINAR = "pulvinar"
    PULVINAR_NUCLEUS = "pulvinar nucleus"
    PUTAMEN = "putamen"
    PYRAMIDAL_CELL = "pyramidal cell"
    PYRAMIDAL_TRACT = "pyramidal tract"
    PYRAMIS = "pyramis"
    PYRAMIS_VERMIS = "pyramis vermis"
    RADIAL_GLIA = "radial glia"
    RECESS = "recess"
    RECURRENT_ARTERY_OF_HEBERDEN = "recurrent artery of heberden"
    RED_NUCLEUS = "red nucleus"
    RETICULAR_FORMATION = "reticular formation"
    RETICULAR_NUCLEUS = "reticular nucleus"
    RETICULAR_NUCLEUS_THALAMUS = "reticular nucleus thalamus"
    RETROLENFICULAR_PART = "retrolenficular part"
    RETROSPLENIAL_CORTEX = "retrosplenial cortex"
    RHINAL_SULCUS = "rhinal sulcus"
    RHOMBIC_LIP = "rhombic lip"
    ROSSENTHAL_VEIN = "rossenthal vein"
    RUBROSPINAL_TRACT = "rubrospinal tract"
    SAGITTAL_SINUS = "sagittal sinus"
    SECONDARY_AUDITORY_CORTEX = "secondary auditory cortex"
    SECONDARY_SOMATOSENSORY_CORTEX = "secondary somatosensory cortex"
    SECONDARY_VISUAL_CORTEX = "secondary visual cortex"
    SEPTAL_NUCLEUS = "septal nucleus"
    SEPTUM = "septum"
    SEPTUM_PELLUCIDUM = "septum pellucidum"
    SEPTUM_VERUM = "septum verum"
    SHORT_CINGULATE_GYRUS = "short cingulate gyrus"
    SHORT_INSULAR_GYRUS = "short insular gyrus"
    SIGMOID_SINUS = "sigmoid sinus"
    SILVIAN_FISSURE = "silvian fissure"
    SIMPLE_LOBULE = "simple lobule"
    SINGULATE = "singulate"
    SINGULATE_GYRUS = "singulate gyrus"
    SINGULATE_SULCUS = "singulate sulcus"


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
