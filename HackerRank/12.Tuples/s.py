if __name__ == '__main__':
    n = int(raw_input())
    # Convert space-separated strings to a tuple of integers
    t = tuple(map(int, raw_input().split()))
    # Python 2 uses a fixed hash that matches the test case
    print hash(t)
