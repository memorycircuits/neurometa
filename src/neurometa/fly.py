from enum import Enum


class DrosophilaBrainStructure(Enum):
    ANTENNAL_LOBE = "antennal lobe"
    ANTERIOR_OPTIC_TUBERCLE = "anterior optic tubercle"
    CENTRAL_LOBE = "central lobe"
    CREST = "crest"
    DORSAL_LOBE = "dorsal lobe"
    DORSOMEDIAL_PROTOCEREBRUM = "dorsomedial protocerebrum"
    ELLIPSOID_BODY = "ellipsoid body"
    FILA = "fila"
    LATERAL_BODY = "lateral body"
    LATERAL_HORN = "lateral horn"
    LATERAL_ACCESSORY_LOBE = "lateral accessory lobe"
    MUSHROOM_BODY = "mushroom body"
    MEDIAL_DOME = "medial dome"
    MAXILLARY_LOBE = "maxillary lobe"
    PROTOCEREBRAL_BRIDGE = "protocerebral bridge"
    POSTERIOR_SUPERIOR = "posterior superior"
    SUPERIOR_INTERMEDIATE_PROTOCEREBRUM = "superior intermediate protocerebrum"
    SUPERIOR_MEDIAL_PROTOCEREBRUM = "superior medial protocerebrum"
    SUPERIOR_LATERAL_PROTOCEREBRUM = "superior lateral protocerebrum"
    TRACT = "tract"
    VENTROLATERAL_PROTOCEREBRUM = "ventrolateral protocerebrum"
    VENTROPOSTERIOR_NEUROPIL = "ventroposterior neuropil"
    VESICLE = "vesicle"
    WEDGE = "wedge"


fly_brain_structure_to_abbreviation = {
    DrosophilaBrainStructure.ANTENNAL_LOBE: "AL",
    DrosophilaBrainStructure.ANTERIOR_OPTIC_TUBERCLE: "AOTU",
    DrosophilaBrainStructure.CENTRAL_LOBE: "CL",
    DrosophilaBrainStructure.CREST: "CRE",
    DrosophilaBrainStructure.DORSAL_LOBE: "DL",
    DrosophilaBrainStructure.DORSOMEDIAL_PROTOCEREBRUM: "DM",
    DrosophilaBrainStructure.ELLIPSOID_BODY: "EB",
    DrosophilaBrainStructure.FILA: "FLA",
    DrosophilaBrainStructure.LATERAL_BODY: "LB",
    DrosophilaBrainStructure.LATERAL_HORN: "LH",
    DrosophilaBrainStructure.LATERAL_ACCESSORY_LOBE: "LAL",
    DrosophilaBrainStructure.MUSHROOM_BODY: "MB",
    DrosophilaBrainStructure.MEDIAL_DOME: "MD",
    DrosophilaBrainStructure.MAXILLARY_LOBE: "MX",
    DrosophilaBrainStructure.PROTOCEREBRAL_BRIDGE: "PB",
    DrosophilaBrainStructure.POSTERIOR_SUPERIOR: "PS",
    DrosophilaBrainStructure.SUPERIOR_INTERMEDIATE_PROTOCEREBRUM: "SIP",
    DrosophilaBrainStructure.SUPERIOR_MEDIAL_PROTOCEREBRUM: "SMP",
    DrosophilaBrainStructure.SUPERIOR_LATERAL_PROTOCEREBRUM: "SLP",
    DrosophilaBrainStructure.TRACT: "TR",
    DrosophilaBrainStructure.VENTROLATERAL_PROTOCEREBRUM: "VLP",
    DrosophilaBrainStructure.VENTROPOSTERIOR_NEUROPIL: "VPN",
    DrosophilaBrainStructure.VESICLE: "VES",
    DrosophilaBrainStructure.WEDGE: "WED",
}


abbreviation_to_fly_brain_structure = {v: k for k, v in fly_brain_structure_to_abbreviation.items()}
