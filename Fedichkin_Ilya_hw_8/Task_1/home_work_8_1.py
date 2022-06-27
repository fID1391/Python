import re


def email_parse(arg):
    VALID_EMAIL = re.compile((r'^[a-zA-Z0-9_.+-]+'
                              r'@'
                             r'[a-zA-Z0-9-]{3,}\.[a-zA-Z0-9-.]{2,}$'))
    res_dict = {}
    try:
        if VALID_EMAIL.match(arg):
            login, domain = arg.split('@')
            res_dict['username'] = login
            res_dict['domain'] = domain
            return res_dict
        else:
            raise ValueError
    except ValueError:
        return print(f'ValueError: wrong email: {arg}')


if __name__ == '__main__':
    print(email_parse(input('Please enter email: ')))
