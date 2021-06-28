import sys


def say_hello(name):
    print(f"H, {name}!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.arv[1]
    else:
        name = "awesome people of the Hack Week"

    say_hello(name)
