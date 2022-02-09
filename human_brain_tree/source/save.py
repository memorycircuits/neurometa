import json
import os
import pickle
from datetime import date
from pathlib import Path


def save_data(brain_tree_data: dict, wiki_page, brain_tree_save_dir: Path):
    os.makedirs((wiki_backup_dir := brain_tree_save_dir / "source" / "backups"), exist_ok=True)
    os.makedirs((tree_backup_dir := brain_tree_save_dir / "previous_trees"), exist_ok=True)

    change = False
    today = date.today()

    most_recent_brain_tree_path = brain_tree_save_dir / "human_brain_tree.json"
    if most_recent_brain_tree_path.exists():
        with open(most_recent_brain_tree_path, "r") as in_json:
            previous_dataset = json.load(in_json)
    else:
        previous_dataset = None

    if previous_dataset != brain_tree_data:     # TODO: False inequalities are often triggered, fix.
        change = True
        today_brain_tree_path = tree_backup_dir / f"human_brain_tree_{today}.json"
        with open(today_brain_tree_path, "w") as out_json:
            json.dump(brain_tree_data, out_json)

        print(f"Replacing old brain tree data.\nPrevious data stored in {brain_tree_save_dir}")
        with open(most_recent_brain_tree_path, "w") as out_json:
            json.dump(brain_tree_data, out_json)

    if backup_filenames := os.listdir(wiki_backup_dir):
        newest_page_backup_path = wiki_backup_dir / backup_filenames[-1]
        with open(newest_page_backup_path, "rb") as in_bakfile:
            newest_page_backup = pickle.load(in_bakfile)
        create_backup = serialize_wikipedia_sections(newest_page_backup) != serialize_wikipedia_sections(wiki_page)
    else:
        create_backup = True

    if create_backup:
        change = True
        if not (
                backup_pickle_path := wiki_backup_dir / f"wiki_page_bak_{today}.pickle"
        ).exists():
            with open(backup_pickle_path, "wb") as out_bakfile:
                # Create a backup of the wikipedia page
                pickle.dump(wiki_page, out_bakfile)
        print("Adding new page version to backups")

    if not change:
        print("No change since last run")


def serialize_wikipedia_sections(wiki_page):
    def serializer(section):
        return {
            "level": section.level,
            "title": section.title.strip(),
            "text": section.text.strip(),
            "sections": [serializer(sub_sub_section) for sub_sub_section in section.sections]
        }

    result = [serializer(section) for section in wiki_page.sections]
    return result
