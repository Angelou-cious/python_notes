def tabular(names, scores):

    print(f"{'Name':<20} {'Score'}")
    print(f"-" * 30)


    for name, score in zip(names, scores):
        print(f'{name:<20} {score}')


names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

tabular(names, scores)