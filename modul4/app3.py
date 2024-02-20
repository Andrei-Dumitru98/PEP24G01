number_of_participants = int(input("Type the number of the participants: "))
ages = []
for i in range(1, number_of_participants + 1):
    try:
        age = int(input("Type the age of the participant: "))
    except ValueError:
        age = int(input(f"Invalid format of the participant {i}. Type again: "))
    ages.append(age)


def avg(list_of_numbers):
    total = sum(list_of_numbers)
    average_age = total / len(list_of_numbers)
    return average_age


print(avg(ages))