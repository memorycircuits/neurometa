import datetime
import json
import os
import pickle
from pathlib import Path
from typing import Optional

import wikipediaapi


def section_unpacker(section, current_dict: Optional[dict] = None):
    unpacked_data = current_dict or {}
    if section.text:
        for line in section.text.split("\n"):
            processed_line = line.split(",")[0].replace(" and ", " & ").strip()
            if not processed_line or "References" in processed_line:
                continue

            parenthesis_split = processed_line.split("(")

            if len(parenthesis_split) > 1:
                unpacked_data[parenthesis_split[0].strip()] = processed_line
            else:
                unpacked_data[processed_line] = processed_line
    else:
        for sub_section in section.sections:
            unpacked_data = section_unpacker(sub_section, unpacked_data)

    return unpacked_data


directory_path = Path(__file__).parent
backups_path = directory_path / "backups"
os.makedirs(backups_path, exist_ok=True)

wiki_api = wikipediaapi.Wikipedia(
    language="en", extract_format=wikipediaapi.ExtractFormat.WIKI
)

today = datetime.date.today()
wiki_page = wiki_api.page("List_of_model_organisms")

result = {}
for section in wiki_page.sections:
    if "Eukaryotes" == section.title:
        for eu_section in section.sections:
            result[eu_section.title] = section_unpacker(section)
    else:
        result[section.title] = section_unpacker(section)

most_recent_model_organisms = directory_path.parent / "recent_list_of_model_organisms.json"
if most_recent_model_organisms.exists():
    with open(most_recent_model_organisms, "r") as in_json:
        previous_dataset = json.load(in_json)
else:
    previous_dataset = None

# I/O operations
if previous_dataset != result:
    with open(most_recent_model_organisms, "w") as out_json:
        json.dump(result, out_json)

    if not (
            backup_pickle_path := backups_path / f"wiki_page_bak_{today}.pickle"
    ).exists():
        with open(backup_pickle_path, "wb") as out_bakfile:
            # Create a backup of the wikipedia page
            pickle.dump(wiki_page, out_bakfile)

    print("Change since last run, new entry added")
else:
    print("No change since last run, adding a new entry is redundant (skipping save)")
