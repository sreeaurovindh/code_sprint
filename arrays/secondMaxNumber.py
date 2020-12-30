 def second_max_element(inp_arr):
     max_buff = [float("-inf"),float("-inf")]
     tot_len = len(inp_arr)
     if tot_len ==0 or tot_len == 1:
         return None
     for item in inp_arr:
         if max_buff[0] > max_buff[1]:
             min_index = 1
         else:
             min_index = 0
         if max_buff[min_index] < item:
             max_buff[min_index] = item
     if max_buff[0] > max_buff[1]:
         return max_buff[1]
     else:
         return max_buff[0]
