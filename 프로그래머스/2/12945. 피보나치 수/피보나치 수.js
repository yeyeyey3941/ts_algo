function solution(n) {
  const fibo_arr = new Array(n + 1);
  fibo_arr[0] = 0;
  fibo_arr[1] = 1;
  for (let i = 2; i < fibo_arr.length; i++) {
    fibo_arr[i] = (fibo_arr[i - 1] + fibo_arr[i - 2]) % 1234567;
  }
  let answer = fibo_arr[n];
  return answer;
}