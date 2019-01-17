import random
import re

n = (random.randint(0, 9) for i in range(2500)) 
str_number = ''.join(str(i) for i in n) 
with open('test.txt', 'w', )  as f: 
    f.write(str_number)
    f.close()

result = re.findall(r"0{2,}|1{2,}|2{2,}|3{2,}|4{2,}|5{2,}|6{2,}|7{2,}|8{2,}|9{2,}|^\D", str_number)

len_rezult = [len(result[i]) for i in range (len(result))]
maximum = max(len_rezult)
ind=len_rezult.index(maximum)
print("Максимальная последовательность", result[ind])
