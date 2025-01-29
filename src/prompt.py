def generate_prompt(user):
    if user.age <= 2:
        life_stage = "infancy"
    elif user.age <= 5:
        life_stage = "early childhood"
    elif user.age <= 12:
        life_stage = "childhood"
    elif user.age <= 18:
        life_stage = "adolescence"
    elif user.age <= 65:
        life_stage = "adulthood"
    else:
        life_stage = "old age"

    prompt = (
        f"A character named {user.name} is {user.age} years old, in the {life_stage} stage of life. "
        f"Their current attributes are:\n"
        f"- Health: {user.attributes['health']}\n"
        f"- Wealth: {user.attributes['wealth']}\n"
        f"- Happiness: {user.attributes['happiness']}\n"
        f"- Intelligence: {user.attributes['intelligence']}\n\n"
    )
  
    if user.decision_history:
        prompt += "Recent decisions include: " + ", ".join(
            [f"At age {d['age']}: {d['decision']}" for d in user.decision_history]
        ) + ".\n\n"
    else:
        prompt += "No major decisions have been made yet.\n\n"

    prompt += f"Generate a scenario for {user.name} in the {life_stage} stage of life. "
    prompt += "Present the scenario and then provide 3-4 clear choices for how they should react. "
    prompt += "Label each choice with a letter (A, B, C, D). "
    prompt += "Do not generate the outcome of the choices.\n\n"
    prompt += "Important formatting instructions:\n"
    prompt += "1) Do NOT use any markdown or bold/italic text around the choice labels.\n"
    prompt += "2) The labels must appear exactly like:\n"
    prompt += "A) <choice>\n"
    prompt += "B) <choice>\n"
    prompt += "C) <choice>\n"
    prompt += "etc.\n\n"

    if life_stage == "infancy":
        prompt += (
            "Generate a scenario where the character interacts with their parents or caregivers. "
            "Include decisions such as developing physical skills (e.g., crawling, walking) or responding to early social cues. "
            "Each choice should influence their attributes like health and happiness."
        )
    elif life_stage == "early childhood":
        prompt += (
            "Generate a scenario focused on play, early learning, or relationships with other children. "
            "Include decisions like joining a playgroup, learning a new skill, or dealing with early conflicts. "
            "Each choice should influence happiness, intelligence, or social skills."
        )
    elif life_stage == "childhood":
        prompt += (
            "Generate a scenario about school, hobbies, or family interactions. "
            "Include decisions like choosing a favorite subject, making friends, or trying a new sport. "
            "Each choice should impact attributes like intelligence, health, or happiness."
        )
    elif life_stage == "adolescence":
        prompt += (
            "Generate a scenario focused on friendships, education, or discovering personal interests. "
            "Include decisions like joining a club, focusing on academics, or exploring early career paths. "
            "Each choice should influence intelligence, happiness, or future opportunities."
        )
    elif life_stage == "adulthood":
        prompt += (
            "Generate a scenario related to career, relationships, or personal growth. "
            "Include decisions like pursuing a promotion, starting a family, or taking a financial risk. "
            "Each choice should impact attributes like wealth, happiness, or health."
        )
    elif life_stage == "old age":
        prompt += (
            "Generate a scenario about retirement, health management, or leaving a legacy. "
            "Include decisions like mentoring younger generations, pursuing a hobby, or prioritizing health. "
            "Each choice should influence happiness, health, or social connections."
        )

    prompt += (
        "After listing the choices, add a line exactly containing:\n"
        "###HIDDEN_CHANGES###\n"
        "On the next line, output valid JSON mapping each choice letter (A, B, C, D) to an object with four keys:\n"
        "  health, wealth, happiness, intelligence.\n"
        "\n"
        "Constraints for each choice's attribute changes:\n"
        "1) You may only increase at most ONE attribute.\n"
        "2) You may optionally decrease ONE different attribute, but it's not mandatory.\n"
        "3) Any increase or decrease should be small (between -2 and +2), and logically consistent with the choice.\n"
        "4) If you don't want to change an attribute, set it to 0.\n"
        "\n"
        "Example of the JSON format:\n"
        "{\n"
        '  "A": {"health": +1, "wealth": 0, "happiness": 0, "intelligence": -1},\n'
        '  "B": {"health": 0, "wealth": 0, "happiness": +1, "intelligence": 0},\n'
        '  "C": {"health": 0, "wealth": 0, "happiness": 0, "intelligence": 0}\n'
        "}\n"
        "\n"
        "Do NOT explain or justify these changes. Only produce the scenario text, then the labeled choices, "
        "then ###HIDDEN_CHANGES###, then the JSON. No additional commentary.\n"
        "Do not wrap the scenario or choices in JSON; only the changes.\n"
        "The scenario must not reveal how attributes are changed.\n"
    )

    return prompt
