import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

width, height = 300, 300
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam_active = False

def ToggleCam():

    global cam_active, Cam_Text
    print(cam_active)
    if cam_active == False:
        cam_active = True
        btn_Cam["text"] = "cam - on"
    else:
        cam_active = False
        btn_Cam["text"] = "cam - off"

def getImage():
    global photo
    filename = filedialog.askopenfilename()
    photo = ImageTk.PhotoImage(file=filename)
    lmain.configure(image=photo)


root = Tk()
root.bind('<Escape>', lambda e: root.quit())

canvas = Canvas(root,height=400,width=600)
canvas.pack()

Cam_frame = Frame(root, bg="black")
Cam_frame.place(relx = 0.05, rely= 0.05, relwidth=0.5, relheight=0.85)
lmain = Label(Cam_frame, bg="black")
lmain.pack()

Info_frame = Frame(root)
Info_frame.place(relx=0.6, rely= 0.05, relwidth=0.35,relheight=0.5)


btn_Cam = Button(Info_frame, text="cam - off", command= ToggleCam)
btn_File = Button(Info_frame, text="load image",command=getImage)
lbl_Data = Label(Info_frame,text="Information: ")
cbo_Cam = ttk.Combobox(Info_frame, values=["Camera One", "Camera Two"])

btn_Cam.place(relx = 0.05, rely= 0.05, relwidth=0.4)
cbo_Cam.place(relx = 0.5, rely=0.065, relwidth=0.5)
btn_File.place(relx = 0.05, rely= 0.25, relwidth=0.4)
lbl_Data.place(rely= 0.45, relwidth=0.5)

cbo_Cam.current(0)


def show_frame():
    if cam_active == True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
    else:
        lmain.imgtk = None

    lmain.after(10, show_frame)


show_frame()
root.mainloop()