
def print_diamond(side_len):
    """
    Print the diamond whose length of side is side_len
    :param side_len: The length of the diamond side
    :return: None
    """
    for x in list(range(side_len)) + list(reversed(range(side_len - 1))):
        print('{: <{w1}}{:*<{w2}}'.format('', '', w1=side_len - x - 1, w2=x * 2 + 1))


def main():
    """
    Entry function of this program
    - Get the length of diamond side from user
    - Run the print_diamond function
    :return: None
    """
    side_len = int(input("Side length of diamond: "))

    print_diamond(side_len)


if __name__ == "__main__":
    main()
