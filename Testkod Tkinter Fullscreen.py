from tkinter import *


window=Tk()


# window.configure(width = screen_width, height = screen_height)

windowsize = "200x200+-300+-300"
window.geometry (windowsize)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

print(str(screen_width) + str(screen_height))

window.state('zoomed')



# window.configure(width = screen_width, height = screen_height)
# windowsize = str(screen_width) + "x" + str(screen_height) + "+-500+-0"
# windowsize = str(screen_width) + "x" + str(screen_height) + "+-500+-0"
# window.geometry (windowsize)


# print(windowsize)



window.configure(bg = 'white')
text = Text(window)
text.insert(INSERT, "Hello....." + '\n')
text.insert(INSERT, "Hi.....")
text.pack()



window.mainloop()



