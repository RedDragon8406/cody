import settings
from PIL import Image, ImageOps , ImageFilter

def help_menu(): #This function by AmirParsa
    print(settings.HELP_MENU)
    help_input = input()
    if help_input == "1":
        full_help()
    elif help_input == "2":
        pass
    else:
        print(settings.help_ERROR)
    return

def full_help(): #This function by AmirParsa
    print(settings.full_help_menu)
    return
def code_reader(code): # from before
    splitted_code = code.split()
    jam = ""
    jam2 = ""
    try:
        for i in range(len(splitted_code[0])):
            if splitted_code[0][i] != '"':
                jam += splitted_code[0][i]
        splitted_code[0] = jam
        for i in range(len(splitted_code[3])):
            if splitted_code[3][i] != '"':
                jam2 += splitted_code[3][i]
        splitted_code[3] = jam2
        return splitted_code
    except:
        print("error found | your input is not true, try again:")

def grayscale(img): # from before
    image = ImageOps.grayscale(img)
    return image

def bAndW(img): # from before
    image = img.convert("1")
    return image

def negative(img): # from before
    image = ImageOps.invert(img)
    return image
def brown_style(img): # sepehr new
    image = img.brown_style(img)
    return image
def cmyk(img): # sepehr new
    image = img.format(CMYK)
    return image    
def blur(img): # sepehr new
    image = img.filter(ImageFilter.BLUR)
    return image

def resize(img, dimensions:list ): # sepehr new
    image = img.resize((dimensions[0],dimensions[1]))
    return image

def rotate(img,degree): #sepehr new
    image = img.rotate(degree)
    return image
"""
def detail(img): # sepehr new
    print(f"format : {img.format}")
    print(f"size : ({img.width},{img.height})")
    print(f"mode : {img.mode}")
"""

def editing_mistake(edit_type): # by AmirParsa Rouhani
    all_types = settings.EDITING_VALID_TYPES.copy()
    valid_types = []
    for i in range(len(all_types)):
        t = 0
        for h in range(len(edit_type)):
            for j in range(len(all_types[i])):
                if all_types[i][j] == edit_type[h]:
                    t += 1
        if t + 2 >= len(edit_type) >= t - 2:
            valid_types.append(all_types[i])
    return valid_types

def edit_choose(address, img):
    if address == "grayscale": # from before
        img = grayscale(img)
        return img
    elif address == "black_and_white": #from before
        img = bAndW(img)
        return img
    elif address == "negative": #from before
        img = negative(img)
        return img
    elif address == "cmyk": # sepehr now
        img = cmyk(img)
        return img
    elif address == "brown_style": # sepehr now
        img = brown_style(img)
        return img
    elif address == "resize": # sepeher new
        dims = input(settings.RESIZE).split()
        for i in dims:
            try:
                i = int(i)
            except:
                print("thats probebly not number c:")
        img = resize(img,dims)
        return img
    elif address == "rotate": # sepehr new
        degree=int(input(settings.ROTATE))
        img = rotate(img,degree)
        return img
    elif address == "blur": # sepehr new
        img = blur(img)
        return img
    else: # this by AmirParsa (before)
        mistake = editing_mistake(address)
        if mistake == []:
            print(settings.editing_ERROR)
        else:
            print(settings.USER_MADE_MISTAKE)
            for i in range(len(mistake)):
                print(str(i + 1) + ". " + mistake[i])
            mistake_input = input()
            address = mistake[i - 1]
            return edit_choose(address, img)

def export_menu(address, img): # AmirParsa
    img.save(address)
    return

def insert_checker(address):
    try:
        img = Image.open(address[0])
        if address[1] == 'edit':
            img = edit_choose(address[2],img)
        else: #by AmirParsa Rouhani (from 102 to 112) # others from before
            print(settings.USER_MADE_MISTAKE)
            print("1. edit")
            print("2. nothing, just exit")
            editing_input = input()
            if editing_input == "2":
                print("Process finished | You exited without saving the image")
                return True
            elif editing_input == "1":
                address[1] = "edit"
                img = edit_choose(address[2], img)
        try:
            export_menu(address[3],img)
            return True
        except:
            print("Error found | Can't export the file, try again: " + address[3]) 
    except:
        print("Error found | No image found with address: " + address[0])

