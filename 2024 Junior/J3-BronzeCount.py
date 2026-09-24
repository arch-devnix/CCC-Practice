def function():

    inputs = sys.stdin.read().split()

    if len(inputs) < 3:

        return

    N = int(inputs[0]) # the amount of scores

    index = 1

    score = [int(i) for i in inputs[1:N+1]]
    sorted_scores = sorted(score, reverse=True)
    unique_sorted_scores = list(dict.fromkeys(sorted_scores))
    third_place = unique_sorted_scores[2]
    
    scores = [i for i in sorted_scores if i == third_place]

    print(f'{third_place} {len(scores)}')
