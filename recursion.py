def get_add(n):
    if n==0:
        return 1
    else:
        return n*get_add(n-1)
user_num = int(input("Enter a number: "))
result = get_add(user_num)
print(f'The final result is: {result}')