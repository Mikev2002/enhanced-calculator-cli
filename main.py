from app.calculator import Calculator

def main():
    calc = Calculator()
    print("🧮 Enhanced Calculator CLI. Type 'help' for commands.")

    while True:
        command = input("> ").strip().lower()
        if not command:
            continue

        if command == "exit":
            print("Goodbye!")
            break

        elif command == "help":
            print("""
Available commands:
  add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
  history         - Show calculation history
  undo            - Undo last calculation
  redo            - Redo last undone calculation
  clear           - Clear history
  exit            - Exit the calculator
""")
        elif command == "history":
            history = calc.get_history()
            if not history:
                print("No history yet.")
            for item in history:
                print(item.to_dict())

        elif command == "undo":
            calc.undo()
            print("Undo performed.")

        elif command == "redo":
            calc.redo()
            print("Redo performed.")

        elif command == "clear":
            calc.clear_history()
            print("History cleared.")

        else:
            # Parse operation and operands
            parts = command.split()
            if len(parts) != 3:
                print("Invalid command format. Example: add 5 2")
                continue

            op_name, a_str, b_str = parts
            try:
                a = float(a_str)
                b = float(b_str)
                result = calc.calculate(op_name, a, b)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
            except ZeroDivisionError as e:
                print(f"Math Error: {e}")
            except Exception as e:
                print(f"Unhandled Error: {e}")

if __name__ == "__main__":
    main()
