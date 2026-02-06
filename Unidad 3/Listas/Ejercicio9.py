n = int(input("Introduce un número entero mayor que 2: "))
primes = set(range(2, n + 1))
numbers = list(range(2, n + 1))
multiples = [True for x in range(len(numbers))]

for i in range(len(numbers)):
  if multiples[i] == False:
    continue
  for j in range(i + 1, len(numbers)):
    if numbers[j] % numbers[i] == 0:
      multiples[j] = False
      primes.discard(numbers[j])

print(primes)