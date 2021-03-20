VOWELS = "aeiou"

name = input("Name: ")
name_length = len(name)
vowel_count = 0

for char in name:
    if char.lower() in VOWELS:
        vowel_count += 1
print("Out of {} letters, {} has {} vowels".format(name_length, name, vowel_count))
