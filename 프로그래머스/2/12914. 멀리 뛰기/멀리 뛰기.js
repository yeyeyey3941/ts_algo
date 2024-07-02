function solution(n) {
  var answer = 0;
  jumping_count = new Array(n + 1);
  jumping_count[1] = 1;
  jumping_count[2] = 2;
  for (let i = 3; i < jumping_count.length; i++) {
    jumping_count[i] = (jumping_count[i - 1] + jumping_count[i - 2]) % 1234567;
  }
  return jumping_count[n];
}