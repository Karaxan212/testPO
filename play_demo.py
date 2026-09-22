from Games import check_guess, validate_input


def run_demo():
    target = 25
    demo_inputs = ["10", "40", " 25 ", "abc", "3.14", ""]

    print(f"Target number: {target}\n")

    for inp in demo_inputs:
        print(f"Input: {repr(inp)} -> ", end="")
        try:
            val = validate_input(inp)
        except ValueError as e:
            print(f"Validation error: {e}")
            continue

        result = check_guess(target, val)
        print(f"Guess {val}: {result}")


if __name__ == "__main__":
    run_demo()
