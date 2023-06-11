from collections import deque

people = deque()

water_quantity = int(input())
name = input()

while name != "Start":
    people.append(name)


command = input()

while name != "End":
    data = command.split()
    if len(data) == 1:
        littres_wanted =int(data[0])

        if water_quantity >= littres_wanted:
            water_quantity -=littres_wanted
            person = people.popleft()
            print(f"{person} got water")
        else:
            person = people.popleft()
            print(f"{person} must wait")
    else:
        litres_to_fill = int(data[1])
        water_quantity += litres_to_fill

    command = input()

print(f"{water_quantity} litres left")