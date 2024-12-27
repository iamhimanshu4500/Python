candidates = ["Alice", "Bob", "Charlie"]
vote_counts = {candidate: 0 for candidate in candidates}

def cast_vote():
    print("Candidates: ")
    for i, candidate in enumerate(candidates, 1):
        print(f"{i}. {candidate}")
    
    choice = int(input("Enter the number of the candidate you want to vote for: "))
    if 1 <= choice <= len(candidates):
        selected_candidate = candidates[choice - 1]
        vote_counts[selected_candidate] += 1
        print(f"Vote casted for {selected_candidate}")
    else:
        print("Invalid choice. Please try again.")

def show_results():
    print("\nCurrent Vote Counts:")
    for candidate, votes in vote_counts.items():
        print(f"{candidate}: {votes} votes")

def main():
    while True:
        print("\n1. Cast Vote")
        print("2. Show Results")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            cast_vote()
        elif choice == 2:
            show_results()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
