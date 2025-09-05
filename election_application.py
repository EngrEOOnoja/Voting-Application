candidates = {}
voters = {}     	


def is_numeric(input_str):
    return input_str.isdigit()

def register_candidate():
    name = input("Enter candidate party name: ")
    if name in candidates:
        print("Candidate already registered.")
    else:
        candidates[name] = 0 
        print("Candidate registered successfully.")

def register_voter():
    age = input("Enter voter age: ")
    if(type(age) != int):
    	print("Invalid input. Age must be a number.")
    	return

    if age < 18:
        print("Sorry, you are not up to voting age.")
        return

    name = input("Enter voter name: ")
    lga = input("Enter voter LGA: ")

    if name in voters:
        print("Voter already registered.")
    else:
        voters[name] = {"age": age, "lga": lga, "has_voted": False}
        print("Voter registered successfully.")

def cast_vote():
    if not voters or not candidates:
        print("No voters or candidates registered.")
        return

    voter_name = input("Enter your voter name: ")

    if voter_name not in voters:
        print("You are not registered as a voter.")
        return

    if voters[voter_name]["has_voted"]:
        print("You have already voted.")
        return

    print("Candidates:")
    for index, candidate in enumerate(candidates.keys(), start=1):
        print(f"{index}. {candidate}")

    vote_input = input("Enter the number of the candidate you want to vote for: ")

    if not is_numeric(vote_input):
        print("Invalid input! You must enter a number.")
        return

    choice = int(vote_input)

    if 1 <= choice <= len(candidates):
        selected_candidate = list(candidates.keys())[choice - 1]
        candidates[selected_candidate] += 1
        voters[voter_name]["has_voted"] = True
        print(f"Vote cast successfully for {selected_candidate}")
    else:
        print("Invalid candidate number.")

def view_results():
    if all(votes == 0 for votes in candidates.values()):
        print("No votes cast yet.")
        return

    print("\nElection Results:")
    for candidate, count in candidates.items():
        print(f"{candidate}: {count} vote(s)")

def main():
    print(type(candidates))
    while True:
        print("\n1. Register Candidate Party")
        print("2. Register Voter")
        print("3. Cast Vote")
        print("4. View Results")
        print("5. Exit")

        choice_input = input("Enter your choice: ")

        if not is_numeric(choice_input):
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        choice = int(choice_input)

        if choice == 1:
            register_candidate()
        elif choice == 2:
            register_voter()
        elif choice == 3:
            cast_vote()
        elif choice == 4:
            view_results()
        elif choice == 5:
            print("Exiting........!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 5.")

main()

