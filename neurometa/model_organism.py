from typing import Optional

import wikipediaapi


def model_organism() -> dict:
    def section_unpacker(recursive_section, current_dict: Optional[dict] = None):
        unpacked_data = current_dict or {}
        if recursive_section.text:
            for line in recursive_section.text.split("\n"):
                processed_line = line.split(",")[0].replace(" and ", " & ").strip()
                if not processed_line or "References" in processed_line:
                    continue

                parenthesis_split = processed_line.split("(")

                if len(parenthesis_split) > 1:
                    unpacked_data[parenthesis_split[0].strip()] = processed_line
                else:
                    unpacked_data[processed_line] = processed_line
        else:
            for sub_section in recursive_section.sections:
                unpacked_data = section_unpacker(sub_section, unpacked_data)

        return unpacked_data

    wiki_api = wikipediaapi.Wikipedia(
        language="en", extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    wiki_page = wiki_api.page("List_of_model_organisms")

    result = {}
    for section in wiki_page.sections:
        if "Eukaryotes" == section.title:
            for eu_section in section.sections:
                result[eu_section.title] = section_unpacker(section)
        else:
            result[section.title] = section_unpacker(section)

    return result
