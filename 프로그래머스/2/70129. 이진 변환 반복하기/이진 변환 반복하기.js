function solution(s) {
  var totalZeroCount = 0;
  var loopCount = 0;
  while (s != "1") {
    loopCount++;
    var zeroCount = 0;
    for (var i = 0; i < s.length; i++) s[i] == "0" ? zeroCount++ : 0;
    totalZeroCount += zeroCount;
    var newNumber = s.length - zeroCount;
    s = "";
    while (newNumber > 1) {
    //   console.log(newNumber, s);
      if (newNumber % 2) {
        s = "1" + s;
      } else {
        s = "0" + s;
      }
      newNumber = Math.floor(newNumber / 2);
    }
    s = "1" + s;
    // console.log(s, loopCount, totalZeroCount);
  }
  return [loopCount, totalZeroCount];
}