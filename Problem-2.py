# Problem-2.py
# Language: Python 3
# Generate first 'a' odd numbers (for input a)

def generate_odds(a: int):
    # returns list of first a odd numbers
    return [2*i + 1 for i in range(a)]

def main():
    s = input("Enter a (positive integer): ").strip()
    try:
        a = int(s)
        if a < 0:
            print("Please enter a non-negative integer.")
            return
        result = generate_odds(a)
        print(", ".join(map(str, result)))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()