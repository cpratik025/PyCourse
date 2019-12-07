username = input('Please Enter a Username')
password = input('Please Enter a Password')
pass_len = len(password)
pass_sec= '*'*pass_len

print(f'Hi {username}, the password you selected for you profile {pass_sec} is of length {pass_len}')