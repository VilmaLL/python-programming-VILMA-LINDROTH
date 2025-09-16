Sequence = input("sequence of characters: ")
CleanedSequence = Sequence.replace(" ", "").lower()

if CleanedSequence == CleanedSequence[::-1]:
    print(f"The sequence \"{Sequence}\" is a palindrome.")
else:
    print(f"The sequence \"{Sequence}\" is not a palindrome.")