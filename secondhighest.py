def runner_up(scores):
    sorted_scores = sorted(scores, reverse=True)
    second_max = sorted_scores[1]  
    return second_max
N = int(input("Enter the number of player score: "))
scores = list(input("Enter the scores separated by space: ").strip().split())
if len(scores) != N:
        print("Number of scores provided does not match N.")
second_max = runner_up(scores)
print(f"The runner up is: {second_max}")