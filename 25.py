def dels_(num):
    d = [1, num]
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            d.append(i)
            d.append(num // i)
    return sorted(list(set(d)))

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

print(len(dels_(394450)))
