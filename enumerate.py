class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()#dict函数返回一个字典,参数为赋值表达式
        for i,num in enumerate(nums):#返回一个迭代器,非常有用,每次返回一个元组,           i为下标索引,num为数组的值
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i#列表下标为i的值作为字典的key,对应value是i
        return []






















"""作者：力扣官方题解
链接：https://leetcode.cn/problems/two-sum/solutions/434597/liang-shu-zhi-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""