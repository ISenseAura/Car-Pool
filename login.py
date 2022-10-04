from pathlib import Path
from re import L
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
 
 
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/login")
 
 
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
 
def login():
    LOGIN()
 
class LOGIN(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
 
 
        self.geometry("360x800")
        self.configure(bg = "#FFFFFF")
 
 
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 800,
            width = 360,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
 
        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            180.0,
            400.0,
            image=image_image_1
        )
 
        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            180.0,
            272.0,
            image=image_image_2
        )
 
        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            181.0,
            376.0,
            image=image_image_3
        )
 
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            182.0,
            285.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        entry_1.place(
            x=64.0,
            y=272.0,
            width=236.0,
            height=25.0
        )
 
        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            182.0,
            386.5,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        entry_2.place(
            x=64.0,
            y=373.0,
            width=236.0,
            height=25.0
        )
 
        self.canvas.create_text(
            70.0,
            243.0,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("Bungee Regular", 16 * -1)
        )
 
        self.canvas.create_text(
            64.0,
            347.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Bungee Regular", 16 * -1)
        )
 
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
   
   
   
        button_1.image = button_image_1
        button_1.place(
            x=165.0,
            y=413.0,
            width=152.0,
            height=45.0
        )
 
        button_image_2 = PhotoImage(
            file="/Users/admin/Documents/Car%20Pool/build/assets/button_2.png")
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
   
        button_2.image = button_image_2
        button_2.place(
            x=100.0,
            y=477.0,
            width=161.0,
            height=56.0
        )
 
        self.canvas.create_text(
            165.0,
            534.0,
            anchor="nw",
            text="or",
            fill="#FFFFFF",
            font=("Cairo Bold", 20 * -1)
        )
 
        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.image = button_image_3
        button_3.place(
            x=57.0,
            y=582.0,
            width=257.0,
            height=47.0
        )
 
        self.canvas.create_rectangle(
            116.0,
            672.0,
            256.0,
            672.0,
            fill="#000000",
            outline="")
 
        self.canvas.create_text(
            48.0,
            721.0,
            anchor="nw",
            text="Don’t have an account?",
            fill="#FFFFFF",
            font=("Cairo Bold", 20 * -1)
        )
 
        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_2.image = button_image_2
        button_4.place(
            x=255.0,
            y=718.0,
            width=76.0,
            height=35.0
        )
 
        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            199.0,
            117.0,
            image=image_image_4
        )
        self.resizable(False, False)
        self.mainloop()
 
