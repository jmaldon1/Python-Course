class Solution:
    def twoSum(self, nums, target):
    	for n in nums:
    		print("n = {}".format(n))
    		indexN = nums.index(n)
    		print("indexN = {}".format(indexN))
    		for p in nums[1:]:
    			print("p = {}".format(p))
    			indexP = nums.index(p)
    			print("indexP = {}".format(indexP))
    			if indexP == 0:
    				continue
    			else:
    				if n + p == target:
    					num1 = nums.index(n)
    					num2 = nums.index(p)
    					return [num1,num2]


    twoSum(0,[3, 3], 6)