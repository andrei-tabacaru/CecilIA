import re
import json

def parse_scenario(scenario_text: str):
    """
    Returns:
      scenario_description (str),
      choices (list of (letter, desc)),
      changes (dict mapping 'A' -> {health, wealth, ...})
    """
    if '###HIDDEN_CHANGES###' in scenario_text:
        main_part, changes_part = scenario_text.split("###HIDDEN_CHANGES###", 1)
    else:
        return None, None, None
    
    lines = main_part.split("\n")
    # lines = scenario_text.split("\n")
    scenario_description = []
    choices = []

    choice_regex = re.compile(r'^[*\s]*([A-D])\)\s*(.*)', re.IGNORECASE)

    for line in lines:
        line = line.strip()
        match = choice_regex.match(line)
        # If this line starts with "A)", "B)", "C)" or "D)"
        if match:
            # letter = match.group(1) #e.g. A
            # choice_desc = match.group(2) #e.g. Focus instanlty on...
            # choice_desc = choice_desc.strip()
            letter = match.group(1).upper()
            choice_text = match.group(2).strip()
            choices.append((letter, choice_text))
        else:
            # It's part of the scenario description
            scenario_description.append(line)

    # Join the scenario text lines
    scenario_text_clean = "\n".join(scenario_description).strip()

    # If no choices were found
    # if not choices:
    #     return None, None

    # return scenario_text_clean, choices

    changes_part = changes_part.strip()

    try:
        changes_part = changes_part.replace('+', '')
        changes = json.loads(changes_part)
    except json.JSONDecodeError:
        changes = {}

    if not choices or not changes:
        return None, None, None

    return scenario_text_clean, choices, changes    