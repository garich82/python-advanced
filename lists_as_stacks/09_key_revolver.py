from collections import deque

price_bullet = int(input())
barrel_size = int(input())
bullets = [int(bullet) for bullet in input().split()]
locks = deque([int(lock) for lock in input().split()])
intelli_value = int(input())
barrel = barrel_size
used_bullets = 0

while bullets and locks:
    used_bullets += 1
    bullet_size = bullets.pop()
    lock_size = locks.popleft()

    if bullet_size <= lock_size:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock_size)

    barrel -= 1
    if barrel == 0 and bullets:
        barrel = barrel_size
        print("Reloading!")

if not locks:
    money_earned = intelli_value - used_bullets * price_bullet
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
