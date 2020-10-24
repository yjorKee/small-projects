SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def factorial(number):
    answer = 1
    for num in range(1, number+1):
        answer *= num
    return answer


def n_choose_k(n, k):
    n_factorial = factorial(n)
    k_factorial = factorial(k)
    n_minus_k = n - k
    n_minus_k_factorial = factorial(n_minus_k)
    answer = n_factorial / (k_factorial * n_minus_k_factorial)
    return answer


def binomial_theorem(power):
    k = 0
    while k < power:
        choose_term = int(n_choose_k(power, k))
        n_minus_k = power - k

        if k == 0:
            string = f'a' + f'{n_minus_k}'.translate(SUP)
            print(string, end=' + ')
        elif n_minus_k == 0:
            print(f'b{k}', end=' + ')
        else:
            string = f'{choose_term}' + f'a{n_minus_k}'.translate(SUP) + f'b{k}'.translate(SUP)
            print(f'{string}', end=' + ')

        k = k + 1

    else:
        print(f'b{k}'.translate(SUP))


# Enter the power in n
n = 69
binomial_theorem(n)
