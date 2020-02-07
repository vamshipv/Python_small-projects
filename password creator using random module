import random
import string

truepass = 0


print("enter your name")
username = str(input())
print("welcome", username)

print("how may char passsword")
passwordd = int(input())
print("your %d char password is" % (passwordd))

alphalower = string.ascii_lowercase
alphahigher = string.ascii_uppercase
numbers = string.digits
symbols = string.hexdigits

password = alphahigher + alphalower + numbers + symbols

randl = random.choice(alphalower)
rand2 = random.choice(alphahigher)
rand3 = random.choice(numbers)
rand4 = random.choice(symbols)

temppass = randl + rand2 + rand3 + rand4


for i in range(passwordd - 4):

    temppass = temppass + random.choice(password)
apassword = ""
for i in temppass:
    apassword += i

print(apassword)

