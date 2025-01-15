#Simple Python Script for Vim Practice

# Constants
PI = 3.14159

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return PI * radius ** 2

# Function to print Fibonacci sequence up to n
def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Class to represent a simple counter
class Counter:
    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def __str__(self):
        return f"Current count: {self.count}"


# Main logic
if __name__ == "__main__":
    # Test circle area calculation  	^^
    print("Circle Area Test:")
    try:
        radius = 5
        print(f"Area of circle with radius {radius}: {calculate_circle_area(radius)}")
    except ValueError as e:
        print(e)

    print("\nFibonacci Sequence Test:")
    n = 10
    print(f"First {n} Fibonacci numbers: {fibonacci_sequence(n)}")

    print("\nCounter Test:")
    counter = Counter()
    print(counter)
    counter.increment()
    print(counter)
    counter.decrement()
    print(counter)
    counter.reset()
    print(counter)