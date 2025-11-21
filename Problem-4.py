# Problem-4.py
# Language: Python 3
# Count multiples of 1..9 in the provided list

def count_multiples(numbers):
    counts = {}
    for d in range(1, 10):
        c = sum(1 for num in numbers if num % d == 0)
        counts[d] = c
    return counts

def main():
    s = input("Enter list of integers separated by commas (e.g. 1,2,8,9,12):\n").strip()
    try:
        parts = [p.strip() for p in s.split(',') if p.strip() != ""]
        nums = [int(p) for p in parts]
        counts = count_multiples(nums)
        print(counts)
    except ValueError:
        print("Invalid input. Ensure you enter integers separated by commas.")

if __name__ == "__main__":
    main()