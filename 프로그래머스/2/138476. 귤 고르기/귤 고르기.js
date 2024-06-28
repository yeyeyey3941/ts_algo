function solution(k, tangerine) {
  var answer = 0;
  var counter = {};
  // var array = [];
  for (let i = 0; i < tangerine.length; i++) {
    counter.hasOwnProperty(tangerine[i])
      ? counter[tangerine[i]]++
      : (counter[tangerine[i]] = 1);
  }
  // console.log(counter);
  // console.log(Object.keys(counter));
  const array = Object.values(counter);
  array.sort((a, b) => a - b);
  // console.log(array);
  while (k > 0) {
    answer++;
    k -= array.pop();
  }
  return answer;
}