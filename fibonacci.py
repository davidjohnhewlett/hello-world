import sys


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed: fibonacci(0) == 0, fibonacci(1) == 1)."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    position = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print(f"Fibonacci number at position {position} is {fibonacci(position)}")
