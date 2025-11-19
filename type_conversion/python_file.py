bool('23')  # True
bool('hello')  # True
bool('')  # False

bool(0)  # False
bool(10) # True

x = '23'
y = 5
print(x + y)  # ❌ TypeError
print(int(x) + y)  # 28
print(x + str(y))  # '235'


single_value =2,
print(single_value)  # (2,)  => tuple
a = 1, 2, 3
print(a)  # (1, 2, 3)  => tuple
type(a)   # <class 'tuple'>
a = 1, 2, 3
print(a)  # (1, 2, 3)  => tuple
type(a)   # <class 'tuple'>



# | Feature           | List (`[]`)                              | Tuple (`()`)                            |
# | ----------------- | ---------------------------------------- | --------------------------------------- |
# | Mutable/Immutable | Mutable → change ho sakta hai            | Immutable → change nahi kar sakte       |
# | Syntax            | `[1, 2, 3]`                              | `(1, 2, 3)`                             |
# | Use case          | Jab values change ho sakti hain          | Jab values fixed ho, safety ke liye     |
# | Methods           | `.append()`, `.remove()`, etc. available | Limited methods, e.g., count(), index() |
# | Performance       | Slightly slower than tuple               | Faster than list                        |






# # user_email = int("sanchitraizada@outlook.com") #js k jaise concat nahi karta hai 
# # user_pincode =1231
# # print(user_email +user_pincode) # invalid literal for int() with base 10: 'True' string ko int me conver karne par yeh error ayega

# # number = True
# # print(int(number))   #yeh convert karega boolean ko 1 me 

# # gtvalue = '1' #yeh nahi kar sakta hai 
# # data = 2
# # print(gtvalue+data)

# value = ''
# # print(int(value))
# print(bool(value))
# value1 = '0'
# print(bool(value1))

user_detail = "sanchit","chitansh","sanchit"
print(user_detail[2])
print(type(user_detail))