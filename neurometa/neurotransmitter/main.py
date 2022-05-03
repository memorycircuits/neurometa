import pkgutil

import pandas as pd


def neurotransmitter() -> dict:
    standard_neurotransmitter_names, neurotransmitter_with_alternative_names = [], []
    for row in pd.read_excel(
        pkgutil.get_data(__name__, "wikipedia_table.ods")
    ).iterrows():
        row = row[1]
        name, abbreviation = row[1:3]

        name = name.strip().replace("\xa0", " ")
        if "(" in name:
            name, alternative_name = name.split("(")
            name = name.strip()
            alternative_name = alternative_name.strip(") ")
        else:
            alternative_name = None

        standard_neurotransmitter_names.append(name.lower().replace(" ", "_"))

        if isinstance(abbreviation, float):  # abbreviation is nan
            names = name
        else:
            abbreviation = abbreviation.strip().replace("\xa0", " ")
            names = f"{name}; {abbreviation}"
        if alternative_name:
            names += f"; {alternative_name}"

        neurotransmitter_with_alternative_names.append(names)

    return dict(
        zip(standard_neurotransmitter_names, neurotransmitter_with_alternative_names)
    )
