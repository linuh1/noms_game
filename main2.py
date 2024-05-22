def define_players():
    res = {}
    for player_num in range(1, 7):
        res[player_num] = input(f'Игрок № {player_num}, введите Ваше имя: ')
        if 2 <= player_num < 6:
            command = command_input('Добавить игрока', 'Закончить набор игроков')
            if command == '2':
                break
    return res

def play_mushroom():
    if input('1 - Защитить своего Нома\n'
             '2 - Удалить гриб игрока')


def choose_player_to_action():
    input()

def command_input(*args):
    commands = ''
    for num in range(1, len(args)+1):
        commands.join(str(num))
    for command_num, command in enumerate(args, 1):
        print(f'{command_num} - {command}')
    while True:
        command = input('Введите команду: ')
        if command in commands:
            break
        else:
            print('Введите корректную команду.')
        return command

deck = {''}

players = define_players()