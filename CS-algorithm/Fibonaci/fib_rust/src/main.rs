use std::time::Instant;
use std::collections::HashMap;

fn fibonacci_iterative(n: u32) -> u32 {
    let mut a = 0;
    let mut b = 1;
    for _ in 0..n {
        let temp = a;
        a = b;
        b = temp + b;
    }
    a
}

fn fibonacci_recursive(n: u32) -> u32 {
    if n <= 1 {
        n
    } else {
        fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    }
}

fn fibonacci_memo(n: u32, memo: &mut HashMap<u32, u32>) -> u32 {
    if n <= 1 {
        return n;
    }
    if let Some(&value) = memo.get(&n) {
        return value;
    }
    let result = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo);
    memo.insert(n, result);
    result
}

fn main() {
    let test_values = [35, 40, 45, 50];
    for &val in &test_values {
        let start_time = Instant::now();
        let result_iterative = fibonacci_iterative(val);
        let elapsed_iterative = start_time.elapsed();
        println!("Iteracyjna Fibonacci({}) = {}, czas wykonania: {:.2?} sekund", val, result_iterative, elapsed_iterative);

        let start_time = Instant::now();
        let result_recursive = fibonacci_recursive(val);
        let elapsed_recursive = start_time.elapsed();
        println!("Rekurencyjna Fibonacci({}) = {}, czas wykonania: {:.2?} sekund", val, result_recursive, elapsed_recursive);

        let start_time = Instant::now();
        let mut memo = HashMap::new();
        let result_memo = fibonacci_memo(val, &mut memo);
        let elapsed_memo = start_time.elapsed();
        println!("Rekurencyjna z memo Fibonacci({}) = {}, czas wykonania: {:.2?} sekund", val, result_memo, elapsed_memo);
    }
}