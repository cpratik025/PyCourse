import requests
import hashlib
import sys


def request_api(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error Fatching {response.status_code},check the api and try again')
    return response

def get_password_leak_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_Api(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    five_char,tail=sha1_password[:5],sha1_password[5:]
    response2 = request_api(five_char)
    return get_password_leak_count(response2,tail)

def main(args):
    for password in args:
        count = pwned_Api(password)
        if int(count) > 10:
            print(f'{password} was found {count} times. You should consider changing your password')
        else:
            print(f'{password} is found {count} time only please carry on')
    return 'done'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
