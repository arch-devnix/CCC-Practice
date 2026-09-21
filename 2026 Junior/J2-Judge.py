import sys

def function():
    inputs = sys.stdin.read().splitlines()
    if not inputs or len(inputs) < 6:
        return

    D = int(inputs[5])

    scores = [int(x) for x in inputs[0:5]]

    scores.sort()

    middle_sum = sum(scores[1:4])

    print(middle_sum * D)
