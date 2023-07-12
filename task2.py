choice = input("hours to minutes or minutes to hours? ")
if choice == "hours to minutes":
    hours = int(input("Enter number of hours: "))
    hours *= 60
    print(hours)
elif choice == "minutes to hours":
    mins = int(input("Enter number of minute: "))
    mins /= 60
    print(mins)
# a program that converts from hours to minutes or minutes to hours depending on the user's choice.