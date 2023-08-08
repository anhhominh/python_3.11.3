
class Solution {
  int findPoisonedDuration(List<int> timeSeries, int duration) {
    var result = 0;
    for (var i = 1; i < timeSeries.length; i++) {
      result += min(timeSeries[i] - timeSeries[i-1], duration);
    }
    if (timeSeries.isNotEmpty) {
      result += duration;
    }
    return result;
  }
}