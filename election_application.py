candidates = []
voters = set()
voted_voters = set()
votes = []

def is_numeric(input_str):
    return input_str.isdigit()

def register_candidate():
    name = input("Enter candidate party name: ").strip()
    if name in candidates:
        print("Candidate already registered.")
    else:
        candidates.append(name)
        print("Candidate registered successfully.")

def register_voter():
    try:
        age = int(input("Enter voter age: "))
    except ValueError:
        print("Invalid input. Age must be a number.")
        return

    if age < 18:
        print("Sorry, you are not up to voting age.")
        return

    name = input("Enter voter name: ").strip()
    lga = input("Enter voter LGA: ").strip()

    if name in voters:
        print("Voter already registered.")
    else:
        voters.add(name)
        print("Voter registered successfully.")

def cast_vote():
    if not voters or not candidates:
        print("No voters or candidates registered.")
        return

    voter_name = input("Enter your voter name: ").strip()

    if voter_name not in voters:
        print("You are not registered as a voter.")
        return

    if voter_name in voted_voters:
        print("You have already voted.")
        return

    print("Candidates:")
    for index, candidate in enumerate(candidates, start=1):
        print(f"{index}. {candidate}")

    vote_input = input("Enter the number of the candidate you want to vote for: ").strip()

    if not is_numeric(vote_input):
        print("Invalid input! You must enter a number.")
        return

    choice = int(vote_input)

    if 1 <= choice <= len(candidates):
        selected_candidate = candidates[choice - 1]
        votes.append(selected_candidate)
        voted_voters.add(voter_name)
        print(f"Vote cast successfully for {selected_candidate}")
    else:
        print("Invalid candidate number.")

def view_results():
    if not votes:
        print("No votes cast yet.")
        return

    print("\nElection Results:")
    result_count = {}
    for candidate in candidates:
        result_count[candidate] = votes.count(candidate)

    for candidate, count in result_count.items():
        print(f"{candidate}: {count} vote(s)")

def main():
    while True:
        print("\n1. Register Candidate Party")
        print("2. Register Voter")
        print("3. Cast Vote")
        print("4. View Results")
        print("5. Exit")

        choice_input = input("Enter your choice: ").strip()

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
