import json

import pandas as pd


neurotransmitters = []
for row in pd.read_excel("neurotransmitter.ods").iterrows():
    row = row[1]

    neurotransmitters.append(
        (row[1] if isinstance(row[2], float) else "; ".join(row[1:3]))
        .strip()
        .replace("\xa0", " ")
    )

with open("neurotransmitters.json", "w") as out_json:
    json.dump(neurotransmitters, out_json)
