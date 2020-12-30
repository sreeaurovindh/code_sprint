class Solution:
    
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        index_tuple = ()
        max_sum = -1
        curr_sum = 0
        start_ind = 0
        end_ind = 0
        all_zeros = 0
        counted = -1
        # Run for a single element
        if len(A) == 1:
            if A[0] > 0:
                return A
            else:
                return []
        # Run for entire loop
        for i in range(len(A)):
            if A[i] >= 0:
                curr_sum += A[i]
                end_ind += 1
                counted = 0
                all_zeros = 1
            else:
                if all_zeros == 1:
                    index_tuple,max_sum = self.update_max_array(max_sum,curr_sum,start_ind,end_ind,index_tuple)
                start_ind = i +1
                end_ind = i +1
                curr_sum = 0
                
        if all_zeros == 0:
            return []        
        if len(index_tuple) == 0:
            return A
        if counted == 0:
            index_tuple,max_sum = self.update_max_array(max_sum,curr_sum,start_ind,end_ind,index_tuple)
        
            
        output = [A[i] for i in range(index_tuple[0],index_tuple[1])]
        return output
        
    def update_max_array(self,max_sum,curr_sum,start_ind,end_ind,index_tuple):
        
        if max_sum < curr_sum:
            max_sum = curr_sum
            index_tuple = (start_ind,end_ind,(end_ind - start_ind + 1))
            counted =1
        elif max_sum == curr_sum: 
            len_tuple = index_tuple[2]
            curr_len = end_ind - start_ind + 1
            if curr_len > len_tuple:
                index_tuple = (start_ind,end_ind,(end_ind - start_ind +1))
                counted = 1
            elif curr_len == len_tuple:
                if A[start_ind] < A[index_tuple[0]]:
                    index_tuple = (start_ind,end_ind,(end_ind - start_ind +1))
                    counted =1        
        return index_tuple,max_sum        
    

A = [ -81293, -4101, 58248, 82332, 98765, 59002, 20719, 82437 ]
t = Solution()
print(t.maxset(A))