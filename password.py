import random
letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","o","P","Q","R","S","T","U","V","W","X","Y","Z"]
special_char=["!","@","$","%","^","&","+","(",")"]
n_letters=int(input("Enter how many letters would do like: "))
n_special=int(input("Enter how many special letters do would like: "))
n_number =int(input("enter how many numbers do would like: "))
password=[]
for i in range (1,n_letters+1):
    char = random.choice(letters)
    password +=char

for j in range (1,n_special+1):
    char = random.choice(special_char)
    password +=char
for k in range(1,n_number+1):
    char = random.randint(1,10)
    password +=[char]
random.shuffle(password)
tough_password=""
for char in password:
    tough_password +=str(char)
print("the final generated password is:",  end=" ")
print(tough_password)