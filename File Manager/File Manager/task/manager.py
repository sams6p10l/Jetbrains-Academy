import os
import shutil
os.chdir('module/root_folder')

while True:
    cmd = input().strip()
    if cmd == 'quit':
        break

    try:
        if cmd == 'pwd':
            print(os.getcwd())

        elif cmd.startswith('rm'):
            path = cmd[3:]
            if path == '':
                print('Specify the file or directory')
                continue

            if "." in path:
                os.remove(path)
            else:
                shutil.rmtree(path)

        elif cmd.startswith('cp'):
            arguments = cmd[3:]
            arguments = arguments.split(' ')
            if len(arguments) == 2:
                source, destination = arguments
                if source not in os.listdir():
                    print('No such file or directory')
                elif os.path.isdir(destination):
                    if source in os.listdir(destination):
                        print(f'{source} already exists in this directory')
                    else:
                        shutil.copy2(source, destination)
                else:
                    shutil.copy2(source, destination)
            elif len(arguments) > 2:
                print('Specify the current name of the file or directory and the new location and/or name')
            else:
                print('Specify the file')

        elif cmd.startswith('mv'):
            arguments = cmd[3:]
            arguments = arguments.split(' ')
            if len(arguments) == 2:
                first, second = arguments
                if first not in os.listdir():
                    print('No such file or directory')
                    continue
                elif os.path.isdir(second):
                    if first in os.listdir(second):
                        print(f'The file or directory already exists')
                    else:
                        shutil.move(first, second)
                        continue
                elif second in os.listdir():
                    print('The file or directory already exists2')
                else:
                    shutil.move(first, second)
            else:
                print('Specify the current name of the file or directory and the new location and/or name')

        elif cmd.startswith('mkdir'):
            path = cmd[6:]
            if path == '':
                print('Specify the name of the directory to be made')
            if path in os.listdir():
                print('The directory already exists')
            else:
                os.mkdir(path)

        elif cmd == 'ls':
            entries = os.listdir()
            directories = sorted([entry for entry in entries if os.path.isdir(entry)])
            files = sorted([entry for entry in entries if os.path.isfile(entry)])

            print(f'{len(directories)} directories and {len(files)} files')
            print('\n'.join(directories + files))

        elif cmd == 'ls -l':
            for file in os.listdir():
                print(f'{file} {os.stat(file).st_size}')

        elif cmd == 'ls -lh':
            for file in os.listdir():
                size = os.stat(file).st_size
                if size < 1024:
                    print(f'{file} {size}B')
                elif size < 1024 * 1024:
                    print(f'{file} {size // 1024}KB')
                elif size < 1024 * 1024 * 1024:
                    print(f'{file} {size // 1024 // 1024}MB')
                elif size < 1024 * 1024 * 1024 * 1024:
                    print(f'{file} {size // 1024 // 1024 // 1024}GB')

        elif cmd == 'cd ..':
            os.chdir('..')
            print(os.getcwd())

        elif cmd.startswith('cd '):
            os.chdir(cmd[3:])
            print(os.getcwd())
        else:
            print('Invalid command')

    except FileNotFoundError:
        print('No such file or directory')
    except Exception as e:
        print(e)
