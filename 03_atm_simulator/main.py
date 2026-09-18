PIN = "2468"


def authenticate():
    for attempt in range(3):
        if input("Enter PIN: ").strip() == PIN:
            return True
        print(f"Incorrect PIN. Attempts left: {2 - attempt}")
    return False


def read_amount(prompt):
    try:
        amount = float(input(prompt))
    except ValueError:
        print("Enter a valid amount.")
        return None
    if amount <= 0:
        print("Amount must be greater than zero.")
        return None
    return amount


def main():
    if not authenticate():
        print("Card blocked.")
        return

    balance = 1000.0
    history = []
    while True:
        print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. History\n5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            print(f"Balance: ${balance:.2f}")
        elif choice == "2":
            amount = read_amount("Deposit amount: $")
            if amount is not None:
                balance += amount
                history.append(f"Deposit: +${amount:.2f}")
        elif choice == "3":
            amount = read_amount("Withdrawal amount: $")
            if amount is not None:
                if amount > balance:
                    print("Insufficient funds.")
                else:
                    balance -= amount
                    history.append(f"Withdrawal: -${amount:.2f}")
        elif choice == "4":
            print("\n".join(history) if history else "No transactions yet.")
        elif choice == "5":
            print("Thank you for using the ATM.")
            break
        else:
            print("Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
