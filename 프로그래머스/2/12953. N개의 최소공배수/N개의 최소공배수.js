function solution(arr) {
  var answer = 1;
  let prime = new Array(101).fill(1);
  prime[0] = 0;
  prime[1] = 0;
  let prime_set = new Array();
  for (let i = 2; i < prime.length; i++) {
    if (prime[i] !== 0) {
      prime_set.push(i);
      for (let j = i * 2; j < prime.length; j = j + i) {
        prime[j] = 0;
      }
    }
  }
  for (let i = 0; i < prime_set.length; i++) {
    let maxima = 0;
    for (let j = 0; j < arr.length; j++) {
      let temp = count(arr[j], prime_set[i]);
      maxima = maxima > temp ? maxima : temp;
    }
    answer *= Math.pow(prime_set[i], maxima);
    // console.log(prime_set[i], answer);
  }
  return answer;
}
function count(num, prime) {
  let cnt = 0;
  while (num % prime == 0) {
    cnt++;
    num /= prime;
  }
  return cnt;
}