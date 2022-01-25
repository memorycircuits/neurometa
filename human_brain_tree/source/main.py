import datetime
import json
import pickle
import re
import shutil
from copy import copy
from pathlib import Path

import wikipediaapi

from human_brain_tree.source.utils import (
    scrape_sessions_from_wiki_class,
    define_depth_for_every_subfield,
)


OUTPUT_FILE_STEM = "brain_structure_hierarchy"

directory_path = Path(__file__).parent

re_and = re.compile(r" and ")
deli = re.compile(r"[,;]")
parenthesis_exp = re.compile(r"\([\w,; ]*\)")
id_followed_by_numbering = re.compile(r"^[\w ]* \d+")


wiki_api = wikipediaapi.Wikipedia(
    language="en", extract_format=wikipediaapi.ExtractFormat.WIKI
)

today = datetime.date.today()
wiki_page = wiki_api.page("List_of_regions_in_the_human_brain")

if not (
    backup_pickle_path := directory_path / "backups" / f"wiki_page_bak_{today}.pickle"
).exists():
    with open(backup_pickle_path, "wb") as out_bakfile:
        # Create a backup of the wikipedia page
        pickle.dump(wiki_page, out_bakfile)

section_titles = {}
for section in wiki_page.sections:
    section_titles[section.title] = scrape_sessions_from_wiki_class(section)

data, section_data = {}, []
section, deeper_section, current_section_field = None, None, None
for line in wiki_page.text.splitlines():
    if "Related topics" in line:
        break

    if not line or (":" not in line and len(line.split(" ")) >= 15):
        continue
    elif line in section_titles:
        if section:
            data[section] = copy(section_data)
            section_data = []
        section = line
    else:
        assert section
        if (parenthesis_exp_findings := re.findall(parenthesis_exp, line)) and len(
            parenthesis_exp_findings
        ) == 1:
            split_line = re.split(parenthesis_exp, line)
            if len(split_line) == 2:
                if not split_line[1]:
                    section_data.append(line.strip())
                    continue

        if " and " in line.lower():
            section_data.append(line)
        elif re.findall(deli, line):
            split_line = tuple(map(str.strip, re.split(deli, line)))
            if id_number := re.findall(id_followed_by_numbering, line):
                split_id_number = id_number[0].split(" ")
                parent = " ".join(split_id_number[:-1])
                first_id = split_id_number[-1]
                for idx, chunk in enumerate(split_line):
                    if first_id in chunk:
                        daughters = (
                            [first_id, *split_line[idx + 1 :]]
                            if "(" not in chunk
                            else [
                                f"{first_id} {parenthesis_exp_findings[0]}",
                                *split_line[idx + 2 :],
                            ]
                        )
                        break
            else:
                parent, daughters = split_line[0], split_line[1:]
            if ":" in parent:
                parent_split = parent.split(":")
                if len(parent_split) != 1:
                    assert len(parent_split) == 2, len(parent_split)
                    parent = parent_split[0].strip()
                    if parent_split[1]:
                        daughters = [parent_split[1].strip(), *daughters]
                else:
                    parent = parent.replace(":", "")

            # section_data.append({parent: [daughter for daughter in daughters if daughter.lower() == "other"]})
            section_data.append({parent: daughters})
        else:
            section_data.append(line)


data_with_depth = {}
for section, section_data in data.items():
    data_with_depth[section] = define_depth_for_every_subfield(
        section, section_data, section_titles
    )

organized_data = {"neuronal_structure": {}}
for section_name, data in data_with_depth.items():
    if "Neurotransmitter pathways" == section_name:
        organized_data["neurotransmitter"] = data
    elif "Neural pathways" == section_name:
        organized_data["neuronal_pathway"] = data
    else:
        organized_data["neuronal_structure"][section_name] = data

organized_data["neuro_endocrine_system"] = organized_data["neuronal_structure"].pop(
    "Neuro endocrine systems"
)
organized_data["neuro_vascular_system"] = organized_data["neuronal_structure"].pop(
    "Neuro vascular systems"
)
organized_data["dural_meningeal_system"] = organized_data["neuronal_structure"].pop(
    "Dural meningeal system"
)

flattened_structure_dataset = set()


def recursive_set_adder(data_to_add):
    if isinstance(data_to_add, str):
        flattened_structure_dataset.add(data_to_add.capitalize())
    elif isinstance(data_to_add, dict):
        for subsection_name, subsection in data_to_add.items():
            if any(data.isdigit() for data in subsection):
                for daughter_tag in subsection:
                    flattened_structure_dataset.add(f"{subsection_name} {daughter_tag}")
            else:
                recursive_set_adder(subsection)
    else:
        for data in data_to_add:
            recursive_set_adder(data)


for subsection in organized_data["neuronal_structure"].values():
    recursive_set_adder(subsection)

flattened_structure_dataset.remove("Surface")  # Absurd brain structure.

organized_data["neuronal_structure_flat"] = list(sorted(flattened_structure_dataset))
organized_data = dict(sorted(organized_data.items()))

most_recent_brain_tree_path = directory_path.parent / "recent_human_brain_tree.json"
with open(most_recent_brain_tree_path, "r") as in_json:
    previous_dataset = json.load(in_json)

# I/O operations
if previous_dataset != organized_data:
    most_recent_brain_tree_history_path = (
        directory_path.parent / "human_brain_trees" / f"human_brain_tree_{today}.json"
    )
    with open(most_recent_brain_tree_history_path, "w") as out_json:
        json.dump(organized_data, out_json)

    shutil.copy(most_recent_brain_tree_history_path, most_recent_brain_tree_path)

    print("Change since last run, new entry added")
else:
    print("No change since last run, adding a new entry is redundant (skipping save)")
