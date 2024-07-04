// function solution(s: string): string {
//   let answer: string = "";
//   const num_arr: Array<number> = s.split(" ").map(Number);
//   let maxima = num_arr[0];
//   let minima = num_arr[0];
//   for (let i = 0; i < num_arr.length; i++) {
//     if (num_arr[i] > maxima) {
//       maxima = num_arr[i];
//     }
//     if (num_arr[i] < minima) {
//       minima = num_arr[i];
//     }
//   }
//   answer = [minima, maxima].join(" ");
//   return answer;
// }

function solution(s) {
    var answer = "";
    const num_arr = s.split(" ").map(Number);
    let maxima = num_arr[0];
    let minima = num_arr[0];
    for (let i = 0; i < num_arr.length; i++) {
        if (num_arr[i] > maxima) {
            maxima = num_arr[i];
        }
        if (num_arr[i] < minima) {
            minima = num_arr[i];
        }
    }
    answer = [minima, maxima].join(" ");
    return answer;
}
