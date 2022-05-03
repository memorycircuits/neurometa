def scrape_sessions_from_wiki_class(root_section):
    if root_section.sections:
        return {
            deeper_section.title: scrape_sessions_from_wiki_class(deeper_section)
            for deeper_section in root_section.sections
        }
    else:
        return root_section.title


def define_depth_for_every_subfield(rem_section, rem_section_data, previous_subsection):
    current_subsections = previous_subsection[rem_section]

    subsections, substructures = {}, []
    for i, data in enumerate(rem_section_data, start=1):
        if isinstance(data, dict):
            subsections.update(data)
        elif data in current_subsections:
            subsections[data] = define_depth_for_every_subfield(
                data, rem_section_data[i:], current_subsections
            )
        else:
            substructures.append(data)

    if subsections:
        subsections["Substructures"] = substructures
        return subsections
    return substructures


def serialize_wikipedia_sections(wiki_page):
    def serializer(section):
        return {
            "level": section.level,
            "title": section.title.strip(),
            "text": section.text.strip(),
            "sections": [
                serializer(sub_sub_section) for sub_sub_section in section.sections
            ],
        }

    result = [serializer(section) for section in wiki_page.sections]
    return result
