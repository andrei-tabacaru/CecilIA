from llm_interaction import generate_scenario, generate_outcome
from user import UserProfile
from utils import parse_scenario
from audio_mechanics import speak_text_in_memory

def main():
    """
    Main game loop.
    """

    name = input("Enter the name of your character: ")
    user = UserProfile(name = name)

    last_scenario_and_choice = None

    while True:
        print("\n--- Current Status ---")
        print(f"Name: {user.name}")
        print(f"Age: {user.age}")
        print(f"Attributes: {user.attributes}")
        print("----------------------\n")

        scenario_text = generate_scenario(user)
        if scenario_text is None:
            break
        
        scenario_description, choices, hidden_changes = parse_scenario(scenario_text)
        if scenario_description is None or choices is None or hidden_changes is None:
            print("Failed to parse scenario. Exiting.")
            break

        print("\n" + scenario_description + '\n')
        speak_text_in_memory(scenario_description)
        for letter, desc in choices:
            print(f"{letter}) {desc}")

        user_choice = input("\nWhat do you choose?: ").upper()

        chosen_changes = hidden_changes.get(user_choice, {})

        last_scenario_and_choice = (scenario_text, user_choice)

        user.update_attributes(
            health = chosen_changes.get("health", 0),
            wealth = chosen_changes.get("wealth", 0),
            happiness = chosen_changes.get("happines", 0),
            intelligence = chosen_changes.get("intelligence", 0),
        )

        if last_scenario_and_choice:
            outcome_text = generate_outcome(user, scenario_text, user_choice)
            if outcome_text is not None:
                print("Outcome: ")
                print(outcome_text + "\n")
                speak_text_in_memory(outcome_text)

        user.add_decision(user.age, user_choice)
        user.age += 1

if __name__ == "__main__":
    main()

