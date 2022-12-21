def fibonacci(n):
    """
    returns nth sequence of fibonacci series
    """
    # only positive integers accepted
    if n < 0 or not int:
        print("must input a positive integer")
    # first two numbers in sequence are 1
    # base casee
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    # return 1


def lucas(n):
    """
    returns nth sequence of lucas series
    """
    if n < 0 or not int:
        print("must input a positive integer")
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)


def sum_series(n, option1=0, option2=1):
    """
    returns nth sequence of fibonacci series when no option args are passed
    returns nth sequence of lucas series when optional args 2,1 are passed (example args: (n,2,1))
    """
    if n < 0 or not int:
        print("must input a positive integer")
    if n == 0:
        return option1
    if n == 1:
        return option2
    return sum_series(n-1, option1, option2) + sum_series(n-2, option1, option2)
