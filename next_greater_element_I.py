class Solution {
  List<int> nextGreaterElement(List<int> nums1, List<int> nums2) {
      List<int> greaterElements=[];
      for(int i=0;i<nums1.length;i++){
          greaterElements.add(greater(nums1[i],nums2));
      }
      return greaterElements;
      }
      int greater (int n,List<int> list){
          for(int i=list.indexOf(n);i<list.length;i++){
              if(n<list[i])return list[i];
      }
    return -1;
  }
}