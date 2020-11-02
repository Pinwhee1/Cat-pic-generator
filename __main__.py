import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
import requests

BG = "#F9F4F2"
FG = "#262322"
RELIEF = "ridge"
GEOMETRY = "400x200+730+400"
GEOMETRY_SUB = "400x200+730+170"
CATPIC = "catpic.png"
with open("apikey.txt", "r") as f:
    APIKEY = f.read().strip()

class SubWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # Window

        self.title("Cat pic. @Pinwheel")
        self.resizable(False, False)
        self.configure(bg=BG)

        self.img = ImageTk.PhotoImage(Image.open(CATPIC))
        self.pic_holder = tk.Label(self, bg=BG, image=self.img)
        self.pic_holder.pack()

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window

        self.title("Get cat pics. @Pinwheel")
        self.geometry(GEOMETRY)
        self.resizable(False, False)
        self.configure(bg=BG)

        # The button.

        tk.Button(self, text="You know what to do.", bg=BG, fg=FG, relief=RELIEF,
            command=lambda: self.get_cat_pic(), font=Font(size=24)).place(
            anchor="n", relx=0.5, rely=0.05, relwidth=0.9, relheight=0.9)

    @classmethod
    def get_response(cls):
        response = requests.get(
            "http://api.thecatapi.com/v1/images/search",
            headers={"x-api-key": APIKEY})
        second_response = requests.get(response.json()[0]["url"])
        return second_response.content

    def get_cat_pic(self):
        with open(CATPIC, "wb") as f:
            f.write(self.get_response())
        SubWindow()

if __name__ == "__main__":
    MainWindow().mainloop()