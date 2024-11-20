from tkinter import *
import os
from openai import OpenAI
global q
global path

client = OpenAI()


#GUI
root = Tk()
root.title("Watch Lookup")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

sended = ""
def get_send():
    return send
#Send function
def send():
    e.get()
    send = e.get()
    txt.insert(END, "\n" + send)
    #print(e.get())
    print(sended)
    user = e.get().lower()
    question = send
    q = question.lower()
    path = 'path to watch data' + q + '.txt'

    if os.path.exists(path):
        x = open(path, 'r')
        txt.insert(END, x.read())
    else:
        global formattedmessage
        completion = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system",
                 "content": "you are only able to tell me the following information about a watch in the from "
                            "of a list: ID, Brand, Model Number, Year Released, Measurements, Lug Width, "
                            "Lug to Lug, Diameter, Bracelet, Bracelet/Strap, Leather/NATO/Rubber, Color, "
                            "Movement, Maker, Quartz/Mechanical, Automatic/Hand Wind, Complication, "
                            "Case Material, Color, Bezel style. if a selection varies, write all variations"},
                {"role": "user", "content": q}
            ]
        )

        formattedMessage = completion.choices[0].message.content
        formattedMessage = str(formattedMessage)
        f = open(path, 'w')
        f.write(formattedMessage)
        f.close()
        txt.insert(END, "\n" + formattedMessage)


    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Watch Lookup v1.0", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

txt.insert(END, "\n" + "What watch?")

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)

root.mainloop()

