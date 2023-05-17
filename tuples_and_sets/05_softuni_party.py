vips = set()
regulars = set()

for _ in range(int(input())):
    reservation_number = input()
    if reservation_number[0].isdigit():
        vips.add(reservation_number)
    else:
        regulars.add(reservation_number)

guest = input()

while guest != "END":

    if guest[0].isdigit() and guest in vips:
        vips.remove(guest)
    elif guest in regulars:
        regulars.remove(guest)

    guest = input()

print(len(vips) + len(regulars))
if vips:
    print(*sorted(vips), sep="\n")
if regulars:
    print(*sorted(regulars), sep="\n")
