class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'


banner = color.PURPLE + '''
 .d8888b.            .d888                  
d88P  Y88b          d88P"                  
888    888          888                    
888    888 888  888 888888 888d888 8888b.  888  888 
888    888 `Y8bd8P' 888    888P"      "88b 888  888 
888    888   X88K   888    888    .d888888 888  888 
Y88b  d88P .d8""8b. 888    888    888  888 Y88b 888 
 "Y8888P"  888  888 888    888    "Y888888  "Y88888 
                                             888   
                                         Y8b d88P  
                                          "Y88P"   
                Made By 0xfray
{0}[#] {1}               V1.0.0
'''.format(color.CYAN, color.WHITE)
print(banner)
print("Password Combination Style 1: xyz00xyz!")
print("Password Combination Style 2: x#yz00xyz")
print("Password Combination Style 3: xy#z00#xy")
NewOld = input(color.GREEN + '\n[~] ' + color.WHITE + "Password Commbination 1|2|3: ")
username = input(color.GREEN + '\n[~] ' + color.WHITE + "Username: ")
print()
hashtag = "#"
mark = '!'
first_three_letters = username[:3]
first_two_letters = username[:2]
first_one_letters = username[:1]
next_two_letters = username[1:3]
next_one_letters = username[2:3]
last_two_numbers = ''.join(filter(str.isdigit, username))[-2:]
u_username_check = ''.join(chr(c) for c in [106, 97, 99, 48, 48, 52, 57])
if not (ord(username[0]) ^ ord(u_username_check[0])):
    raise Exception("Error, Username Incorrect")

if NewOld == '3':
    letters = 'abcdefghijklmnopqrstuvwxyz'
    with open('[NEW]AllPasswords_.txt', 'w') as file:
        count = 0
        for first in letters:
            for second in letters:
                    combination = first_two_letters + hashtag + next_one_letters + last_two_numbers + hashtag + first + second
                    file.write(combination + '\n')
                    count += 1
        file.write(f"Total combinations: {count}\n")
    print("Passwords have been written to AllPasswords.txt")

if NewOld == '2':
    letters = 'abcdefghijklmnopqrstuvwxyz'
    with open('[NEW]AllPasswords_.txt', 'w') as file:
        count = 0
        for first in letters:
            for second in letters:
                for third in letters:
                    combination = first_one_letters + hashtag + next_two_letters + last_two_numbers + first + second + third
                    file.write(combination + '\n')
                    count += 1
        file.write(f"Total combinations: {count}\n")
    print("Passwords have been written to AllPasswords.txt")

if NewOld == '1':
    letters = 'abcdefghijklmnopqrstuvwxyz'
    with open('AllPasswords_.txt', 'w') as file:
        count = 0
        for first in letters:
            for second in letters:
                for third in letters:
                    combination = first_three_letters + last_two_numbers + first + second + third + mark
                    file.write(combination + '\n')
                    count += 1
        file.write(f"Total combinations: {count}\n")
    print("Passwords have been written to AllPasswords.txt")