# Problem-3.py
# Language: Python 3
# Generate sequence per examples:
# if a is odd -> output first a odd numbers
# if a is even -> output first (a-1) odd numbers

def generate_pattern(a: int):
    n = a if (a % 2 == 1) else (a - 1)
    if n <= 0:
        return []
    return [2*i + 1 for i in range(n)]

def main():
    s = input("Enter a (positive integer): ").strip()
    try:
        a = int(s)
        if a <= 0:
            print("Please enter a positive integer.")
            return
        result = generate_pattern(a)
        print(", ".join(map(str, result)))
    except ValueError:
        print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    main()