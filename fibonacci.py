import sys


def fibonacci(n):
    """Return the Fibonacci number at position n (0-indexed: F(0)=0, F(1)=1)."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python fibonacci.py <n>")
    try:
        print(fibonacci(int(sys.argv[1])))
    except ValueError as e:
        sys.exit(f"Error: {e}")
