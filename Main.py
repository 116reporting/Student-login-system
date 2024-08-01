from tkinter import *
from tkinter import messagebox
import mysql.connector

# Database connection
mydatabase = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='Bloodysweet19',
    database='student'
)
mycur = mydatabase.cursor()
print("Connected to Database")

# Create table if not exists
mycur.execute("""
    CREATE TABLE IF NOT EXISTS login (
        rollnumber INT(10), 
        username VARCHAR(255), 
        password VARCHAR(255), 
        admissionno INT(10), 
        class VARCHAR(10), 
        phnumber VARCHAR(10), 
        email VARCHAR(255), 
        city VARCHAR(100), 
        hobby VARCHAR(255), 
        result INT(10)
    )
""")

background = "#06283D"
framebg = "#EDEDED"
framefg = "06283D"
exit_mode = False
trialCount = 0

def trial():
    global trialCount
    trialCount += 1
    print("TrialCount is ", trialCount)
    if trialCount >= 3:
        messagebox.showerror("Warning", "You have exceeded the login attempt limit!")
        root.destroy()

def register():
    root.destroy()
    regtkin = Tk()
    regtkin.title("Register System")
    regtkin.geometry("1280x720")
    regtkin.config(bg=background)
    regtkin.resizable(False, False)

    regframe = Frame(regtkin, bg="red")
    regframe.pack(fill=Y)

    backgroundimage = PhotoImage(file="images/Details.png")
    Label(regframe, image=backgroundimage).pack()

    # Entry fields and labels
    fields = [
        ("Username", "Enter Your User Name"),
        ("Password", "Enter Your Password"),
        ("Roll Number", "Enter Your Roll Number"),
        ("Admission Number", "Enter Your Admission Number"),
        ("Class and Section", "Enter Your Class and Section"),
        ("Phone Number", "Enter Your Phone Number"),
        ("Email", "Enter Your Email"),
        ("City", "Enter Your City"),
        ("Hobby", "Enter Your Hobby"),
        ("10th Result", "Enter Your 10th Result")
    ]
    
    entries = {}
    y_pos = 150
    
    for field, placeholder in fields:
        label = Label(
            regtkin, text=field, fg="#fff", bg="#155CA2",
            borderwidth=5, relief="groove", font=('Arial', 20, 'bold'), width=16
        )
        label.place(x=250, y=y_pos)
        
        entry = Entry(
            regtkin, width=30, fg="#375174", border=0, bg="#fff", font=('Arial Bold', 24)
        )
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda e, p=placeholder, ent=entry: ent.delete(0, 'end') if ent.get() == p else None)
        entry.bind("<FocusOut>", lambda e, p=placeholder, ent=entry: ent.insert(0, p) if ent.get() == '' else None)
        entry.place(x=550, y=y_pos)
        
        entries[field] = entry
        y_pos += 50
    
    def submit():
        values = {field: ent.get().strip() for field, ent in entries.items()}
        
        # Input validation
        for field, val in values.items():
            if val == '' or val == f"Enter Your {field}":
                messagebox.showerror("Entry Error", f"Enter your {field}")
                return
        
        if not values['Roll Number'].isdigit() or not values['Admission Number'].isdigit() or not values['Phone Number'].isdigit():
            messagebox.showerror("Entry Error", "Roll Number, Admission Number, and Phone Number should be in numbers")
            return
        
        if not values['Email'].endswith('@gmail.com'):
            messagebox.showerror("Entry Error", "Enter a proper Email ending with @gmail.com")
            return
        
        query_insert_val = "INSERT INTO login (rollnumber, username, password, admissionno, class, phnumber, email, city, hobby, result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val_list = (
            values["Roll Number"], values["Username"], values["Password"], values["Admission Number"], 
            values["Class and Section"], values["Phone Number"], values["Email"], 
            values["City"], values["Hobby"], values["10th Result"]
        )
        mycur.execute(query_insert_val, val_list)
        mydatabase.commit()
        messagebox.showinfo("Connection", "Registered Successfully")
        messagebox.showinfo("Connection", "You can now Login!!!")
        regtkin.destroy()

    registerbutton = Button(
        regtkin, text="SUBMIT", bg="#6237CF", fg="#fff", width=50, height=2, command=submit
    )
    registerbutton.place(x=470, y=660)
    
    regtkin.mainloop()

def loginuser():
    username = user.get()
    password = code.get()
    
    if username in ["UserID", "", " "] or password in ["Password", "", " "]:
        messagebox.showerror("Entry Error", "Type Username and Password")
    else:
        try:
            mydb = mysql.connector.connect(
                host='localhost', user='root', password='Bloodysweet19', database="student"
            )
            mycursor = mydb.cursor()
            print("Connected to Database")
        except:
            messagebox.showerror("Connection", "Database connection not established")
            return
        
        mycursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (username, password))
        myresult = mycursor.fetchone()
        
        if myresult is None:
            messagebox.showinfo("Invalid", "Invalid UserID or Password")
            trial()
        else:
            messagebox.showinfo("Login", "Successfully Logged in!")
            root.destroy()

            tkin = Tk()
            tkin.title("User Details")
            tkin.geometry("1280x720")
            tkin.config(bg=background)
            tkin.resizable(False, False)

            frame = Frame(tkin, bg="red")
            frame.pack(fill=Y)
            backgroundimage = PhotoImage(file="images/Details.png")
            Label(frame, image=backgroundimage).pack()

            topic = f"Details About {myresult[1]}"
            label = Label(
                tkin, text=topic, fg="#fff", bg="#5FC7FC", font=('Arial', 24, 'bold')
            )
            label.place(x=500, y=70)

            labels_texts = [
                ("Name", myresult[1]),
                ("Roll Number", myresult[0]),
                ("Admission Number", myresult[3]),
                ("Class", myresult[4]),
                ("Phone Number", myresult[5]),
                ("Email", myresult[6]),
                ("City", myresult[7]),
                ("Hobby", myresult[8]),
                ("10th Result", myresult[9])
            ]
            
            y_pos = 165
            for label_text, user_info in labels_texts:
                label = Label(
                    tkin, text=label_text, fg="#fff", bg="#155CA2", borderwidth=5,
                    relief="groove", font=('Arial', 20, 'bold'), width=16
                )
                label.place(x=250, y=y_pos)

                value_label = Label(
                    tkin, text=user_info, fg="#fff", bg="#155CA2", borderwidth=5,
                    relief="groove", font=('Arial', 20, 'bold'), width=22
                )
                value_label.place(x=700, y=y_pos)
                
                y_pos += 55
            
            tkin.mainloop()

root = Tk()
root.title("Login System")
root.geometry("1280x720")
root.config(bg=background)
root.resizable(False, False)

frame = Frame(root, bg="red")
frame.pack(fill=Y)

backgroundimage = PhotoImage(file="images/Details.png")
Label(frame, image=backgroundimage).pack()

Label(root, text="User Login", fg="#fff", bg="#5FC7FC", font=('Arial', 24, 'bold')).place(x=500, y=70)

# Username
Label(root, text="Username", fg="#fff", bg="#155CA2", borderwidth=5, relief="groove",
      font=('Arial', 20, 'bold'), width=16).place(x=250, y=150)

user = Entry(root, width=30, fg="#375174", border=0, bg="#fff", font=('Arial Bold', 24))
user.insert(0, 'UserID')
user.bind("<FocusIn>", lambda e: user.delete(0, 'end') if user.get() == 'UserID' else None)
user.bind("<FocusOut>", lambda e: user.insert(0, 'UserID') if user.get() == '' else None)
user.place(x=550, y=150)

# Password
Label(root, text="Password", fg="#fff", bg="#155CA2", borderwidth=5, relief="groove",
      font=('Arial', 20, 'bold'), width=16).place(x=250, y=200)

code = Entry(root, width=30, fg="#375174", border=0, bg="#fff", font=('Arial Bold', 24), show='*')
code.insert(0, 'Password')
code.bind("<FocusIn>", lambda e: code.delete(0, 'end') if code.get() == 'Password' else None)
code.bind("<FocusOut>", lambda e: code.insert(0, 'Password') if code.get() == '' else None)
code.place(x=550, y=200)

# Buttons
Button(root, text="Login", bg="#6237CF", fg="#fff", width=50, height=2, command=loginuser).place(x=470, y=300)
Button(root, text="Register", bg="#6237CF", fg="#fff", width=50, height=2, command=register).place(x=470, y=370)

root.mainloop()
