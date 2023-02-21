import tkinter
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageEnhance

files = []
wtrmrks = []
raw_wtr = []
finished_products = []
filename = ""
# -----------------------------------------------------------------------
# def wtrpasity(event):
#     global wtrmrks, raw_wtr
#     opacity = int(watermark_opacity.get())
#     image1 = Image.open(raw_wtr[-1])
#     image1.putalpha(round((opacity/100)*255))
#     image1.thumbnail((img.width, img.height))
#     wtrmrks[-1] = image1
#     wtrsize(watermark_size.get())
#     wtrpos(pos.get())
# -----------------------------------------------------------------------
def wtrsize(event):
    global wtrmrks, raw_wtr
    percentage = watermark_size.get()
    image1 = Image.open(raw_wtr[-1])
    wdth, height = image1.size
    if wdth > height:
        w = int(10*percentage)
        h = round(w*height/wdth)
        img = image1.resize((w, h))
    elif wdth < height:
        h = int(2*percentage)
        w = round(h*wdth/height)
        img = image1.resize((w,h))

    opacity = watermark_opacity.get()/100
    # img.convert("RGBA")
    # pixels = img.load()
    # for y in range(int(height * .55), int(height * .75)):
    #     alpha = 255 - int((y - height * .55) / height / .20 * 255)
    #     for x in range(wdth):
    #         pixels[x, y] = pixels[x, y][:3] + (alpha,)
    # for y in range(y, height):
    #     for x in range(wdth):
    #         pixels[x, y] = pixels[x, y][:3] + (0,)

    img.convert("RGBA")
    assert 0 <= opacity <= 1
    alpha = img.split()[2]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    img.putalpha(alpha)
    img.thumbnail((img.width, img.height))
    img.putalpha(alpha)
    wtrmrks.append(img)
    wtrpos(pos.get())
# -----------------------------------------------------------------------
def save():
    global finished_products
    index = 0
    for image in finished_products:
        image.save(f"C:\\Users\\USER\Desktop\\{index}.png", "PNG")
        index +=1

# -----------------------------------------------------------------------
def wtrpos(event):
    global wtrmrks, files, finished_products
    finished_products = []
    img = wtrmrks[-1]
    for f in files:
        new_image = Image.open(f)
        wdth, height = new_image.size
        if wdth > height:
            image__ = new_image.resize((830, round(830 * height / wdth)))
            display.geometry("1200x800")
            display.maxsize(width=1200, height=800)
        else:
            image__ = new_image.resize((round(800 * wdth / height), 800))
            display.maxsize(width=round(800 * wdth / height) + 370, height=800)
            display.geometry(f"{round(800 * wdth / height) + 370}x{800}")
        position = pos.get()
        if position == 1:
            x = 10
            y = 10
        elif position == 2:
            x = image__.width - (img.width + 10)
            y = 10
        elif position == 3:
            x = round((image__.width / 2) - (img.width / 2))
            y = round((image__.height / 2) - (img.height / 2))
        elif position == 4:
            x = 10
            y = image__.height - (img.height + 10)
        elif position == 5:
            x = image__.width - (img.width + 10)
            y = image__.height - (img.height + 10)

        image__.paste(img, (x, y))
        finished_products.append(image__)
        try:
            select_image(uploader.curselection())
        except tkinter.TclError:
            pass

# -----------------------------------------------------------------------
def select_image(event):
    global filename, finished_products
    if len(finished_products) < 1:
        file = uploader.get(uploader.curselection())
        image1 = Image.open(file)
        wdth, height = image1.size
        if wdth > height:
            img = image1.resize((830, round(830 * height / wdth)))
            display.geometry("1200x800")
            display.maxsize(width=1200, height=800)
        else:
            img = image1.resize((round(800 * wdth / height), 800))
            display.maxsize(width=round(800 * wdth / height) + 370, height=800)
            display.geometry(f"{round(800 * wdth / height) + 370}x{800}")

        # Convert the image in TkImage
        test = ImageTk.PhotoImage(img)
        filename = file
        # Display the image with label
        canvas.config(width=img.width, height=img.height)
        canvas.create_image(0, 0, image=test, anchor="nw", tag="hello")
        canvas.image = test

    else:
        try:
            current = finished_products[uploader.curselection()[0]]
            wdth, height = current.size
            if wdth > height:
                img = current.resize((830, round(830 * height / wdth)))
                display.geometry("1200x800")
                display.maxsize(width=1200, height=800)
            else:
                img = current.resize((round(800 * wdth / height), 800))
                display.maxsize(width=round(800 * wdth / height) + 370, height=800)
                display.geometry(f"{round(800 * wdth / height) + 370}x{800}")

            test = ImageTk.PhotoImage(img)
            canvas.config(width=img.width, height=img.height)
            canvas.create_image(0, 0, image=test, anchor="nw", tag="hello")
            canvas.image = test
        except IndexError:
            file = uploader.get(uploader.curselection())
            image1 = Image.open(file)
            wdth, height = image1.size
            if wdth > height:
                img = image1.resize((830, round(830 * height / wdth)))
                display.geometry("1200x800")
                display.maxsize(width=1200, height=800)
            else:
                img = image1.resize((round(800 * wdth / height), 800))
                display.maxsize(width=round(800 * wdth / height) + 370, height=800)
                display.geometry(f"{round(800 * wdth / height) + 370}x{800}")

            # Convert the image in TkImage
            test = ImageTk.PhotoImage(img)
            filename = file
            # Display the image with label
            canvas.config(width=img.width, height=img.height)
            canvas.create_image(0, 0, image=test, anchor="nw", tag="hello")
            canvas.image = test

# -----------------------------------------------------------------------
def dlt(filename):
    print(filename)
    print(uploader.get(ANCHOR))
    if str(uploader.get(ANCHOR)) == str(filename):
        canvas.delete("hello")
        viewer_section.config(width=830, height=800)
        canvas.config(width=830, height=800)
        display.geometry("1200x800")
        display.maxsize(width=1200, height=800)
    files.remove(uploader.get(ANCHOR))
    uploader.delete(ANCHOR)
# -----------------------------------------------------------------------
def upld():
    filetypes = (('All files', '*.*'), ('text files', '*.txt'))

    filenames = fd.askopenfilenames(title='Upload', initialdir='/', filetypes=filetypes)

    for filename in filenames:
        files.append(filename)
        uploader.insert(END, filename)

def upld_wtrmrk():
    global wtrmrks
    filetypes = (('All files', '*.*'), ('text files', '*.txt'))

    filenames = fd.askopenfilenames(title='Upload', initialdir='/', filetypes=filetypes)
    for filename in filenames:
        raw_wtr.append(filename)
    wtrsize(watermark_size.get())


# -----------------------------------------------------------------------
display = Tk()
display.title("Image Watermark")
display.geometry("1200x800")
display.maxsize(width=1200, height=800)
display.config(bg="grey")
# --------------------------Edit Section-----------------------------

edit_section = Frame(pady=5, bg="grey", highlightthickness=0, borderwidth=0)
edit_section.grid(column=0, row=0)

# -----------title & description-------------
title = Label(edit_section, bg="grey", text="Image Watermark App", padx=20, pady=10, justify="center", font=("sans", 15, "bold"))
title.grid(column=0, row=0, columnspan=2)

description = Label(edit_section, bg="grey", text="*Upload images\n*Upload your watermak (transparent background)\n*configure the size of the watermark\n*Position the watermark\n*Save the image(s)", padx=50, pady=10, justify="left")
description.grid(column=0, row=1, columnspan=2)

# --------------Upload images & Show them-------------------
upload = Button(edit_section, anchor="center", justify="center", text="Upload an image", bg="blue", fg="white", width=15, command=upld, borderwidth=0, font=("sans", 9, "bold"))
upload.grid(column=0, row=2, columnspan=2)

file_holder = Frame(edit_section, bg="grey")
file_holder.grid(column=0, row=3, rowspan=5, padx=10, pady=10, columnspan=2)

scroll = Scrollbar(file_holder, orient="vertical")

uploader = Listbox(file_holder, width=42, justify="left", yscrollcommand=scroll.set, selectmode=SINGLE)
uploader.bind('<Double-1>', select_image)
uploader.grid(column=0, row=0, rowspan=5)

scroll.config(command=uploader.yview)
# scroll.grid(column=1, row=0, rowspan=5)

white_space = Label(file_holder, text="", bg="grey")
white_space.grid(row=5, column=0)

delete = Button(file_holder, command=lambda: dlt(filename), text="Delete", anchor="center", justify="center", bg="blue", fg="white", width=12, borderwidth=0, font=("sans", 9, "bold"))
delete.grid(row=6, column=0)
# -----------------Watermark upload & Editor---------------------
watermark_section = Frame(edit_section, pady=20, padx=5, bg="grey")
watermark_section.grid(column=0, row=8, columnspan=2)

watermark = Button(watermark_section, command=upld_wtrmrk, borderwidth=0, text="Upload Watermark", bg="blue", fg="white", width=20, anchor="center", justify="center", font=("sans", 9, "bold"))
watermark.grid(column=0, row=0)

watermark_whitespace = Label(watermark_section, bg="grey", text="")
watermark_whitespace.grid(column=0, row=1)

watermark_size_label = Label(watermark_section, text="\nWatermark Size", font=("sans", 9, "bold"), bg="grey")
watermark_size_label.grid(column=0, row=3)

size = IntVar()
size.get()

watermark_size = Scale(watermark_section, variable=size, command=lambda x: wtrsize(size), orient=HORIZONTAL, length=300, bg="grey", highlightthickness=0, borderwidth=0)
watermark_size.set(50)
watermark_size.grid(column=0, row=4)

watermark_opacity_label = Label(watermark_section, text="\nWatermark Opacity", font=("sans", 9, "bold"), bg="grey")
watermark_opacity_label.grid(column=0, row=5)

pcty = IntVar()
pcty.get()

watermark_opacity = Scale(watermark_section, variable=pcty, command=lambda x: wtrsize(size), orient=HORIZONTAL, length=300, bg="grey", highlightthickness=0, borderwidth=0)
watermark_opacity.set(100)
watermark_opacity.grid(column=0, row=6)

watermark_position_frame = Frame(watermark_section, bg="grey")
watermark_position_frame.grid(column=0, row=7)

watermark_position_label = Label(watermark_position_frame, bg="grey", text="\nPosition", anchor="center", justify="center", padx=20, font=("sans", 9, "bold"))
watermark_position_label.grid(column=0, row=0, columnspan=3)

pos = IntVar()
pos.set(3)
pos.get()

p1 = Radiobutton(watermark_position_frame, bg="grey", text="Top Left", padx=10, value=1, variable=pos, command=lambda: wtrpos(pos.get()))
p1.grid(column=0, row=1)

p2 = Radiobutton(watermark_position_frame, bg="grey", text="Top Right", padx=10, value=2, variable=pos, command=lambda: wtrpos(pos.get()))
p2.grid(column=2, row=1)

p3 = Radiobutton(watermark_position_frame, bg="grey", text="Center", padx=10, value=3, variable=pos, command=lambda: wtrpos(pos.get()))
p3.grid(column=1, row=2)

p4 = Radiobutton(watermark_position_frame, bg="grey", text="Bottom Left", padx=10, value=4, variable=pos, command=lambda: wtrpos(pos.get()))
p4.grid(column=0, row=3)

p5 = Radiobutton(watermark_position_frame, bg="grey", text="Bottom Right", padx=10, value=5, variable=pos, command=lambda: wtrpos(pos.get()))
p5.grid(column=2, row=3)

save = Button(edit_section, command=save, borderwidth=0, text="Save", bg="blue", fg="white", width=15, anchor="center", justify="center", font=("sans", 9, "bold"))
save.grid(column=0, row=9, columnspan=2)

# ----------------------------Image Viewer-----------------------------
viewer_section = Frame(display, width=830, height=800, bg="black", borderwidth=0, highlightthickness=0)
viewer_section.grid(column=1, row=0, rowspan=10)

canvas = Canvas(viewer_section, bg="black", width=830, height=800, borderwidth=0, highlightthickness=0)
canvas.grid(column=0, row=0, rowspan=10)
# ----------------------------------------------------------------------
display.mainloop()