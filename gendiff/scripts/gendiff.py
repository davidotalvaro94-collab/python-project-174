import argparse

from gendiff.scripts.gendiff import *


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")

    args = parser.parse_args()
    

    # Agregamos en paso 4
    diff = generate_diff("file1.json", "file2.json")
    print(diff)


if __name__ == "__main__":
    main()