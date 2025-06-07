def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length must be between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3: Only letters and numbers allowed
    if not s.isalnum():
        return False

    # Rule 4 & 5: Numbers, if present, must be at the end and can't start with 0
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False  # first number can't be 0
            if not s[i:].isdigit():
                return False  # numbers must be at the end
            break

    return True


main()
