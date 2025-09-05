character = input("Input any letter of the alphabet: ")
if character.isupper():
    print(character, "is an uppercase letter")
elif character.islower():
    print(character, "is a lowercase letter")
else:
    print(character, "is not a letter in the alphabet")