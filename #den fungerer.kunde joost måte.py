import tkinter as tk
import sqlite3


def delete1():
        global screen3
        screen3 = tk.Toplevel(screen)
        screen3.title("Delete")
        screen3.geometry("300x250")
        tk.Label(screen3, text="Enter kunde_nr to delete").pack()
        kunde_nr_entry = tk.Entry(screen3)
        kunde_nr_entry.pack()
        tk.Button(screen3, text="Delete", command=lambda: delete2(screen3)).pack()
        screen3.destroy()

def delete2(screen3):
        screen3.destroy()


def login_success():
        global screen3
        screen3 = tk.Toplevel(screen)
        screen3.title("Du er har logget inn")
        screen3.geometry("150x100")
        tk.Label(screen3,text="Nå har du logget in").pack()
        tk.Button(screen3, text="OK", command=lambda:[home_screen(), screen3.destroy()]).pack()

def delete3():
    screen4.destroy()

def delete4():
        screen5.destroy()


def password_not_recognized():
    global screen4
    screen4 = tk.Toplevel(screen)
    screen4.title("Feil")
    screen4.geometry("150x100")
    tk.Label(screen4,text="Prøv igjen").pack()
    tk.Button(screen4, text="OK", command=lambda: delete2(screen4)).pack()

def user_not_found():
        global screen5
        screen5 = tk.Toplevel(screen)
        screen5.title("Bruker eksistrer ikke")
        screen5.geometry("150x100")
        tk.Label(screen5,text="Bruker eksistrer ikke").pack()
        tk.Button(screen5, text="OK", command=delete4).pack()

def logout():
        # clear the user's login credentials
    tk.Button(screen6, text="Log ut", command=lambda: logout(username_login_entry)).pack()

        # switch back to the login screen
    screen6.destroy()

def logout(username_entry):
    # clear the user's login credentials
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    # switch back to the login screen
    screen6.destroy()

def home_screen():
    global screen6
    screen6 = tk.Toplevel(screen)
    screen6.title("Hjem side")
    screen6.geometry("1000x1500")

    tk.Label(screen6, text="Velkomen til hjemme side! Den siden jobber vi med. Venligs prøv etter neste oppgave").pack()
    tk.Button(screen6, text="Log ut", command=lambda: logout(username_entry)).pack()

def register_user():
    # Get the user input from the Entry widgets
    username_info = username.get()
    password_info = password.get()
    phone_info = phone.get()
    email_info = email.get()
    address_info = address.get()

    # Connect to the database and create the users table if it doesn't exist
    conn = sqlite3.connect('1db1.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (customer_num INTEGER PRIMARY KEY, username TEXT, password TEXT, phone TEXT, email TEXT, address TEXT)")

    # Get the maximum customer number from the database
    c.execute("SELECT MAX(customer_num) FROM users")
    max_customer_num = c.fetchone()[0]

    # Increment the maximum customer number by 1 to get the new customer number for the new user
    if max_customer_num:
        customer_num = max_customer_num + 1
    else:
        customer_num = 1

    # Check if the username already exists in the database
    c.execute("SELECT * FROM users WHERE username=?", (username_info,))
    if c.fetchone():
        tk.Label(screen1, text="Prøv anne bruker navn!", fg="red", font=("calibri", 11)).pack()
    else:
        # If the username doesn't exist, insert the user's information into the database
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (customer_num, username_info, password_info, phone_info, email_info, address_info))
        conn.commit()

        # Clear the input fields
        username.set("")
        password.set("")
        phone.set("")
        email.set("")
        address.set("")

        tk.Label(screen1, text=f"Registration successful! Your customer number is {customer_num}", fg="green", font=("calibri", 11)).pack()

    conn.close()




def login_verify():
    global home_screen, username_entry, password_entry
    username_info = username_verify.get()
    password_info = password_verify.get()
    username_login_entry.delete(0, tk.END)
    password_login_entry.delete(0, tk.END)

    

    conn = sqlite3.connect('1db1.db')
    
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username_info, password_info))
    if c.fetchone():
        username_entry = username_login_entry
        password_entry = password_login_entry
        login_success()
    else:
        password_not_recognized()

    conn.commit()
    conn.close()

def register():
    global screen1
    screen1 = tk.Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x500")

        # Create the Entry widgets for user input
    global username
    global password
    global phone
    global email
    global address
    username = tk.StringVar()
    password = tk.StringVar()
    phone = tk.StringVar()
    email = tk.StringVar()
    address = tk.StringVar()

    tk.Label(screen1, text="Venligs fyll ut: ").pack()
    tk.Label(screen1, text="").pack()
    tk.Label(screen1, text="Username *").pack()
    username_entry = tk.Entry(screen1, textvariable=username)
    username_entry.pack()
    tk.Label(screen1, text="Password *").pack()
    password_entry = tk.Entry(screen1, show="*", textvariable=password)
    password_entry.pack()
    tk.Label(screen1, text="Phone number").pack()
    phone_entry = tk.Entry(screen1, textvariable=phone)
    phone_entry.pack()
    tk.Label(screen1, text="Email address").pack()
    email_entry = tk.Entry(screen1, textvariable=email)
    email_entry.pack()
    tk.Label(screen1, text="Address").pack()
    address_entry = tk.Entry(screen1, textvariable=address)
    address_entry.pack()
    tk.Button(screen1, text="Register", command=register_user).pack()

def login():
    global screen2
    screen2 = tk.Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x500")
    tk.Label(screen2, text="Venligs fyll ut: ").pack()
    tk.Label(screen2, text="").pack()
    global username_verify
    global password_verify

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    global username_login_entry
    global password_login_entry

    tk.Label(screen2, text="Username *").pack()
    username_login_entry = tk.Entry(screen2, textvariable=username_verify)
    username_login_entry.pack()
    tk.Label(screen2, text="Password *").pack()
    password_login_entry = tk.Entry(screen2, show="*", textvariable=password_verify)
    password_login_entry.pack()
    tk.Label(screen2, text="").pack()
    tk.Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()
    tk.Button(screen2, text="Register", width=10, height=1, command=register).pack()

def main_screen():
    global screen
    screen = tk.Tk()
    screen.geometry("500x500")
    screen.title("Velkommen")

    tk.Label(text="Velkommen til Applikasjon").pack()
    tk.Label(text="").pack()
    tk.Button(text="Login", height="2", width="30", command=login).pack()
    tk.Label(text="").pack()
    tk.Button(text="Register", height="2", width="30", command=register).pack()


    screen.mainloop()
main_screen()