import json

import pandas as pd


neurotransmitter, neurotransmitter_with_alternative_names = [], []
for row in pd.read_excel("neurotransmitter.ods").iterrows():
    row = row[1]
    name, abbreviation = row[1:3]

    name = name.strip().replace("\xa0", " ")
    if "(" in name:
        name, alternative_name = name.split("(")
        name = name.strip()
        alternative_name = alternative_name.strip(") ")
    else:
        alternative_name = None

    neurotransmitter.append(name.lower().replace(" ", "_"))

    if isinstance(abbreviation, float):     # abbreviation is nan
        names = name
    else:
        abbreviation = abbreviation.strip().replace("\xa0", " ")
        names = f"{name}; {abbreviation}"
    if alternative_name:
        names += f"; {alternative_name}"

    neurotransmitter_with_alternative_names.append(names)


with open("neurotransmitters.json", "w") as out_json:
    json.dump(dict(zip(neurotransmitter, neurotransmitter_with_alternative_names)), out_json)
