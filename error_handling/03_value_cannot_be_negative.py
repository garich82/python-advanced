class ValueCannotBeNegative(Exception):
    pass


for i in range(5):
    if int(input()) < 0:
        raise ValueCannotBeNegative
