class Permutations:
    def __init__(self,in_str):
        self.used = [False for i in range(len(in_str))]
        self.in_str = in_str
        self.out_str = ''
        
    def permute(self):
        if len(self.out_str) == len(self.in_str):
            print(self.out_str)
            return
        for i in range(len(self.in_str)):
            
            if self.used[i]:
                continue
            self.out_str = self.out_str + self.in_str[i]
            self.used[i] = True
            self.permute()
            print("------",i)
            self.used[i] = False
            self.out_str = self.out_str[:-1]

t = Permutations("HID")
t.permute()
                            
