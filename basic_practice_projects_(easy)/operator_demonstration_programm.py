num1 = 20
num2 = 10

#Arithmetic Operations
print(f"Addition : {num1 + num2}")
print(f"Subtraction : {num1 - num2}")
print(f"Multiplication : {num1 * num2}")
print(f"Division : {num1 / num2}")
print(f"Floor Division : {num1 // num2}")
print(f"Modulo : {num1 % num2}")
print(f"Power : {num1 ** num2}")

#Assigment Operator
num1+=num2
print(f"num1 += num2: {num1 }")
num1 -= num2
print(f"num1 -= num2 : {num1}")
num1 *= num2
print(f"num1 *= num2 : {num1}")
num1 /= num2
print(f"num1 /= num2 :{num1}")
num1 //= num2
print(f"num1 //= num2 :{num1}")
num1 %= num2 
print(f"num1 %= num2 :{num1}")
num1 **= num2
print(f"num1 **= num2 : {num1}")

#Comparison Operator
print(f"num1>num2 :{num1>num2}")
print(f"num1>=num2 :{num1>=num2}")
print(f"num1<num2 :{num1<num2}")
print(f"num1<=num2 :{num1<=num2}")
print(f"num1==num2 :{num1==num2}")

#Logical Operator
print(num1)
print(num2)
print(f"num1 and num2 :{num1 and num2}")
print(f"num1 and num2 :{num1 or num2}")

a = 20
b = 20
print(f"id of a is :{id(a)}")
print(f"id of b is :{id(b)}")
print(f"a is b :{a is b}")
print(f"a is not b :{a is not b}")


str1 = "a quick brown fox jump over a lazy dog"
print(f"fox in str1 : {"fox" in str1}")
print(f"table not in str1 : {"table" not in str1}")

num3 = 23 & 28
print(f"23 & 28 : {num3}")

num3 = 23 | 28
print(f"23 | 28 : {num3}")

num3 = 23 ^ 28
print(f"23 ^ 28 : {num3}")

print(f"23<<3 : {23 << 3}")
print(f"23 >> 3 : {23 >> 3}")