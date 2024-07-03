/*
function solution(scoville: Array<number>, K: number): number {
  function heapPush(heap: Array<number>, value: number): void {
    heap.push(value);
    let current_index = heap.length-1;
    while (current_index !== 0) {
      if (heap[current_index] < heap[Math.floor((current_index - 1) / 2)]) {
        [heap[current_index], heap[Math.floor((current_index - 1) / 2)]] = [
          heap[Math.floor((current_index - 1) / 2)],
          heap[current_index],
        ];
        current_index = Math.floor((current_index - 1) / 2);
      } else {
        // current_index = 0; // swap-end
        break;
      }
    }
  }
  function heapPop(heap: Array<number>): number | undefined {
    switch (heap.length) {
      case 0:
        return undefined;
      case 1:
        return heap.pop();
      default:
        const minima = heap[0];
        heap[0] = heap.pop() as number;

        let current_index = 0;
        heapify(heap, 0);
        return minima;
    }
  }
  function heapify(heap, index) {
    let left = index * 2 + 1;
    let right = index * 2 + 2;
    let self = index;
    if (left < heap.length && heap[left] < heap[self]) {
      self = left;
    }
    if (right < heap.length && heap[right] < heap[self]) {
      self = right;
    }
    if (self !== index) {
      [heap[index], heap[self]] = [heap[self], heap[index]];
      heapify(heap, self);
    }
  }

  var heap_list = [];
  for (let i = 0; i < scoville.length; i++) {
    heapPush(heap_list, scoville[i]);
    console.log(heap_list);
  }
  let answer = 0;
  while (heap_list.length > 1) {
    if (heap_list[0] < K) {
      let first = heapPop(heap_list);
      let second = heapPop(heap_list);
      if (first === undefined || second === undefined) {
        break;
      }
      let new_food = first + second * 2;
      heapPush(heap_list, new_food);
      answer++;
    } else {
      return answer;
    }
  }
  if (heap_list[0] < K) {
    return -1;
  }
  return answer;
}
*/

function solution(scoville, K) {
  function heapPush(heap, value) {
    var _a;
    heap.push(value);
    var current_index = heap.length-1;
    while (current_index !== 0) {
      if (heap[current_index] < heap[Math.floor((current_index - 1) / 2)]) {
        (_a = [heap[Math.floor((current_index - 1) / 2)], heap[current_index]]),
          (heap[current_index] = _a[0]),
          (heap[Math.floor((current_index - 1) / 2)] = _a[1]);
          current_index = Math.floor((current_index - 1) / 2);
      } else {
        // current_index = 0; // swap-end
        break;
      }
    }
  }
  function heapPop(heap) {
    switch (heap.length) {
      case 0:
        return undefined;
      case 1:
        return heap.pop();
      default:
        var minima = heap[0];
        heap[0] = heap.pop();
        var current_index = 0;
        heapify(heap, 0);
        return minima;
    }
  }
  function heapify(heap, index) {
    var _a;
    var left = index * 2 + 1;
    var right = index * 2 + 2;
    var self = index;
    if (left < heap.length && heap[left] < heap[self]) {
      self = left;
    }
    if (right < heap.length && heap[right] < heap[self]) {
      self = right;
    }
    if (self !== index) {
      (_a = [heap[self], heap[index]]),
        (heap[index] = _a[0]),
        (heap[self] = _a[1]);
      heapify(heap, self);
    }
  }
  var heap_list = [];
  for (var i = 0; i < scoville.length; i++) {
    heapPush(heap_list, scoville[i]);
    
  }
  var answer = 0;
  while (heap_list.length > 1) {
    if (heap_list[0] < K) {
      var first = heapPop(heap_list);
      var second = heapPop(heap_list);
      if (first === undefined || second === undefined) {
        break;
      }
      var new_food = first + second * 2;
      heapPush(heap_list, new_food);
      answer++;
    } else {
      return answer;
    }
  }
  if (heap_list[0] < K) {
    return -1;
  }
  return answer;
}