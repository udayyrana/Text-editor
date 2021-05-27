import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser,filedialog,messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x700')
main_application.title('U-pad Text Editor')



################ main menu ##########################
#################End Main menu#######################
# for adding file icons
# new_icon = tk.PhotoImage('path')
main_menu = tk.Menu()

file_menu = tk.Menu(main_menu,tearoff=False)

edit_menu = tk.Menu(main_menu,tearoff=False)

view_menu = tk.Menu(main_menu,tearoff=False)

help_menu = tk.Menu(main_menu,tearoff=False)





#########"""""""color theme'''''''###########
color_menu = tk.Menu(main_menu,tearoff=False)
theme_choice = tk.StringVar()

color_dict = {
    'Light Defalut' : ('#000000', '#ffffff'),
    'Light  Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' : ('#ededed', '#6b9dc2')
}

#cascade
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_cascade(label='View',menu=view_menu)
main_menu.add_cascade(label='Color',menu=color_menu)
main_menu.add_cascade(label='Help',menu=help_menu)

################ toolbar ##########################
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)


# font box
font_tuple = tk.font.families()
font_family =tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Times New Roman'))
font_box.grid(row=0,column=0,padx=5)

#size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var,state='readonly')
font_size['values'] = tuple(range(8,60,2))
font_size.current(2)
font_size.grid(row=0,column=1,padx=5)

#bold button
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_btn = ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

#italic button
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_btn = ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

#under line button
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_btn = ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

#font color button
font_icon = tk.PhotoImage(file='icons/font_color.png')
font_btn = ttk.Button(tool_bar,image=font_icon)
font_btn.grid(row=0,column=5,padx=5)

#align buttons
align_left_icon = tk.PhotoImage(file='icons/align_left.png')
align_left_btn = ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

align_center_icon = tk.PhotoImage(file='icons/align_center.png')
align_center_btn = ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

align_right_icon = tk.PhotoImage(file='icons/align_right.png')
align_right_btn = ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

#################End toolbar#######################


################ text editor ##########################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscroll=scroll_bar.set)

#font family and font size functionality
current_font_family='Times New Roman'
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_fontsize)

##########button functionality************
##bold button functionality

def change_bold(event=None):
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_btn.configure(command=change_bold)


#######italic button functionality*****

def change_italic(event=None):
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] =='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

italic_btn.configure(command=change_italic)


#######underline functionality*****

def change_underline(event=None):
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_btn.configure(command=change_underline)


def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_btn.configure(command=change_font_color)

#####align functionality
def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=align_left)


def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=align_center)


def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('rightalign_right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'rightalign_right')

align_right_btn.configure(command=align_right)






text_editor.config(font=('Times New Roman',12))

#################End text editor#######################


################ status bar ##########################

status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

##status bar functionality

text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",changed)

#################End status bar#######################


################ main menu functionality ##########################

url = ''
#####new functionality

def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

file_menu.add_command(label='New', accelerator='Ctrl+N',command=new_file)    #if want to add image then put image='new_icon(mentioned above)' then compund=tk.left

###### open functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File', filetypes=(('Text File','*.txt'),('All Files','*,*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

#file_commands
file_menu.add_command(label='Open', accelerator='Ctrl+O',command=open_file) 
file_menu.add_separator()

#save file
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*,*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

file_menu.add_command(label='Save', accelerator='Ctrl+S',command=save_file)  

# save as functionality
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*,*')))
        url.write(content)
        url.close()
    except:
        return

file_menu.add_command(label='Save As', accelerator='Ctrl+Shift+S',command=save_as)    
file_menu.add_separator()

#exit functionality

def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*,*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file_menu.add_command(label='Exit',command=exit_func)


#edit commands
edit_menu.add_command(label='Cut',accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit_menu.add_command(label='Copy',accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit_menu.add_command(label='Paste',accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit_menu.add_separator()
edit_menu.add_command(label='Clear All',command=lambda:text_editor.delete(1.0,tk.END))

#find Functionality
def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get('1.0',tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete('1.0',tk.END)
        text_editor.insert('1.0',new_content)
        
    find_dialog = tk.Toplevel()
    find_dialog.geometry('450x150+500+200')
    find_dialog.title('Find and Replace')
    find_dialog.resizable(0,0)

    ###frame
    find_frame = ttk.LabelFrame(find_dialog,text='Find/Replace')
    find_frame.pack(pady=20)

    #label
    text_find_label = ttk.Label(find_frame,text='Find : ')
    text_replace_label = ttk.Label(find_frame,text='Replace : ')

    #entry box
    find_input = ttk.Entry(find_frame, width=30)    
    replace_input = ttk.Entry(find_frame, width=30)

    #button
    find_button = ttk.Button(find_frame, text='Find',command=find)
    replace_button = ttk.Button(find_frame, text='Replace',command=replace)

    #label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    #entry box grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    
    #button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_dialog.mainloop()

#edit_commands

edit_menu.add_command(label='Find',accelerator='Ctrl+F',command=find_func)

#view
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        # status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True



def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar= False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True

#view commands
view_menu.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_toolbar,command=hide_toolbar)
view_menu.add_checkbutton(label='Status Bar',onvalue=True,offvalue=0,variable=show_statusbar,command=hide_statusbar)

#color commands
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color,foreground=fg_color)

count=0
for i in color_dict:
    color_menu.add_radiobutton(label=i,variable=theme_choice,command=change_theme)
    count+=1

#help command
# help_menu.add_command(label='Help',accelerator='F1')



#################End Main menu functionality#######################


main_application.config(menu=main_menu)

#########bind shorcut keys
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Shift-S>", save_as)
main_application.bind("<Alt-x>", exit_func)
main_application.bind("<Control-f>", find_func)


main_application.mainloop()