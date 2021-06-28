import sys


def say_hello(name):
    """Print a hello statement to screen."""
    print(f"Hi, {name}!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "awesome people of the Hack Week"

    say_hello(name)
