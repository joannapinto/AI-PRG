
from itertools import permutations

def solve(word1, word2, result):
    letters = set(word1 + word2 + result)
    if len(letters) > 10:
        print("No solutions")
        return

    for perm in permutations(range(10), len(letters)):
        assign = dict(zip(letters, perm))
        if any(assign[w[0]] == 0 for w in (word1, word2, result)):
            continue

        num1 = int("".join(str(assign[char]) for char in word1))
        num2 = int("".join(str(assign[char]) for char in word2))
        new_res = int("".join(str(assign[char]) for char in result))

        if num1 + num2 == new_res:
            print(f"{num1} + {num2} = {new_res}, Assignment: {assign}")
            return

    print("No solution found.")

print("CRYPTARITHMETIC PUZZLE SOLVER")
solve(input("Enter the first word: ").upper(), input("Enter the second word: ").upper(), input("Enter the result: ").upper())
