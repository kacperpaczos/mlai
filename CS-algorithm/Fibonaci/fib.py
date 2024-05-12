import time

def fibonacci_rekurencyjnie(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rekurencyjnie(n-1) + fibonacci_rekurencyjnie(n-2)

def fibonacci_rekurencyjnie_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci_rekurencyjnie_memo(n-1, memo) + fibonacci_rekurencyjnie_memo(n-2, memo)
        return memo[n]


def fibonacci_iteracyjnie(n):
    if n <= 1:
        return n
    poprzednia_liczba, obecna_liczba = 0, 1
    for _ in range(2, n+1):
        poprzednia_liczba, obecna_liczba = obecna_liczba, poprzednia_liczba + obecna_liczba
    return obecna_liczba

import matplotlib.pyplot as plt

# Testowanie czasu wykonania dla różnych wartości n używając funkcji rekurencyjnej
test_values_rekurencyjnie = [35, 40, 45, 50]
times_rekurencyjnie = []
for val in test_values_rekurencyjnie:
    start_time = time.time()
    result = fibonacci_rekurencyjnie(val)
    end_time = time.time()
    execution_time = end_time - start_time
    times_rekurencyjnie.append(execution_time)
    print(f"Fibonacci rekurencyjnie({val}) = {result}, czas wykonania: {execution_time:.6f} sekund")

# Testowanie czasu wykonania dla różnych wartości n używając funkcji rekurencyjnej z memoizacją
test_values_rekurencyjnie_memo = [35, 40, 45, 50]
times_rekurencyjnie_memo = []
for val in test_values_rekurencyjnie_memo:
    start_time = time.time()
    result = fibonacci_rekurencyjnie_memo(val)
    end_time = time.time()
    execution_time = end_time - start_time
    times_rekurencyjnie_memo.append(execution_time)
    print(f"Fibonacci rekurencyjnie z memoizacją({val}) = {result}, czas wykonania: {execution_time:.6f} sekund")

# Testowanie czasu wykonania dla różnych wartości n używając funkcji iteracyjnej
test_values_iteracyjnie = [35, 40, 45, 50]
times_iteracyjnie = []
for val in test_values_iteracyjnie:
    start_time = time.time()
    result = fibonacci_iteracyjnie(val)
    end_time = time.time()
    execution_time = end_time - start_time
    times_iteracyjnie.append(execution_time)
    print(f"Fibonacci iteracyjnie({val}) = {result}, czas wykonania: {execution_time:.6f} sekund")

# Rysowanie wykresu
plt.figure(figsize=(10, 5))
plt.plot(test_values_rekurencyjnie, times_rekurencyjnie, label='Rekurencyjnie', marker='o')
plt.plot(test_values_rekurencyjnie_memo, times_rekurencyjnie_memo, label='Rekurencyjnie z memoizacją', marker='o')
plt.plot(test_values_iteracyjnie, times_iteracyjnie, label='Iteracyjnie', marker='o')
plt.xlabel('Wartość n')
plt.ylabel('Czas wykonania (sekundy)')
plt.title('Porównanie czasu wykonania funkcji Fibonacci')
plt.legend()
plt.grid(True)
plt.show()

