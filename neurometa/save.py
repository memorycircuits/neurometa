import json
import os
from datetime import date
from pprint import pprint

from deepdiff import DeepDiff
from orjson import orjson
from pydantic import DirectoryPath

from neurometa.human_brain_tree.main import human_brain_tree
from neurometa.model_organism import model_organism
from neurometa.neurotransmitter.main import neurotransmitter


def save_data(dataset: dict, dataset_label: str, save_dir: DirectoryPath):
    try:
        latest_dataset_filename = str(os.listdir(save_dir)[-1])
    except IndexError:
        pass

    assert latest_dataset_filename.startswith(
        dataset_label
    ), f"dataset_label={dataset_label}, should be at the start of the filename"

    with open(save_dir / latest_dataset_filename, "rb") as in_json:
        latest_dataset = json.load(in_json)

    difference = DeepDiff(dataset, latest_dataset, ignore_order=True)
    difference.pop("type_changes", None)
    if not difference:
        return print("Done: No change in data since last save, nothing new to store")

    print("Difference:")
    pprint(difference, indent=2, width=200)

    new_dataset_filename = save_dir / f"{dataset_label}_{date.today()}.json"
    with open(new_dataset_filename, "w") as out_json:
        json.dump(dataset, out_json)

    print(f"Done: New dataset saved to {new_dataset_filename}\n\n")


def save_all(output_directory: DirectoryPath, make_directories: bool = False):
    datasets = {
        "human_brain_tree": human_brain_tree(),
        "model_organism": model_organism(),
        "neurotransmitter": neurotransmitter(),
    }
    for dataset_label, dataset in datasets.items():
        print(f"Saving {dataset_label} dataset")
        dataset_dir = output_directory / dataset_label
        if make_directories:
            os.mkdir(dataset_dir)
        save_data(dataset, dataset_label, dataset_dir)
