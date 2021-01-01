from os import listdir, rename, getlogin
from os.path import splitext, join

login = getlogin()
print("""

██████╗ ███████╗      ███╗  ██╗ █████╗ ███╗   ███╗███████╗██████╗
██╔══██╗██╔════╝      ████╗ ██║██╔══██╗████╗ ████║██╔════╝██╔══██╗
██████╔╝█████╗  █████╗██╔██╗██║███████║██╔████╔██║█████╗  ██████╔╝
██╔══██╗██╔══╝  ╚════╝██║╚████║██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║  ██║███████╗      ██║ ╚███║██║  ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝      ╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

                                           ╔╗  ╔╗   ╔══╦══╦══╦═╦═╗
                                    ╔══╦═╗╔╝╠═╗║╚╦╦╗║═╦╣╔╗║╔═╣║║║║
                                    ║║║║╬╚╣╬║╩╣║╬║║║║╔╝║╚╝║╚╗║║║║║
                                    ╚╩╩╩══╩═╩═╝╚═╬╗║╚╝ ╚═╗╠══╩╩═╩╝
                                                 ╚═╝     ╚╝
""")

address = fr"C:\Users\{login}\AppData\Roaming\.vimeworld\minigames\screenshots"

path = input(f"Путь до скриншотов: {address}\n"
             f"Введите адрес, где хранятся скриншоты (Enter, если согласны с адресом выше):")
if path != "":
    address = path
print(f"Выбран путь {address}\n")

try:
    mod = int(input("Выберите формат в которых хотите переделать скриншоты.\n"
                    "1 - из гггг-мм-дд_час_мин_сек в дд.мм.гггг (час:мин:сек)\n"
                    "2 - из дд.мм.гггг (час:мин:сек) в гггг-мм-дд_час_мин_сек\n"
                    "Выбран формат: "))
    if mod == 1:
        try:
            for file_name in listdir(address):
                base_name, ext = splitext(file_name)
                base_name = base_name.split("_")
                base_name[0] = base_name[0].split("-")
                base_name[0][0], base_name[0][2] = base_name[0][2], base_name[0][0]
                base_name[0] = base_name[0][0] + "." + base_name[0][1] + "." + base_name[0][2]
                base_name[1] = base_name[1].split(".")
                base_name[1] = base_name[1][0] + "ч " + base_name[1][1] + "мин " + base_name[1][2] + "сек"
                if len(base_name) == 3:
                    base_name = base_name[0] + " " + base_name[1] + " (" + base_name[2] + ")" + ext
                else:
                    base_name = base_name[0] + " " + base_name[1] + ext
                abs_file_name = str(join(address, file_name))
                new_abs_file_name = str(join(address, base_name))
                rename(abs_file_name, new_abs_file_name)
            input("""
╔============================╗
║Файлы успешно переименованы.║
╚============================╝
""")
        except:
            input("""
╔========================================╗
║Возникла ошибка. Останавливаю программу.║
╚========================================╝
""")
    elif mod == 2:
        try:
            for file_name in listdir(address):
                base_name, ext = splitext(file_name)
                base_name = base_name.split(" ")
                base_name[0] = base_name[0].split(".")
                base_name[0][0], base_name[0][2] = base_name[0][2], base_name[0][0]
                base_name[0] = base_name[0][0] + "-" + base_name[0][1] + "-" + base_name[0][2]
                base_name[1] = base_name[1].replace("ч", "")
                base_name[2] = base_name[2].replace("мин", "")
                base_name[3] = base_name[3].replace("сек", "")
                base_name[1] = base_name[1] + "." + base_name[2] + "." + base_name[3]
                if len(base_name) == 3:
                    base_name = base_name[0] + "_" + base_name[1] + "_" + base_name[4] + "" + ext
                else:
                    base_name = base_name[0] + "_" + base_name[1] + ext
                abs_file_name = str(join(address, file_name))
                new_abs_file_name = str(join(address, base_name))
                rename(abs_file_name, new_abs_file_name)
            input("""
╔============================╗
║Файлы успешно переименованы.║
╚============================╝
""")
        except:
            input("""
╔========================================╗
║Возникла ошибка. Останавливаю программу.║
╚========================================╝
""")
    else:
        input("""
╔=======================================================================╗
║Прости, но ты допустил ошибку в выборе формата. Останавливаю программу.║
╚=======================================================================╝
""")
except:
    input("""
╔=======================================================================╗
║Прости, но ты допустил ошибку в выборе формата. Останавливаю программу.║
╚=======================================================================╝
""")

