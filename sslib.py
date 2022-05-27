from calendar import calendar
from ctypes import alignment
from textwrap import fill
from tkinter import *
from turtle import left, position, right
import qrcode
from tkcalendar import DateEntry
from tkinter import ttk, messagebox as mb
import mysql.connector as mysql
import datetime as dt
import string
import random

window = Tk()
window.title("Self-Service Library Management System")
window.geometry('1230x700')
window.resizable('false', 'false')
bg_image = PhotoImage(file = "welcome.png")
administrator_image = PhotoImage(file = "administrator.png")
book_list = PhotoImage(file="booklist.png")
add_book = PhotoImage(file="addbook.png")
borrow_book = PhotoImage(file="borrowbook.png")
set_date = PhotoImage(file="setdate.png")
borrow = PhotoImage(file="findbook.png")
return_book = PhotoImage(file="returnbook.png")
return_detail = PhotoImage(file="return_details.png")
window.iconbitmap("SSLIB.ico")



#add background image of a window
class Main:
    def __init__(self, master ):
        #Connect Mysql
        global mydb, mycursor
        #red #6d0e0e
        #yellow #e6a005
        #conneting to the msyql
        mydb1 = mysql.connect(host = "localhost", user = "root", password = "")
        mycursor1 = mydb1.cursor()
        #creating database
        mycursor1.execute("CREATE DATABASE IF NOT EXISTS book_management")
        mydb1.commit()

        #connect to the book_management database
        mydb = mysql.connect(host = "localhost", user = "root", password = "", database = "book_management")
        mycursor = mydb.cursor(buffered=True)
        #creating tables
        mycursor.execute("CREATE TABLE IF NOT EXISTS admin (id int auto_increment primary key, username varchar(255), password longtext)")
        mycursor.execute("CREATE TABLE IF NOT EXISTS add_book(id int auto_increment primary key, title varchar(255), author varchar(255), isbn varchar(255), genre varchar(255), quantity varchar(20), shelf_number varchar(100))")                                                 
        mycursor.execute("CREATE TABLE IF NOT EXISTS borrow (id int auto_increment primary key, name varchar(255), year varchar(20), section varchar(100), id_number varchar(30), course varchar(255), title varchar(255), isbn varchar(200), genre varchar(255), shelf_number varchar(255), date_borrowed varchar(255), date_returned varchar(255), uniq_code varchar(100))")
        mydb.commit()
        
        style = ttk.Style()
        style.theme_use('clam')
        
        #Exit/Back Button
        style.configure('link.TButton', background='#6d0e0e', foreground='white', borderwidth=0, width=8, font=('Times New Roman', 15))
        style.map('link.TButton', foreground=[('active', '#ffe600')], background=[('active', '#6d0e0e')])
        
        ##e6a005
        #Continue/Proceed Button
        style.configure('link1.TButton', background='#6d0e0e', foreground='white', borderwidth=0, width=9, height=15, font=('Franklin Gothic Demi', 15))
        style.map('link1.TButton', foreground=[('active', 'white')], background=[('active', '#e6a005')])
        
        #Submit Button Admin
        style.configure('submit.TButton', background='#9d9195', foreground='black', borderwidth=0, width=9, height=15, font=('Franklin Gothic Demi', 15))
        style.map('submit.TButton', foreground=[('active', 'white')], background=[('active', '#e6a005')])
        
        #add style button
        #Add/Delete Button
        style.configure('add.TButton', background='#9d9195', foreground='black', borderwidth=0, width=9, height=15, font=('Franklin Gothic Demi', 18))
        style.map('add.TButton', foreground=[('active', 'white')], background=[('active', '#e6a005')])
        
        #style for continue button
        #Back Borrow Button
        style.configure('con.TButton', background='white', foreground='black', borderwidth=0, font=('Franklin Gothic Demi', 15))
        style.map('con.TButton', foreground=[('active', '#6d0e0e')], background=[('active', 'white')])
        
        #Add Book Submit Button
        style.configure('link2.TButton', background='#9d9195', foreground='black', borderwidth=0, width=9, height=15, font=('Franklin Gothic Demi', 15))
        style.map('link2.TButton', foreground=[('active', 'white')], background=[('active', '#e6a005')])

        
        
        self.master = master
        self.welcome()
        
        
        
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Welcome Window
        
    def welcome(self):
        for i in self.master.winfo_children():
            i.destroy()
            
        frame1 = Frame(window, width=1230, height=700)
        image = Label(frame1, image = bg_image)
        image.place(x=0, y=0, relwidth=1, relheight=1)

        btn_admin =Button (frame1, text="ADMINISTRATOR",width=14,padx=21,pady=1,border=0,bg="#cdcfca",cursor ="hand2",font=("Franklin Gothic Demi",20), command= self.administrator)
        btn_admin.place(x=808, y=330)


        btn_borrow = Button(frame1, text="BORROW",width=14,padx=21,pady=1,border=0,bg="#cdcfca",cursor ="hand2",font=("Franklin Gothic Demi",20),command = self.borrow)
        btn_borrow.place(x=808, y=403)


        btn_return = Button(frame1, text="RETURN",width=14,padx=21,pady=1,border=0,bg="#cdcfca",cursor ="hand2",font=("Franklin Gothic Demi",20), command = self.Return)
        btn_return.place(x=808, y=476)


        btn_exit = ttk.Button(window,style="link.TButton", text="EXIT", cursor="hand2",command=window.destroy)
        btn_exit.place(x=891, y=555)


        frame1.pack()
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Administrator Log In Window
    
    def administrator(self):
        for i in self.master.winfo_children():
            i.destroy()
        
        def authentication():
            username = user.get()
            password = passw.get()
            query_login = "SELECT * FROM admin WHERE username = %s AND password = %s"
            mycursor.execute(query_login, (username, password))
            result = mycursor.fetchall()
            
            if result:
                mb.showinfo("Success", "Login Successful")
                self.book_list()
            else:
                mb.showerror("Error", "Invalid Username or Password")
        
        frame2 = Frame(window, width=1230, height=700)
        image = Label(frame2, image = administrator_image)
        image.place(x=0, y=0, relwidth=1, relheight=1)
        global user, passw
        username = Label(frame2, text="USERNAME :", fg= "white",bg="#6d0e0e", font=("Franklin Gothic Demi", 20))
        username.place(x=775, y=330)
        user = Entry(frame2, width=20, bg="white", font=("Franklin Gothic Demi", 20))
        user.place(x=775, y=370)
        def show_password():
            if passw.cget('show') == "*":
                passw.config(show='')
            else:
                passw.config(show="*")
                
                
        
        password = Label(frame2, text="PASSWORD :", fg= "white",bg="#6d0e0e", font=("Franklin Gothic Demi", 20))
        password.place(x=775, y=420)
        passw=Entry(frame2, width=20, bg="white", font=("Franklin Gothic Demi", 20),show="*")
        passw.place(x=775, y=460)
        
        check_button = Checkbutton(frame2,bg = "#6d0e0e", fg="white", text="show password", command=show_password)
        check_button.place(x=775, y=500)
        
        
        btn_submit = ttk.Button(frame2, style="submit.TButton", text="SUBMIT", cursor="hand2",command=authentication)
        btn_submit.place(x=875, y=545)
        btn_back = ttk.Button(frame2,style="link.TButton", text="BACK", cursor="hand2",command=self.welcome)
        btn_back.place(x=890, y=585)

        frame2.pack()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Book List Window
    def book_list(self):
        for i in self.master.winfo_children():
            i.destroy()
        global tree
        frame5 = Frame(window, width=1230, height=700)
        image = Label(frame5, image = book_list)
        image.place(x=0, y=0, relwidth=1, relheight=1)
        
        #Heading style of the Treeview 
        frame_data1 = Frame(frame5, width=1230, height=700)
        
        mycursor.execute("SELECT * FROM add_book ORDER BY id ASC")
        
        #scroll tree
        
        tree=ttk.Treeview(frame_data1, height=18)
        tree['show'] = 'headings'
        
        #configure scrollbar
        vsb = ttk.Scrollbar(frame_data1, orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y, side=RIGHT)        
        # Define number of columns
        tree["columns"]=("title", "author", "isbn", "genre", "quantity", "shlfnum")
        #Assign the width,minwidth and anchor to the respective columns
        tree.column("title", width=220, minwidth=100, anchor="center")
        tree.column("author", width=226, minwidth=100, anchor="center")
        tree.column("isbn", width=200, minwidth=100, anchor="center")
        tree.column("genre", width=200, minwidth=100, anchor="center")
        tree.column("quantity", width=100, minwidth=100, anchor="center")
        tree.column("shlfnum", width=130, minwidth=100, anchor="center")
        #Assign the heading names to the respective columns
        tree.heading("title", text="TITLE",anchor="center")
        tree.heading("author", text="AUTHOR",anchor="center")
        tree.heading("isbn", text="ISBN",anchor="center")
        tree.heading("genre", text="GENRE",anchor="center")
        tree.heading("quantity", text="QUANTITY",anchor="center")
        tree.heading("shlfnum", text="SHELF NUMBER",anchor="center")
        
        i = 0
        mycursor.execute("SELECT * FROM add_book")
        for row in mycursor:
            tree.insert("", i, values=(row[1], row[2], row[3], row[4], row[5], row[6]), tags=("even",))
            tree.tag_configure("even",foreground="black",background="#f5f5f5")

            
            i = i = i + 1
        
        
        
        #Delete Button
        def deleteDB(tree):
            for item in tree.selection():
                item_text = tree.item(item,"values")
                mycursor.execute("DELETE FROM add_book WHERE title = %s",(item_text[0],))
                mydb.commit()
                tree.delete(item)
            
        
        btn_add = ttk.Button(frame5, style="add.TButton", text="ADD", cursor="hand2", command=self.add_book)
        btn_add.place(x=455, y=565)
        
        btn_delete = ttk.Button(frame5, style="add.TButton", text="DELETE", cursor="hand2", command=lambda:deleteDB(tree))
        btn_delete.place(x=625, y=565)
        
        
        btn_back = ttk.Button(frame5,style="link.TButton", text="BACK", cursor="hand2",command=self.administrator)
        btn_back.place(x=563, y=620)

        tree.pack()
        frame_data1.place(x=75, y=155)
        frame5.pack()
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Add Book Window

    def add_book(self):
        #smoke #d9d9d9
        new=Toplevel(window)
        new.geometry("800x670")
        new.title("Add Book")
        new.resizable(False,False)
        image = Label(new, image = add_book)
        image.place(x=0, y=0, relwidth=1, relheight=1)
        
        def add():
            book_name = title.get()
            book_author = author.get()
            book_isbn = isbn.get()
            book_quantity = quantity.get()
            book_genry = genre.get()
            book_shelf_number = shlfnum.get()
            query1 = "INSERT INTO add_book(title, author, isbn, genre, quantity, shelf_number) VALUES( %s, %s, %s, %s, %s, %s)"
            mycursor.execute(query1, (book_name, book_author, book_isbn, book_genry, book_quantity, book_shelf_number))
            mydb.commit()
            
            mb.showinfo("Success", "Book Added Successfully")
            new.destroy()
            self.book_list()
        
        
        title = Entry(new, width=23,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        title.place(x=285, y=220)
        
        author = Entry(new, width=21,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        author.place(x=312, y=268)
        
        isbn = Entry(new, width=23,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        isbn.place(x=285, y=320)
        
        genre = Entry(new, width=22,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        genre.place(x=297, y=370)
        
        quantity = Entry(new, width=19,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        quantity.place(x=337, y=422)
        
        shlfnum = Entry(new, width=16,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        shlfnum.place(x=376, y=473)
        
        
        btn_submit = ttk.Button(new, style="link2.TButton", text="SUBMIT", cursor="hand2", command=add)
        btn_submit.place(x=334, y=532)
        
        
        window.mainloop()
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Borrow Book Window
    
    def borrow_book(self,tree):     
        new2=Toplevel(window)
        new2.geometry("1230x700")
        new2.title("Borrow a Book")
        new2.resizable(False,False)
        image = Label(new2, image = borrow_book)
        image.place(x=0, y=0, relwidth=1, relheight=1)
        
        curItem = tree.focus()
        values = tree.item(curItem, "values")
        print(values)
        
        title = Entry(new2, width=22,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        title.place(x=808, y=280)
        
        isbn = Entry(new2, width=22,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        isbn.place(x=808, y=334)
        
        genre = Entry(new2, width=22,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        genre.place(x=808, y=389)
        
        shlfnum = Entry(new2, width=22,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        shlfnum.place(x=808, y=450)
        
        #Form
        name = Entry(new2, width=22,bg="#d9d9d9",border=0, font=("Open Sans", 17))
        name.place(x=240, y=358)
        
        year = Entry(new2, width=22,bg="#d9d9d9",border=0, font=("Open Sans", 17))
        year.place(x=240, y=417)
        
        section = Entry(new2, width=19,bg="#d9d9d9",border=0, font=("Open Sans", 17))
        section.place(x=276, y=475)
        
        id_number = Entry(new2, width=17,bg="#d9d9d9",border=0, font=("Open Sans", 17))
        id_number.place(x=304, y=536)
        
        course = Entry(new2, width=20,bg="#d9d9d9",border=0, font=("Open Sans", 17))
        course.place(x=264, y=594)
        
        title.insert(0, values[0])
        isbn.insert(0, values[1])
        genre.insert(0, values[2])
        shlfnum.insert(0, values[3])
        Title=title.get()
        Isbn=isbn.get()
        Genre=genre.get()
        Shlfnum=shlfnum.get()
        
        date = dt.datetime.now()
        format_date = f"{date.month}/{date.day}/{date.year}"
        
        #show current date on entry
        date_br = Entry(new2, width=10,bg="#d9d9d9", font=("Franklin Gothic Demi", 18))
        date_br.insert(END, format_date)
        date_br.configure(state='readonly')
        date_br.place(x=155, y=237)
        
        #DATEPICKER DATE ENTRY
        date_rt=DateEntry(new2,selectmode='day', width=10,font=("Franklin Gothic Demi", 17), background='#d9d9d9',foreground='#000000', borderwidth=0, date_pattern='mm/dd/yyyy', year=date.year, month=date.month, day=date.day)
        date_rt.place(x=355, y=237)
        
        
        curdate = date_br.get()
        caldate = date_rt.get()
        def get_random_string(length):
            global result_str
        # With combination of lower and upper case
            result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        # print random string
            
        
        def generate_qrcode():
            get_random_string(15)
            
            
            Name=name.get()
            Year=year.get()
            Section=section.get()
            Id_number=id_number.get()
            Course=course.get()

            query = "INSERT INTO borrow(name, year, section, id_number,course, title, isbn, genre, shelf_number, date_borrowed, date_returned, uniq_code) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
            mycursor.execute(query,(Name, Year, Section, Id_number, Course, Title, Isbn, Genre, Shlfnum, curdate, caldate, result_str))
            qrcode_design = qrcode.QRCode(version=1, box_size=40, border=3)
            qrcode_design.add_data(f"""
+--------Dates-------+
Borrowed Date : {curdate}
Date of return : {caldate}

+-------Borrower Details-------+
Name : {name.get()}
School ID : {id_number.get()}

+-------Book Details-------+
Book Title : {title.get()}
Book ID : {isbn.get()}

+-------Return Code-------+
Code: {result_str}
""")
            qrcode_design.make(fit=True)
            generate_qrcode = qrcode_design.make_image(fill_color="#000000", back_color="#9e9b9b")
            generate_qrcode.save('yournewqrcode.png')
            mb.showinfo("Success", "Please save your QR code")
            generate_qrcode.show()
            mydb.commit()
            self.welcome()
            
            
            
        btn_submit = ttk.Button(new2, style="submit.TButton", text="SUBMIT", cursor="hand2", command = generate_qrcode)
        btn_submit.place(x=840, y=525)
        
        btn_back = ttk.Button(new2, style="link.TButton", text="BACK", cursor="hand2",command=self.borrow)
        btn_back.place(x=853, y=575)
        
        
        
        
        
        window.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------
#Borrow Window

    def borrow(self):
        for i in self.master.winfo_children():
            i.destroy()
        
            
        frame6 = Frame(window, width=1230, height=700)
        image = Label(frame6, image = borrow)
        image.place(x=0, y=0, relwidth=1, relheight=1)
        
        #Search Bar
        def search_func(ev):
            mycursor.execute("SELECT * FROM add_book WHERE title LIKE '%" +var_search.get()+ "%'")
            row = mycursor.fetchall()
            

            if len(row)>0:
                tree.delete(*tree.get_children())
                for i in row:
                    #highlight the selected row
                    tree.insert('', 'end', text="", values=(i[1], i[3], i[4], i[6]), tags=("color"))
                    tree.tag_configure("color",foreground="black",background="#f5f5f5")      
                    
            else:
                tree.delete(*tree.get_children())
                
        var_search = StringVar()   
        search = Entry(frame6,textvariable=var_search, width=22,bg="#d9d9d9", font=("Franklin Gothic Demi", 17))
        search.place(x=870, y=217)
        search.bind('<Key>', search_func)
        
        
        #Heading style of the Treeview 
        frame_data2 = Frame(frame6, width=1230, height=700)
        
        
        tree=ttk.Treeview(frame_data2, height=14)
        tree['show'] = 'headings'
        
        #configure scrollbar
        #scroll tree
        vsb = ttk.Scrollbar(frame_data2, orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y, side=RIGHT)
        # Define number of columns
        tree["columns"]=("title", "isbn", "genre", "shlfnum")
        #Assign the width,minwidth and anchor to the respective columns
        tree.column("title", width=298, minwidth=100, anchor="center")
        tree.column("isbn", width=300, minwidth=100, anchor="center")
        tree.column("genre", width=300, minwidth=100, anchor="center")
        tree.column("shlfnum", width=177, minwidth=100, anchor="center")
        #Assign the heading names to the respective columns
        tree.heading("title", text="TITLE",anchor="center")
        tree.heading("isbn", text="ISBN",anchor="center")
        tree.heading("genre", text="GENRE",anchor="center")
        tree.heading("shlfnum", text="SHELF NUMBER",anchor="center")
        
        i = 0
        mycursor.execute("SELECT * FROM add_book")
        for row in mycursor:
            
            tree.insert("", i, values=(row[1], row[3], row[4], row[6]), tags=("even",))
            tree.tag_configure("even",foreground="black",background="#f5f5f5")

        i = i = i + 1
        
        
        btn_select = ttk.Button(frame6, style="submit.TButton", text="SELECT", cursor="hand2",command = lambda: self.borrow_book(tree))
        btn_select.place(x=495, y=610)
        
        btn_back = ttk.Button(frame6,style="link.TButton", text="BACK", cursor="hand2",command=self.welcome)
        btn_back.place(x=630, y=613)
        
        tree.pack()
        frame_data2.place(x=70, y=279)
        
        frame6.pack()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Return Detail
    def return_detail(self, tree):
    
        new2=Toplevel(window)
        new2.geometry("1230x700")
        new2.title("Return a Book")
        new2.resizable(False,False)
        
        image = Label(new2, image = return_detail)
        image.place(x=0, y=0, relwidth=1, relheight=1)
        
        selected_item = tree.focus()
        values = tree.item(selected_item, "values")
        print(values)
        
        
        name_detail = Entry(new2, width=22,bg="#d9d9d9", font=("Franklin Gothic Demi", 20))
        name_detail.place(x=210, y=240)
        
        book_detail = Entry(new2, width=22,bg="#d9d9d9", font=("Franklin Gothic Demi", 20))
        book_detail.place(x=210, y=300)
        
        
        name_detail.insert(0, values[0])
        book_detail.insert(0, values[5])
        
        
        def returning():
            
            mycursor.execute(f"SELECT * FROM borrow WHERE uniq_code ='{code_detail.get()}'" )
            result = mycursor.fetchone()
            
            if result:
                for item in tree.selection():
                    mycursor.execute(f"DELETE from borrow WHERE uniq_code = '{code_detail.get()}'")

                mydb.commit()
                
                tree.delete(item)
                mb.showinfo("Success", "Thankyou for returning the book")
                self.administrator1()
            else:
                mb.showerror("Error", "Invalid Code")
                
            self.Return()
        
        code_detail = Entry(new2, width=22,bg="#d9d9d9", font=("Franklin Gothic Demi", 20))
        code_detail.place(x=135, y=490)
        #135
        btn_return = ttk.Button(new2, style="submit.TButton", text="RETURN", cursor="hand2",command = returning)
        btn_return.place(x=250, y=545)
        
        btn_back = ttk.Button(new2,style="con.TButton", text="BACK", cursor="hand2",command=self.Return)
        btn_back.place(x=240, y=590)
        
        
        window.mainloop()
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Return Window
    def Return(self):
        for i in self.master.winfo_children():
            i.destroy()
        
        
        frame= Frame(window, width=1230, height=700)
        image = Label(frame, image = return_book)
        image.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame_data1 = Frame(frame, width=1230, height=700)
        frame_data1.place(x=65, y=190)
        
        mycursor.execute("SELECT * FROM borrow ORDER BY id ASC")
        
        #scroll vertical

        
        #scroll tree horizontal
        tree_scrollh = ttk.Scrollbar(frame_data1, orient="horizontal")
        tree_scrollh.pack(side=BOTTOM, fill='x')
        
        tree=ttk.Treeview(frame_data1, xscrollcommand=tree_scrollh.set, height=15)
        tree['show'] = 'headings'
        vsb = ttk.Scrollbar(frame_data1, orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y, side=RIGHT)
        #configure scrollbar
        tree_scrollh.config(command=tree.xview)
        
        # Define number of columns
        tree["columns"]=("name", "year", "section", "id_number", "course", "title", "isbn", "genre", "shelf_number", "date_borrowed", "date_returned")
        #Assign the width,minwidth and anchor to the respective columns
        tree.column("name", width=200, minwidth=250, anchor="center")
        tree.column("year", width=50, minwidth=100, anchor="center")
        tree.column("section", width=100, minwidth=200, anchor="center")
        tree.column("id_number", width=100, minwidth=200, anchor="center")
        tree.column("course", width=100, minwidth=250, anchor="center")
        tree.column("title", width=200, minwidth=270, anchor="center")
        tree.column("isbn", width=80, minwidth=250, anchor="center")
        tree.column("genre", width=90, minwidth=250, anchor="center")
        tree.column("shelf_number", width=50, minwidth=100, anchor="center")
        tree.column("date_borrowed", width=50, minwidth=100, anchor="center")
        tree.column("date_returned", width=50, minwidth=100, anchor="center")


        #Assign the heading names to the respective columns
        tree.heading("name",text="NAME",anchor="center")
        tree.heading("year", text="YEAR",anchor="center")
        tree.heading("section", text="SECTION",anchor="center")
        tree.heading("id_number",text="ID NUMBER",anchor="center")
        tree.heading("course", text="COURSE",anchor="center")
        tree.heading("title", text="TITLE",anchor="center")
        tree.heading("isbn", text="ISBN",anchor="center")
        tree.heading("genre", text="GENRE",anchor="center")
        tree.heading("shelf_number", text="SHELF NUMBER",anchor="center")
        tree.heading("date_borrowed", text="DATE BORROWED", anchor="center")
        tree.heading("date_returned",text="DATE RETURNED", anchor="center")
        
        i = 0
        mycursor.execute("SELECT * FROM borrow ORDER BY id ASC")
        for row in mycursor:
            tree.insert("", i, values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]), tags=("smoke",))
            tree.tag_configure("smoke",foreground="black",background="#f5f5f5")

        i = i = i + 1
        
        btn_select = ttk.Button(frame, style="submit.TButton", text="SELECT", cursor="hand2",command = lambda: self.return_detail(tree))
        btn_select.place(x=495, y=600)
        
        btn_back = ttk.Button(frame, style="link.TButton", text="BACK", cursor="hand2",command=self.welcome)
        btn_back.place(x=630, y=603)
        
        tree.pack()
        frame.pack()

#------------------------------------------------------------------------------------------------------------------------------------------------



Main(window)
window.mainloop()
