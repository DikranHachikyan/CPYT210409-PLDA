
if __name__ == '__main__':
    users = ['anna','maria','markus','jane', 'john']
    mails = ['anna@no.com','maria@no.com','markus@no.com','jane@no.com']
    users_dict = {}

    for data in zip(users, mails):
        user, mail = data
        print(f'{user} => {mail}')
        users_dict[user] = mail    
    
    print(users_dict)
    print('--- ---')    