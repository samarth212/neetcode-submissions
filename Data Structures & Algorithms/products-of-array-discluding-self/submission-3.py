class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        if len(nums) <= 2:
            return nums[::-1]
        # prefix
        # postfix

        pre = []
        post = []
        output = []
    
        # make pre
        prev_product = 1
        for i in nums:
            pre.append(prev_product * i)
            prev_product = prev_product * i
        
        # make post
        prev_product = 1
        for i in nums[::-1]:
            post.append(prev_product * i)
            prev_product = prev_product * i

        post = post[::-1]
        print(pre, post)

        for i in range(len(nums)):
            if i==0:
                output.append(post[i+1])
            elif i==len(nums)-1:
                output.append(pre[i-1])
            else:
                output.append(pre[i-1] * post[i+1])

        return output






       


        