def main():
    names = ["Sam", "Hunter", "Julien", "Dirk"]
    ages = [20, 21, 20, 19]
    oldest_person = get_oldest_person(names, ages)
    print(oldest_person)


def get_oldest_person(names, ages):
    oldest_age = max(ages)
    index = 0
    age = ages[index]
    while age != oldest_age:
        index += 1
        age = ages[index]
    oldest_person = names[index]
    return oldest_person


main()
