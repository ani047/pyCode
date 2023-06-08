# import whole file
import one

# import for specific part  like...
from one import mul
a,b = int(input("Enter for a:")),int(input("Enter for b:"))

sum_num = one.sum(a,b)
print(sum_num)

mul_num = one.mul(a,b)
print(mul_num)

mul1 = mul(a,b)
print(mul_num)

