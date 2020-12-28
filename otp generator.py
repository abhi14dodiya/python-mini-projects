import random
import math

data = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
leng =len(data)

otp = ""

for i in range(4):
    otp += data[math.floor(random.random()*leng)]

print("your otp is ",otp)
