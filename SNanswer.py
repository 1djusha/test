# python 3
# simple password manager
import sys, pyperclip

password = {
    'de': 'Запрос отправлен в немецкую поддержку',
    'wh': 'напишите, пожалуйста, мне в Jabber, когда вам будет удобно, чтобы я подключилась для решения пробелмы',
    'o3': 'для активации лицензии Office 365 введите mariia.afanaseva@t-systems.ru и пароль как от компьютера',
    'pa': 'права ЛА предоставлены. нужно перезагрузить компьютер, выполнить в командной строке gpupdate /force и еще раз перезагрузить компьютер',
    'op': 'порты открыты. нужно перезагрузить компьютер, выполнить в командной строке gpupdate /force и еще раз перезагрузить компьютер',
    'he': 'уточните, пожалуйста, требуется ли еще помощь в рамках данного тикета?'
    }

if len(sys.argv) < 2:
    print('Please use format: hello.py [login]')
    sys.exit()

login = sys.argv[1]

if login in password.keys():
    pyperclip.copy(password[login])
    print('Answer was coppyed to buffer.')
else:
    print("Entry for this login doesn\'t exist.")
