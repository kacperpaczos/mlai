from c45 import c45

# Tworzenie instancji klasy c45
c45_instance = c45()

# Przykładowe dane
data_uniform = [1, 1, 1, 1, 1, 1]
data_balanced = [1, 2, 1, 2, 1, 2]
data_unbalanced = [1, 1, 1, 1, 2, 3]
data_all_unique = [1, 2, 3, 4, 5, 6]
data_empty = []
data_single_value = [1]
data_two_values = [1, 2]
data_with_zeros = [0, 0, 0, 1, 1, 1]

# Obliczanie entropii przy użyciu c45 dla różnych przypadków
result_uniform = c45_instance.entropy(data_uniform, base=2)
result_balanced = c45_instance.entropy(data_balanced, base=2)
result_unbalanced = c45_instance.entropy(data_unbalanced, base=2)
result_all_unique = c45_instance.entropy(data_all_unique, base=2)
result_empty = c45_instance.entropy(data_empty, base=2) if data_empty else 0
result_single_value = c45_instance.entropy(data_single_value, base=2) if len(data_single_value) > 1 else 0
result_two_values = c45_instance.entropy(data_two_values, base=2)
result_with_zeros = c45_instance.entropy(data_with_zeros, base=2)

# Wyświetlanie wyników
print(f"Entropia danych jednolitych: {result_uniform}")
print(f"Entropia danych zbalansowanych: {result_balanced}")
print(f"Entropia danych niezbalansowanych: {result_unbalanced}")
print(f"Entropia danych z unikalnymi wartościami: {result_all_unique}")
print(f"Entropia pustych danych: {result_empty}")
print(f"Entropia danych z pojedynczą wartością: {result_single_value}")
print(f"Entropia danych z dwoma wartościami: {result_two_values}")
print(f"Entropia danych z zerami: {result_with_zeros}")



