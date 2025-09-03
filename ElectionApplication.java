import java.util.ArrayList;
import java.util.Scanner;

public class ElectionApplication {
    public static ArrayList<String> candidates = new ArrayList<>();
    public static ArrayList<String> voters = new ArrayList<>();
    public static ArrayList<String> votes = new ArrayList<>();
    public static ArrayList<String> votedVoters = new ArrayList<>();

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Register Candidate party");
            System.out.println("2. Register Voter");
            System.out.println("3. Cast Vote");
            System.out.println("4. View Results");
            System.out.println("5. Exit");

            System.out.print("Enter your choice: ");
            String choiceInput = input.nextLine();

            if (!isNumeric(choiceInput)) {
                System.out.println("Invalid input! Please enter a number between 1 and 5.");
                continue;
            }

            int choice = Integer.parseInt(choiceInput);

            if (choice < 1 || choice > 5) {
                System.out.println("Invalid choice. Enter a number between 1 and 5.");
                continue;
            }

            switch (choice) {
                case 1:
                    registerCandidate(input);
                    break;
                case 2:
                    registerVoter(input);
                    break;
                case 3:
                    castVote(input);
                    break;
                case 4:
                    viewResults();
                    break;
                case 5:
                    System.out.println("Exiting........!");
                    System.exit(0);
                    break;
            }
        }
    }

    public static void registerCandidate(Scanner scanner) {
        System.out.print("Enter candidate Party name: ");
        String name = scanner.nextLine();

        if (candidates.contains(name)) {
            System.out.println("Candidate already registered.");
        } else {
            candidates.add(name);
            System.out.println("Candidate registered successfully.");
        }
    }

    public static void registerVoter(Scanner scanner) {
    	 System.out.print("Enter voter age: ");
        int age = scanner.nextInt();
	if(age < 18){
		System.out.print("Sorry Not up to voting age");
		}
	else{System.out.print("Welcome, you are up to voting age");
	}
        System.out.print("Enter voter name: ");
        String name = scanner.nextLine();
         System.out.print("Enter voter LGA: ");
        String nameLGA = scanner.nextLine();
	
	        if (voters.contains(name)) {
            System.out.println("Voter already registered.");
         } else {
            voters.add(name);
            System.out.println("Voter registered successfully.");
            
        }
    }

    public static void castVote(Scanner scanner) {
        if (voters.isEmpty() || candidates.isEmpty()) {
            System.out.println("No voters or candidates registered.");
            return;
        }

        System.out.print("Enter your voter name: ");
        String voterName = scanner.nextLine();

        if (!voters.contains(voterName)) {
            System.out.println("You are not registered as a voter.");
            return;
        }

        if (votedVoters.contains(voterName)) {
            System.out.println("You have already voted.");
            return;
        }

        System.out.println("Candidates:");
        for (int index = 0; index < candidates.size(); index++) {
            System.out.println((index + 1) + ". " + candidates.get(index));
        }

        System.out.print("Enter the number of the candidate you want to vote for: ");
        String voteInput = scanner.nextLine();

        if (!isNumeric(voteInput)) {
            System.out.println("Invalid input! You must enter a number.");
            return;
        }

        int choice = Integer.parseInt(voteInput);

        if (choice > 0 && choice <= candidates.size()) {
            String candidate = candidates.get(choice - 1);
            votes.add(candidate);
            votedVoters.add(voterName);
            System.out.println("Vote cast successfully for " + candidate);
        } else {
            System.out.println("Invalid candidate number.");
        }
    }

    public static void viewResults() {
        if (votes.isEmpty()) {
            System.out.println("No votes cast yet.");
            return;
        }

        System.out.println("\nElection Results:");
        for (String candidate : candidates) {
            int count = 0;
            for (String vote : votes) {
                if (vote.equals(candidate)) {
                    count++;
                }
            }
            System.out.println(candidate + ": " + count + " vote(s)");
        }
    }

   public static boolean isNumeric(String input) {
        if (input == null || input.isEmpty()) return false;

        for (char value : input.toCharArray()) {
            if (!Character.isDigit(value)) return false;
        }

        return true;
    }
}