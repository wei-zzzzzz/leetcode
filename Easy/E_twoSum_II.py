'''
Two Sum II - Input array is sorted
2020_11_6
Time: O(n)
Space: O(n)
'''
class Solution:
    '''
    def BS(self, ary, target, head , tail):
        while tail >= head:
            mid = (tail + head) // 2
            if ary[mid] == target: 
                return mid
            elif ary[mid] < target:
                head = mid + 1
            else:
                tail = mid - 1
        return -1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ret =[]
        for i in range(len(numbers)):
            rem = target - numbers[i]
            index = self.BS(numbers, rem, i+1, len(numbers)-1)
            if index != -1:
                ret.append(i+1)
                ret.append(index+1)
                return ret
        return ret
    '''            
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        location = {}
        for index, item in enumerate(numbers,1):
            temp = target - item
            #if location.get(temp):
            if temp in location:
                return [location[temp], index]
            else:
                location[item] = index
    
