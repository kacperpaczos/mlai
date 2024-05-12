#include <iostream>
#include <chrono>
#include <unordered_map>

int fibonacci_rekurencyjnie(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci_rekurencyjnie(n - 1) + fibonacci_rekurencyjnie(n - 2);
    }
}

int fibonacci_rekurencyjnie_memo(int n, std::unordered_map<int, int>& memo) {
    if (memo.find(n) != memo.end()) {
        return memo[n];
    }
    if (n <= 1) {
        return n;
    } else {
        memo[n] = fibonacci_rekurencyjnie_memo(n - 1, memo) + fibonacci_rekurencyjnie_memo(n - 2, memo);
        return memo[n];
    }
}

int fibonacci_iteracyjnie(int n) {
    if (n <= 1) return n;
    int poprzednia = 0, obecna = 1, wynik = 0;
    for (int i = 2; i <= n; ++i) {
        wynik = poprzednia + obecna;
        poprzednia = obecna;
        obecna = wynik;
    }
    return wynik;
}

int main() {
    int test_values[] = {35, 40, 45, 50};
    int num_tests = sizeof(test_values) / sizeof(test_values[0]);

    // Testy dla rekurencyjnej wersji Fibonacci
    for (int i = 0; i < num_tests; ++i) {
        int val = test_values[i];
        auto start_time = std::chrono::high_resolution_clock::now();
        int result_rekurencyjnie = fibonacci_rekurencyjnie(val);
        auto end_time = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed_rekurencyjnie = end_time - start_time;
        std::cout << "Fibonacci rekurencyjnie(" << val << ") = " << result_rekurencyjnie << ", czas wykonania: " << elapsed_rekurencyjnie.count() << " sekund" << std::endl;
    }

    // Testy dla rekurencyjnej wersji Fibonacci z memoizacją
    for (int i = 0; i < num_tests; ++i) {
        int val = test_values[i];
        std::unordered_map<int, int> memo;
        auto start_time = std::chrono::high_resolution_clock::now();
        int result_rekurencyjnie_memo = fibonacci_rekurencyjnie_memo(val, memo);
        auto end_time = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed_rekurencyjnie_memo = end_time - start_time;
        std::cout << "Fibonacci rekurencyjnie z memoizacją(" << val << ") = " << result_rekurencyjnie_memo << ", czas wykonania: " << elapsed_rekurencyjnie_memo.count() << " sekund" << std::endl;
    }

    // Testy dla iteracyjnej wersji Fibonacci
    for (int i = 0; i < num_tests; ++i) {
        int val = test_values[i];
        auto start_time = std::chrono::high_resolution_clock::now();
        int result_iteracyjnie = fibonacci_iteracyjnie(val);
        auto end_time = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed_iteracyjnie = end_time - start_time;
        std::cout << "Fibonacci iteracyjnie(" << val << ") = " << result_iteracyjnie << ", czas wykonania: " << elapsed_iteracyjnie.count() << " sekund" << std::endl;
    }

    return 0;
}
