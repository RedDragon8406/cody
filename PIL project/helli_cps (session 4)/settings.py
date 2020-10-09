MENUS_VALID_STATES = [
    "Menu",
    "Exit"
]#from before

EDITING_VALID_TYPES = [
    "grayscale",
    "black_and_white",
    "negative",
    "cmyk",
    "brown_style",
    "resize",
    "rotate",
    "blur"
] #by AmirParsa Rouhani

editing_ERROR = """Your edit choice not found | Try again by choosing one of the following options:
"address" edit [your edit choice] "exporting address"
1. grayscale
2. black and white
3. negative
4. cmyk
5. brown_style
6. resize
7. rotate
8. blur
""" # from before

MAIN_MENU = """Please insert your code like the following answer: 
"img address" edit [your edit choice] "export address" | or type: help """ #from before

RESIZE = """pls tell me new dimensions like: 10 10 : """ #Sepehr Kardel

ROTATE = """pls tell me a degree for rotating""" #Sepehr Kardel

USER_MADE_MISTAKE = """Your input has a mistake, did you mean:""" #by AmirParsa Rouhani

HELP_MENU = """Help menu:
Please choose one of the following options:
1. Full help
2. separated help"""

help_ERROR = "Error found | Sorry, but your help choice is false, try again:" #AmirParsa

full_help_menu = """Full help menu:
Welcome to our help menu, use these options to get better experience from our app:
Main Menu:
To use our app, you should write this command:
“example.type” edit editType “outExample.type”
+Example.type is your new file name & type
+edit should be in code, if its not, it means that you don’t want to edit your image and you’ll get an error
+editType is your edit type to edit the image, it should be in the code, else you’ll get an error
Valid edit types:
1. grayscale
2. black and white
3. negative
4. cmyk
5. brown_style
6. resize
7. rotate
8. blur

+outExample.type is your finished image name & type
All of these 4 items should be in the app, else you’ll get an error
=======================================================================================

Errors menu:
+ Error found | No image found with address:
This error says that your input image has a problem, maybe your address is not true, or the location is not.

+ Error found | Can't export the file, try again:
This error says that the app can’t export the file, usually this error happens when the type of the exported image is not True!

+ Error found | your input is not true, try again:
This error says that you made a mistake in the code, maybe you didn’t write “edit” or you didn’t write your editting type to edit the image.

+ Your edit choice not found | Try again by choosing one of following options:
"address" edit [your edit choice] "exporting address"
1. grayscale
2. black and white
3. negative
4. cmyk
5. brown_style
6. resize
7. rotate
8. blur
This error says that you didn’t write a valid edit type, maybe it has a typing mistake

+ Your input has a mistake, did you mean:
This error happens when you didn’t write “edit” correctly or your editting type has a mistake.
""" #by AmirParsa


side_parts = """In which part of the program do you need help? 
1.main part (how to edit)
2.error part
""" #by sepehr


help_error = """Errors menu:
+ Error found | No image found with address:
This error says that your input image has a problem, maybe your address is not true, or the location is not.

+ Error found | Can't export the file, try again:
This error says that the app can’t export the file, usually this error happens when the type of the exported image is not True!

+ Error found | your input is not true, try again:
This error says that you made a mistake in the code, maybe you didn’t write “edit” or you didn’t write your editting type to edit the image.

+ Your edit choice not found | Try again by choosing one of following options:
"address" edit [your edit choice] "exporting address"
1. grayscale
2. black and white
3. negative
4. cmyk
5. brown_style
6. resize
7. rotate
8. blur
This error says that you didn’t write a valid edit type, maybe it has a typing mistake""" #by sepehr

help_main = """Main Menu:
To use our app, you should write this command:
“example.type” edit editType “outExample.type”
+Example.type is your new file name & type
+edit should be in code, if its not, it means that you don’t want to edit your image and you’ll get an error
+editType is your edit type to edit the image, it should be in the code, else you’ll get an error
Valid edit types:
1. grayscale
2. black and white
3. negative
4. cmyk
5. brown_style
6. resize
7. rotate
8. blur""" #by sepehr
