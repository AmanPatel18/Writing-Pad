from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk
import PIL.Image

win=Tk()
win.title("Writing Pad")
win.geometry("900x600")
win.iconbitmap('c:/users/patel/documents/Python/Tkinter/Images/Coding_Drift.ico')

global open_file_name
open_file_name = False

def open_file():
    text_field.delete("1.0",END)
    
    text_file=filedialog.askopenfilename(initialdir="C:/Users/patel/Documents/",title="Open File",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
    
    if text_file:
        global open_file_name
        open_file_name=text_file

    name=text_file
    name=name.replace("C:/Users/patel/Documents/","")
    win.title(f'{name} - Writing Pad')

    text_file=open(text_file,'r')
    data=text_file.read()
    text_field.insert(END,data)
    text_file.close()

def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension="." ,initialdir="C:/Users/patel/documents", title="Save File As...", filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))

    if text_file:
        name=text_file
        name=name.replace("C:/Users/patel/Documents/","")
        win.title(f'{name} - Writing Pad!')

        text_file=open(text_file,'w')
        data=text_field.get(1.0,END)
        text_file.write(data)
        text_file.close()
        messagebox.showinfo(title="Save File Status",message="File Saved Successfully!")

def save_as_file2(event):
    text_file=filedialog.asksaveasfilename(defaultextension="." ,initialdir="C:/Users/patel/documents", title="Save File As...", filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))

    if text_file:
        name=text_file
        name=name.replace("C:/Users/patel/Documents/","")
        win.title(f'{name} - Writing Pad!')

        text_file=open(text_file,'w')
        data=text_field.get(1.0,END)
        text_file.write(data)
        text_file.close()
        messagebox.showinfo(title="Save File Status",message="File Saved Successfully!")
    

def save_file():
    global open_file_name
    try:
        if open_file_name:
            text_file=open(open_file_name,'w')
            data=text_field.get(1.0,END)
            text_file.write(data)
            text_file.close()
            messagebox.showinfo(title="Save File Status",message="File Saved Successfully!")
    
        else:
            save_as_file()

    except Exception as e:
        print(e)
        messagebox.showerror(title="Save File Status",message="File can't be saved!")
        
def save_file2(event):
    global open_file_name
    try:
        if open_file_name:
            text_file=open(open_file_name,'w')
            data=text_field.get(1.0,END)
            text_file.write(data)
            text_file.close()
            messagebox.showinfo(title="Save File Status",message="File Saved Successfully!")
    
        else:
            save_as_file()
    except Exception as e:
        print(e)
        messagebox.showerror(title="Save File Status",message="File can't be saved!")

        
def new_file():
    text_field.delete(1.0,END)
    win.title("New File.txt")
    global open_file_name
    open_file_name = False

def about():
    global img
    new_win=Toplevel()
    new_win.geometry("550x300")
    new_win.resizable(0,0)
    new_win.title("About")
    new_win.configure(bg="#7782e6")

    img=ImageTk.PhotoImage(PIL.Image.open('c:/users/patel/documents/Python/Tkinter/Images/Coding_Drift.jpg'))
    img_label=Label(new_win,image=img,borderwidth=0)
    img_label.place(x=10,y=0)

    head='Writing Pad'
    version='Version 1.0\n© 2020 Coding Drift Corporation.\nAll rights reserved.'
    body='This is a text editor where you can edit different types of file and save them.'
    body2='You can do coding and save your code in any correct format.'
    credit="Creted By: Aman Patel"
    email='Email: Patelaman101@gmail.com'

    l1=Label(new_win,text=head,font='Helvetica 20 bold',bg='#7782e6').place(x=200,y=0)
    l2=Label(new_win,text=version,font='Ariel 12 bold',bg='#7782e6').place(x=150,y=50)
    l3=Label(new_win,text=body,font='Ariel 12 italic',bg='#7782e6').place(x=0,y=150)
    l4=Label(new_win,text=body2,font='Ariel 12 italic',bg='#7782e6').place(x=0,y=175)
    l5=Label(new_win,text=credit,font='Ariel 12 bold',bg='#7782e6').place(x=0,y=220)
    l6=Label(new_win,text=email,font='Ariel 12 bold',bg='#7782e6').place(x=0,y=250)
    
def menu_bar():
    global file_menu
    global edit_menu
    global tool_menu
    global help_menu
    #declare main menu

    main_menu=Menu(win)                                     # Menu Bar
    win.config(menu=main_menu)
    
    #adding items to main menu
    
    file_menu=Menu(main_menu,font="Helvetica 10 normal",tearoff=0)     # File Menu
    main_menu.add_cascade(label='File',menu=file_menu)
    
    edit_menu=Menu(main_menu,font="Helvetica 10 normal",tearoff=0)     # Edit Menu
    main_menu.add_cascade(label='Edit',menu=edit_menu)

    tool_menu=Menu(main_menu,font='Helvetica 10 normal',tearoff=0)
    main_menu.add_cascade(label='Tools',menu=tool_menu)

    help_menu=Menu(main_menu,font="Helvetica 10 normal",tearoff=0)     # Help Menu
    main_menu.add_cascade(label='Help',menu=help_menu)
    
    #adding commands to main menu
    
    #file menu commands
    
    file_menu.add_command(label='New File',command=new_file)       # New File
    file_menu.add_command(label='Open File',command=open_file)     #Open File
    
    file_menu.add_separator()
    
    file_menu.add_command(label='Save           Ctrl+S',command=save_file)          # Save File
    file_menu.add_command(label='Save as...    Ctrl+Shift+S',command=save_as_file)    # Save as File
    
    file_menu.add_separator()
    file_menu.add_command(label='Close Window',command=win.quit)   #Close Window
    
    #edit menu commands

    edit_menu.add_command(label='Cut       Ctrl+X',command=lambda: win.event_generate('<Control-x>'))  #cut command
    edit_menu.add_separator()
    edit_menu.add_command(label='Copy     Ctrl+C',command=lambda: win.event_generate('<Control-c>')) #copy command
    edit_menu.add_separator()
    edit_menu.add_command(label='Paste    Ctrl+V',command=lambda: win.event_generate('<Control-v>')) #paste command
    edit_menu.add_separator()
    edit_menu.add_command(label='Undo     Ctrl+Z',command=text_field.edit_undo)
    edit_menu.add_separator()
    edit_menu.add_command(label='Redo     Ctrl+Y',command=text_field.edit_redo)

    #tool menu commands
    tool_menu.add_command(label="Dark Mode On", command=dark_on)
    tool_menu.add_separator()
    tool_menu.add_command(label="Dark Mode Off", command=dark_off)

    #help menu commands

    help_menu.add_command(label='About',command=about)

    # edit menu shortcut commands

    win.bind('<Control-s>',save_file2)
    win.bind('<Control-Shift-KeyPress-S>',save_as_file2)

# Turn on dark Mode
def dark_on():
	main_color = "SystemButtonFace"
	second_color = "SystemButtonFace"
	text_color = "white"

	win.config(bg=main_color)
	text_field.config(bg="black",fg=text_color)
	# file menu colors
	file_menu.config(bg=main_color)
	edit_menu.config(bg=main_color)
	help_menu.config(bg=main_color)
	tool_menu.config(bg=main_color)

# Turn Off dark Mode:
def dark_off():
	main_color = "SystemButtonFace"
	second_color = "SystemButtonFace"
	text_color = "black"

	win.config(bg=main_color)
	text_field.config(bg="white",fg="black")
	# file menu colors
	file_menu.config(bg=main_color)
	edit_menu.config(bg=main_color)
	help_menu.config(bg=main_color)
	tool_menu.config(bg=main_color)

# main text field

text_field=Text(win,width=100,height=20,bd=3,relief='solid',font="Ariel 16 normal",padx=30,pady=30,selectbackground='#fe3d3d',undo=True)
text_field.pack(padx=20,pady=20,fill=BOTH,expand=1)

menu_bar()    
win.mainloop()
