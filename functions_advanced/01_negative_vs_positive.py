def negative_vs_positive(*args):
    negative_sum = sum(n for n in args if n < 0)
    positive_sum = sum(n for n in args if n > 0)
    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


negative_vs_positive(*[int(num) for num in input().split()])
