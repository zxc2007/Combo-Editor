# I'm aware it's a very basic "combo editor", but you could of course add features if you'd like.
# This was just for you to get a look of how it works.
# There is no need to use the regex (Regular Expressions) library.

combos = []
print('Working...')

with open('Input.txt', 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        try:
            combos.append(line.replace('\n', ''))
        except:
            pass

for combo in combos:
    try: # Includes at least 2 non whitespace characters, but removes them.
        email = combo.split(':')[0].split(' ')[1]
        password = combo.split(':')[1].split(' ')[0]

        with open('Output.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{email}:{password}\n')
    
    except:
        try: # Includes non whitespace characters after the password, but removes them.
            email = combo.split(':')[0]
            password = combo.split(':')[1].split(' ')[0]

            with open('Output.txt', 'a', encoding='UTF-8') as f:
                f.write(f'{email}:{password}\n')
        
        except:
            try: # Includes non whitespace characters before the email/username, but removes them.
                email = combo.split(':')[0].split(' ')[1]
                password = combo.split(':')[1]

                with open('Output.txt', 'a', encoding='UTF-8') as f:
                    f.write(f'{email}:{password}\n')

            except: # Clean "combo".
                if ':' in combo:
                    with open('Output.txt', 'a', encoding='UTF-8') as f:
                        f.write(f'{combo}\n')
                else:
                    pass

print('Finished.')
