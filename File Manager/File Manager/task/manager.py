import os
os.chdir('module/root_folder')


cmd = input('Input the command: ')
cmd = cmd.strip()

while cmd != 'quit':
    try:
        if cmd == 'pwd':
            print(os.getcwd())

        elif cmd == 'cd ..':
            os.chdir('..')
            print(os.getcwd())

        elif cmd.startswith('cd '):
            os.chdir(cmd[3:])
            print(os.getcwd())
        else:
            print('Invalid command')

    except Exception as e:
        print(e)

    cmd = input()
    cmd = cmd.strip()
