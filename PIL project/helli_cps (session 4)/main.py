import functions
import settings
from PIL import Image, ImageOps

done = False
print(settings.MAIN_MENU)
import easygui


def input_first_part (): #by Arad Nejati
    a=easygui.enterbox("please enter your image's address","input location")
    return a

def export_checking(): #by Arad Nejati
    a=easygui.enterbox("please enter your image's name to export","export location")
    return a
def edit_type(): #by AmirReza Ardeshiri
    Selected_effect=easygui.buttonbox("Please select your effect","effect",("black_and_white","grayscale","blur","negative","resize","brownstyle","cmyk","rotate"))
    return Selected_effect

better_code_a=input_first_part() #by kardel
edit = edit_type() #By AmirParsa Rouhani
export = export_checking() #By AmirParsa Rouhani
better_code = functions.code_reader(better_code_a, edit, export) #By AmirParsa Rouhani

while not done:
    finish = functions.insert_checker(better_code)
    if finish == True:
        done = True
    else:
        code = input()

