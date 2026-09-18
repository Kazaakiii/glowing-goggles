def add_student(gradebook):
    name = input("Student name: ").strip().title()
    if not name:
        print("Name cannot be empty.")
        return
    scores = input("Scores separated by spaces: ").split()
    try:
        parsed_scores = [float(score) for score in scores]
    except ValueError:
        print("Scores must be numbers.")
        return
    if not parsed_scores or any(score < 0 or score > 100 for score in parsed_scores):
        print("Enter at least one score from 0 to 100.")
        return
    gradebook[name] = parsed_scores
    print(f"Saved {name}.")


def show_report(gradebook):
    if not gradebook:
        print("No students have been added.")
        return
    results = {name: sum(scores) / len(scores) for name, scores in gradebook.items()}
    print("\nGrade report")
    for name, average in sorted(results.items()):
        print(f"{name}: {average:.2f}%")
    best_name = max(results, key=results.get)
    print(f"Top student: {best_name} ({results[best_name]:.2f}%)")


def main():
    gradebook = {}
    while True:
        print("\n1. Add or replace student\n2. Show report\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_student(gradebook)
        elif choice == "2":
            show_report(gradebook)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
