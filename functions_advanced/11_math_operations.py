def math_operations(*args, **kwargs):
    from collections import deque
    numbers = deque([num for num in args])

    a = kwargs["a"]
    s = kwargs["s"]
    d = kwargs["d"]
    m = kwargs["m"]

    while numbers:
        a += numbers.popleft()
        if numbers:
            s -= numbers.popleft()
        if numbers:
            num = numbers.popleft()
            if num != 0:
                d /= num
        if numbers:
            m *= numbers.popleft()

    result = {"a": a, "s": s, "d": d, "m": m}
    sorted_result = {key: value for key, value in sorted(result.items(), key= lambda x: (-x[1], x[0]))}

    return '\n'.join([f"{key}: {value:.1f}" for key, value in sorted_result.items()])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-
2.3), d=0, m=0))
