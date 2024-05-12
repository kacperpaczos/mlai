function fibonacciRekurencyjny(n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacciRekurencyjny(n - 1) + fibonacciRekurencyjny(n - 2);
    }
}

function fibonacciIteracyjny(n) {
    let a = 0, b = 1, c;
    if (n <= 1) return n;
    for (let i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

function fibonacciMemo(n, memo = {}) {
    if (n in memo) return memo[n];
    if (n <= 1) {
        return n;
    } else {
        memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo);
        return memo[n];
    }
}

// Testowanie czasu wykonania dla funkcji rekurencyjnej
const testValuesRekurencyjny = [35, 40, 45, 50];
testValuesRekurencyjny.forEach(val => {
    const startTimeRekurencyjny = Date.now();
    const resultRekurencyjny = fibonacciRekurencyjny(val);
    const endTimeRekurencyjny = Date.now();
    console.log(`Fibonacci rekurencyjny(${val}) = ${resultRekurencyjny}, czas wykonania: ${endTimeRekurencyjny - startTimeRekurencyjny} milisekund`);
});

// Testowanie czasu wykonania dla funkcji iteracyjnej
const testValuesIteracyjny = [35, 40, 45, 50];
testValuesIteracyjny.forEach(val => {
    const startTimeIteracyjny = Date.now();
    const resultIteracyjny = fibonacciIteracyjny(val);
    const endTimeIteracyjny = Date.now();
    console.log(`Fibonacci iteracyjny(${val}) = ${resultIteracyjny}, czas wykonania: ${endTimeIteracyjny - startTimeIteracyjny} milisekund`);
});

// Testowanie czasu wykonania dla funkcji z memoizacją
const testValuesMemo = [35, 40, 45, 50];
testValuesMemo.forEach(val => {
    const startTimeMemo = Date.now();
    const resultMemo = fibonacciMemo(val);
    const endTimeMemo = Date.now();
    console.log(`Fibonacci z memoizacją(${val}) = ${resultMemo}, czas wykonania: ${endTimeMemo - startTimeMemo} milisekund`);
});

// Testowanie czasu wykonania dla funkcji z memoizacją (druga wersja)
const testValuesMemo2 = [35, 40, 45, 50];
testValuesMemo2.forEach(val => {
    const startTimeMemo2 = Date.now();
    const resultMemo2 = fibonacciMemo2(val);
    const endTimeMemo2 = Date.now();
    console.log(`Fibonacci z memoizacją 2(${val}) = ${resultMemo2}, czas wykonania: ${endTimeMemo2 - startTimeMemo2} milisekund`);
});

