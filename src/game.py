from llm_interaction import generate_scenario, generate_outcome
from user import UserProfile
from utils import parse_scenario

def update_attributes(user_profile: UserProfile, choice: str):
    """
    Updates the user's attributes based on their choice.

    Args:
        user_profile: The UserProfile object.
        choice: The choice made by the user (e.g., "A", "B", "C").
    """

    # Implement your logic here for how choices affect attributes
    # This is a placeholder; you'll need to refine this based on your game's rules
    # if choice == "A":
    #     user_profile.update_attributes(health=1, happiness=1)
    # elif choice == "B":
    #     user_profile.update_attributes(intelligence=2)
    # ...and so on

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
        # print("DEBUG => scenario_text: ", scenario_text)
        if scenario_text is None:
            break

        # scenario_description, choices = parse_scenario(scenario_text)
        # print("DEBUG => scenario_description: ", scenario_description)
        # print("DEBUG => choices:", choices) 
        # if scenario_description is None or choices is None:
        #     print("Failed to parse scenario. Exiting.")
        #     break
        
        scenario_description, choices, hidden_changes = parse_scenario(scenario_text)
        # print("DEBUG => scenario_description: ", scenario_description)
        # print("DEBUG => choices: ", choices)
        # print("DEBUG => hidden_changes: ", hidden_changes)
        if scenario_description is None or choices is None or hidden_changes is None:
            print("Failed to parse scenario. Exiting.")
            break

        print("\n" + scenario_description + '\n')
        # for choice_str in choices:
        #     print(choice_str)
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

                # choice_description = ""
                # for choice_letter, desc in choices:
                #     if choice_letter == user_choice:
                #         choice_description = desc
                #         break
                
                # update_attributes(user, choice_description, outcome_text)
        # else:
        #     print("Error generating outcome")
        #     break

        # update_attributes(user, user_choice)
        user.add_decision(user.age, user_choice)
        user.age += 1

if __name__ == "__main__":
    main()

