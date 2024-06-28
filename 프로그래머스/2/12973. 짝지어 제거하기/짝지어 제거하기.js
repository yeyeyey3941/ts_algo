function solution(s) {
  if (s.length % 2 == 1) {
    return 0;
  }
  const array_s = s.split("");

  var stack = [];
  for (i = 0; i < array_s.length; i++) {
    // console.log(stack);
    if (stack.length !== 0) {
      pop_value = stack[stack.length - 1];
      if (pop_value == array_s[i]) {
        stack.pop();
      } else {
        stack.push(array_s[i]);
      }
    } else {
      stack.push(array_s[i]);
    }
  }
  // console.log(stack);

  return stack.length == 0 ? 1 : 0;
}