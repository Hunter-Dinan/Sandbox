"""Taco Reward Program where users give out tacos to increase their score."""

STARTING_NUMBER_OF_TACOS = 5
POINTS_PER_TACO = 2
MENU = """Type G to give someone a taco
Type S to view scores
Type Q to quit"""


class User:
    def __init__(self, name):
        number_of_tacos = STARTING_NUMBER_OF_TACOS
        score = 0
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def give_taco(self, other_user):
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            self.score += 2
            other_user.number_of_tacos += 1
            other_user.score -= 2
            print("{} gave away a taco to {}".format(self.name, other_user.name))
        else:
            print("{} has no tacos to give.".format(self.name))

    def __str__(self):
        return "{}, {} points, {} tacos left".format(self.name, self.score, self.number_of_tacos)


def main():
    user_1_name = input("Enter User 1 name: ").title()
    user_2_name = input("Enter User 2 name: ").title()
    user_3_name = input("Enter User 3 name: ").title()
    user_1 = User(user_1_name)
    user_2 = User(user_2_name)
    user_3 = User(user_3_name)
    users = [user_1, user_2, user_3]
    print("Taco Reward Program")
    print("Most points wins")
    print("Give away as many tacos as you can to win")

    print(MENU)
    menu_input = input(">>>").upper()
    while menu_input != "Q":
        if menu_input == "G":
            valid_input = False
            while not valid_input:
                print("User list: ")
                for user in users:
                    print(user)
                taco_giver = input("Pick a user to be: ")
                if taco_giver.title() == user_1.name:
                    chosen_user = user_1
                    valid_input = True
                elif taco_giver.title() == user_2.name:
                    chosen_user = user_2
                    valid_input = True
                elif taco_giver.title() == user_3.name:
                    chosen_user = user_3
                    valid_input = True
                else:
                    print("That is not a user, Try again")
            valid_input = False
            while not valid_input:
                print("User list: ")
                for user in users:
                    if user.name != taco_giver.title():
                        print(user)
                taco_receiver = input("Pick a user to give a taco to: ")
                if taco_receiver.title() == taco_giver.title():
                    print("Cannot give yourself a taco.")
                elif taco_receiver.title() == user_1.name:
                    other_user = user_1
                    chosen_user.give_taco(other_user)
                    valid_input = True
                elif taco_receiver.title() == user_2.name:
                    other_user = user_2
                    chosen_user.give_taco(other_user)
                    valid_input = True
                elif taco_receiver.title() == user_3.name:
                    other_user = user_3
                    chosen_user.give_taco(other_user)
                    valid_input = True
                else:
                    print("That is not a user, Try again")
        elif menu_input == "S":
            print("Current Scores:")
            for user in users:
                print(user)
        else:
            print("Invalid input, Try again")
        print()
        print(MENU)
        menu_input = input(">>>").upper()

    print("Program Over")
    print("Final Scores:")
    print(user_1)
    print(user_2)
    print(user_3)


main()
