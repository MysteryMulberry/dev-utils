import secrets, string, sys

def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__=='__main__':
    length = int(sys.argv[1]) if len(sys.argv)>1 else 16
    for _ in range(5):
        print(generate_password(length))
