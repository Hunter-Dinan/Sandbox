ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

input_name = input("Name: ")
input_age = int(input("Age: "))
ages_dict[input_name] = input_age

for name in ages_dict:
    print("{:10} - {:5}".format(name, ages_dict[name]))

for name, age in ages_dict.items():
    print("{:10} - {:5}".format(name, age))
