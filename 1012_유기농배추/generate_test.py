import os
from itertools import product

def make_test(i, j):
    test = "1"
    test += f"\n{i} {j} {i*j}"
    for x, y in product(range(i), range(j)):
        test += f"\n{x} {y}"
    test += "\n"

    return test

def save_test(i, j, test, test_dir):
    print(test)
    with open(f"{test_dir}/{i}_{j}.txt", "w") as f:
        f.write(test)

def main():
    current_py_path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(f"{current_py_path}/test"):
        os.mkdir(f"{current_py_path}/test")
    test_dir = f"{current_py_path}/test"

    for i, j in product(range(47, 51), range(47, 51)):
        test = make_test(i, j)
        save_test(i, j, test, test_dir)

if __name__ == "__main__":
    main()