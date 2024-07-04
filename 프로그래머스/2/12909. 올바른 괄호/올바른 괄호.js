// function solution(s: string): boolean {
//   let answer: boolean;
//   let count = 0;
//   for (let i = 0; s.length; i++) {
//     if (s[i] === "(") {
//       count += 1;
//     } else {
//       count -= 1;
//     }
//     if (count < 0) {
//       return false;
//     }
//   }
//   if (count == 0) answer = true;
//   else answer = false;;
//   return answer;
// }

function solution(s) {
  var answer;
  var count = 0;
  for (var i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      count += 1;
    } else {
      count -= 1;
    }
    if (count < 0) {
      return false;
    }
  }
  if (count == 0) answer = true;
  else answer = false;
  return answer;
}