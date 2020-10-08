import functions
import settings
from PIL import Image, ImageOps

done = False
print(settings.MAIN_MENU)
code = input()
if code != "help": #by AmirParsa
    better_code = functions.code_reader(code)
while not done:
    if code != "help": #by AmirParsa
        finish = functions.insert_checker(better_code)
        if finish == True:
            done = True
        else:
            print(settings.MAIN_MENU)
            code = input()
            if code != "help":
                better_code = functions.code_reader(code)
    else: #by AmirParsa
        functions.help_menu() #by AmirParsa
        print(settings.MAIN_MENU) #by AmirParsa
        code = input() #by AmirParsa
        if code != "help": #by AmirParsa
            better_code = functions.code_reader(code) #by AmirParsa

# #by AmirParsa ==> By AmirParsa | #by Sepehr ==> by sepehr | Else from before