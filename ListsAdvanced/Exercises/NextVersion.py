current_version = input().split('.')

num = int(''.join(map(str, current_version)))

new_number = num + 1

new_version = [int(x) for x in str(new_number)]

print(f'{new_version[0]}.{new_version[1]}.{new_version[2]}')

