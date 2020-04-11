import requests
import hashlib

def request_api_data(query_char):
    url = ('https://api.pwnedpasswords.com/range/' + query_char)
    result = requests.get(url)
    if result.status_code != 200:
        raise RuntimeError(f'Error fetching: {result.status_code}, check the api URL or the password\n')
    return result

def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hashx, count in hashes:
        print(hashx, count)

def pwned_api_check(password):
    hashpass = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    first_five, tail = hashpass[:5], hashpass[5:]
    response = request_api_data(first_five)
    print(response)
    return get_password_leak_count(response, tail)

pwned_api_check('Hola123!')