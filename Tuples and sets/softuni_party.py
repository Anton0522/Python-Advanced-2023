n  = int(input())

reservations = set()

for _ in  range(n):
    reservations_num = input()
    reservations.add(reservations_num)

guest_reservations_num = input()

while guest_reservations_num != "END":
    reservations.remove(guest_reservations_num)
    guest_reservations_num = input()

print(len(reservations))
for num in sorted(reservations):
    print(num)
