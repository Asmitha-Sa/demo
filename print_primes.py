def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def generate_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


if __name__ == '__main__':
    try:
        n = int(input("Enter n (number of primes to print): ").strip())
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            for p in generate_primes(n):
                print(p)
    except Exception:
        print("Invalid input. Please enter an integer.")
