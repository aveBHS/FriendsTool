import vk_api
from rucaptcha import RuCaptchaConnection, RuCaptcha
from PIL import Image
import urllib.request

def print_green(text, blink):
    if(blink):
        print(f' \033[6m\033[37m\033[42m{text}\033[0m\033[37m\033[40m')
    else:
        print(f' \033[37m\033[42m{text}\033[37m\033[40m')

def print_red(text, blink):
    if(blink):
        print(f' \033[6m\033[37m\033[41m{text}\033[0m\033[37m\033[40m')
    else:
        print(f' \033[37m\033[41m{text}\033[37m\033[40m')

def print_blue(text, blink):
    if(blink):
        print(f'\033[6m\033[37m\033[44m{text}\033[0m\033[37m\033[40m')
    else:
        print(f' \033[37m\033[44m{text}\033[37m\033[40m')

def print_yellow(text, blink):
    if(blink):
        print(f'\033[6m\033[37m\033[43m{text}\033[0m\033[37m\033[40m')
    else:
        print(f' \033[37m\033[43m{text}\033[37m\033[40m')

print('''\033[0m\033[37m\033[40m                 _   _ _____              
     /\         | | (_)  __ \             
    /  \   _ __ | |_ _| |  | | ___   __ _ 
   / /\ \ | '_ \| __| | |  | |/ _ \ / _` |
  / ____ \| | | | |_| | |__| | (_) | (_| |
 /_/    \_\_| |_|\__|_|_____/ \___/ \__, |
                                     __/ |
 \033[37m\033[42m By https://github.com/aveBHS/ \033[0m\033[37m\033[40m   |___/ 
''')


try:
    f = open('./tokens.txt')
    token = f.readline().split('\n')[0]
    rucaptcha_token = f.readline().split('\n')[0]
    f.close()
except:
    token = input(' Введите токен от страницы >> ')
    if(token == ''):
        print_red(' *** ОШИБКА: НЕВАЛИДНЫЙ ТОКЕН *** ', False)
        exit()
    rucaptcha_token = input(' Введите токен от RuCaptcha >> ')
    if(rucaptcha_token == ''):
        print_yellow(' ** Инфо: RuCaptcha использоваться не будет ** ', False)
API = vk_api.VkApi(token=token)
fcount = API.method('friends.get', {})['count']
for i in range(0, int(fcount/300)+1):
    print_blue(f' * Волна зачистки номер {i+1}. Смещение {i*300} * ', False)
    friend = API.method('friends.get', {'offset': i*300})
    q = ''
    for f in friend['items']:
        q += str(f) + ','
    users = API.method('users.get', {'user_ids': q})
    a = []
    i = 0
    while(i < len(users)):
        try:
            if(users[i]['deactivated'] == 'banned' or users[i]['deactivated'] == 'deleted'):
                try:
                    API.method('friends.delete', {'user_id': users[i]['id']})
                    print(' Перенес в подписчики @id' + str(users[i]['id']))
                except vk_api.Captcha as e:
                    if(rucaptcha_token == ''):
                        print_yellow(' ** ВКонтакте просит капчу, но сервис отключен, засыпаю на 10 сек ** ', False)
                        time.sleep(10)
                        continue
                    print_blue(" ** ВКонтакте просит капчу, начинаю решать... ** ")
                    urllib.request.urlretrieve(e.url, f"./{user_id}.jfif")
                    Image.open(f"./{user_id}.jfif").save(f"./{user_id}.png")
                    captcha_compl = connection.send(file=open(f"./{str(user_id)}.png", "rb"))
                    print_green(" Капчу решил, ответ: " + captcha_compl.upper() + " ", False)
                    e.try_again(key=captcha_compl)
                except Except as err:
                    print_red(f' *** ОШИБКА: {err} *** ', True)
                i += 1
            else:
                i += 1
        except:
            i += 1
print_green(f' УСПЕШНО ЗАВЕРШИЛ ЗАЧИСТКУ ', True)
