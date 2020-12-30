class Solution:
  
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        start_index = 0
        end_index = 0
        max_sum = float('-inf')
        curr_sum = 0    
        index_tuple = ()        
        all_negative = True
        
        if len(A)== 0 or (len(A)==1 and A[0]< 0):
            return []
        if len(A) == 1 and A[0] >= 0:
            return A
        
        for i in range(len(A)):
            if A[i] >= 0:
                curr_sum += A[i]
                end_index += 1
                all_negative = False
            else:
                max_sum,index_tuple = self.update_tuple(max_sum,curr_sum,index_tuple,start_index,end_index)
                start_index = i+1
                end_index = i+1
                curr_sum = 0
            
        if all_negative == True:
            return []
        max_sum,index_tuple =self.update_tuple(max_sum,curr_sum,index_tuple,start_index,end_index)
        output = [A[i] for i in range(index_tuple[0],index_tuple[1])]
        return output
    
    def update_tuple(self,max_sum,curr_sum,index_tuple,start_index,end_index):
        if max_sum < curr_sum:
            max_sum = curr_sum
            index_tuple = (start_index,end_index,end_index - start_index +1)
        elif max_sum == curr_sum:
            len_tuple = index_tuple[2]
            curr_len = (end_index- start_index +1)
            if curr_len > len_tuple:
                index_tuple = (start_index,end_index,end_index - start_index +1)
            elif curr_len == len_tuple:
                if A[start_index] < A[index_tuple[0]]:
                    index_tuple = (start_index,end_index,end_index - start_index +1)
        return max_sum, index_tuple
               
            

A = [0]
test = Solution()
print(test.maxSubArray(A))