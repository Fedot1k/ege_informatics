def dels_(num): # функция нахождения делителей (быстрее перебора в 555 раз)
    d = [1, num]
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            d.append(i)
            d.append(num // i)
    return list(set(d))

def is_prime(num): # функция простого числа
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

