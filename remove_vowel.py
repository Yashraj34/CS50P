def main():
    x=input("Input: ")
    print("Output: ",remove_vowels(x))

def remove_vowels(x):
    vowels="aeiouAEIOU"
    result=""

    for char in x:
        if char not in vowels:
            result+=char

    return result
main()
    