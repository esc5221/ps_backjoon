import os

# test from txt file
def test_from_txt_file():
    current_py_path = os.path.dirname(os.path.abspath(__file__))
    test_dir = f"{current_py_path}/test"
    for file in os.listdir(test_dir):
        with open(f"{test_dir}/{file}", "r") as f:
            test = f.read()
        yield test

# execute test
def test():
    for test in test_from_txt_file():
        os.system(f"echo '{test}' | python3 1012_유기농배추/1012.py")

if __name__ == "__main__":
    test()
