function solution(arr) {
  var answer = 0;
  var local_sum = 0;
  answer =
    arr.reduce((sum_value, now_value) => {
      sum_value += now_value;
      return sum_value;
    }, local_sum) / arr.length;
  return answer;
}
