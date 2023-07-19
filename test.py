from databases import create_table_user, insert_user

data = dict(
    first_name = input("Enter your first name: "),
    last_name = input("Enter your last name: "),
    email = input("Enter your email: "),
    username = input("Enter your username: "),
    password1 = input("Enter your password: "),
    password2 = input("Password confirm: ")
)

response = insert_user(data)
if response == 201:
    print('OK')

if __name__ == '__main__':
    create_table_user()