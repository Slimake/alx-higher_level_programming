#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        if not name.startswith("__"):
            print("{0}".format(name))
    print(dir(hidden_4))
