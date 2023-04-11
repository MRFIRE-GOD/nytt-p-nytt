import tkinter as tk
import sqlite3
from tkinter import messagebox


class CustomerGUI:
    def __init__(self, master):
        root.geometry("500x500")
        root.configure(background='#ADD8E6')
        self.master = master
        master.title("Customer Management System")

        # create labels and entry customer_numgets for input fields
        self.name_label = tk.Label(master, text="Name")
        self.name_entry = tk.Entry(master)

        self.password_label = tk.Label(master, text="Password")
        self.password_entry = tk.Entry(master, show="*")

        self.email_label = tk.Label(master, text="Email")
        self.email_entry = tk.Entry(master)

        self.phone_label = tk.Label(master, text="Phone")
        self.phone_entry = tk.Entry(master)

        self.address_label = tk.Label(master, text="Address")
        self.address_entry = tk.Entry(master)

        # create buttons for add, show, and delete users
        self.add_customer_to_db = tk.Button(master, text="Add  ", height= 2, width=15, command=self.add_customer_to_db )
        self.delete_customer_from_db = tk.Button(master, text="Delete",height= 2, width=20, command=self.delete_customer_from_db)
        self.show_button = tk.Button(master, text="Show ",height= 2, width=20, command=self.show_customer)

        # pack the customer_numgets onto the frame
        self.name_label.pack()
        self.name_entry.pack()
        self.name_label.config(fg="black")


        self.password_label.pack()
        self.password_entry.pack()
        self.password_label.config(fg="black")

        self.email_label.pack()
        self.email_entry.pack()
        self.email_label.config(fg="black")


        self.phone_label.pack()
        self.phone_entry.pack()
        self.phone_label.config(fg="black")


        self.address_label.pack()
        self.address_entry.pack()
        self.address_label.config(fg="black")

        

        self.add_customer_to_db.pack()
        self.add_customer_to_db.config(fg="black")
        self.add_customer_to_db.configure(bg="light blue")
        self.add_customer_to_db.config(font=("TkDefaultFont", 10))




        self.delete_customer_from_db.pack()
        self.delete_customer_from_db.config(fg="black")
        self.delete_customer_from_db.configure(bg="light blue")
        self.delete_customer_from_db.config(font=("TkDefaultFont", 10))
        




        self.show_button.pack()
        self.show_button.config(fg="black")
        self.show_button.configure(bg="light blue")
        self.show_button.config(font=("TkDefaultFont", 10))
        





        

    def show_customer(self):
        def display_customer():
            
            try:
                customer_num = int(customer_num_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid customer number")
                return

            conn = sqlite3.connect('1db1.db')
            c = conn.cursor()

            # Query database for customer information
            query = f"SELECT * FROM users WHERE customer_num = '{customer_num}'"
            c.execute(query)
            customer = c.fetchone()

            # Display customer information this look wierd but i dont want to see the password
            if customer:
                nr_label.config(text=f"NR: {customer[0]}")
                name_label.config(text=f"Name: {customer[1]}"),
                email_label.config(text=f"Email: {customer[3]}"),
                phone_label.config(text=f"Phone: {customer[4]}"),
                address_label.config(text=f"Address: {customer[5]}")
            else:
                nr_label.config(text="customer not found")
                name_label.config(text=""),
                email_label.config(text=""),
                phone_label.config(text=""),
                address_label.config(text=""),

            conn.close()

        # create a new window for input and display
        customer_window = tk.Toplevel(self.master)
        customer_window.geometry("500x500")
        customer_window.configure(bg="light blue")
        customer_window.title("Show Customer")

        customer_num_label = tk.Label(customer_window, text="Enter Customer number:")
        customer_num_entry = tk.Entry(customer_window)
        submit_button = tk.Button(customer_window, text="Submit", command=display_customer)

        # create labels to display customer information
        nr_label = tk.Label(customer_window, text="")
        name_label = tk.Label(customer_window, text="")
        email_label = tk.Label(customer_window, text="")
        phone_label = tk.Label(customer_window, text="")
        address_label = tk.Label(customer_window, text="")

        nr_label.config(font=("TkDefaultFont", 16))
        nr_label.config(fg="red")

        name_label.config(font=("TkDefaultFont", 16))
        name_label.config(fg="red")

        email_label.config(font=("TkDefaultFont", 16))
        email_label.config(fg="red")

        phone_label.config(font=("TkDefaultFont", 16))
        phone_label.config(fg=("red"))

        address_label.config(font=("TkDefaultFont", 16))
        address_label.config(fg="red")


    # grid the widgets
        customer_num_label.grid(row=0, column=0)
        customer_num_entry.grid(row=0, column=1)
        submit_button.grid(row=1, column=1)
        nr_label.grid(row=1, column=0, columnspan=2)
        name_label.grid(row=3, column=0, columnspan=2)
        email_label.grid(row=4, column=0, columnspan=2)
        phone_label.grid(row=5, column=0, columnspan=2)
        address_label.grid(row=6, column=0, columnspan=2)

    

    def add_customer_to_db(self):
        """
        This method adds a new customer to the database.
        """
        conn = sqlite3.connect('1db1.db')
        c = conn.cursor()

        customer_name = self.name_entry.get()
        customer_password = self.password_entry.get()
        customer_email = self.email_entry.get()
        customer_phone = self.phone_entry.get()
        customer_address = self.address_entry.get()

        # Check if the username already exists in the database
        query = f"SELECT username FROM users WHERE username='{customer_name}'"
        c.execute(query)
        result = c.fetchone()

        if result:
            # If the username already exists, display an error message
            messagebox.showerror("Error", f"{customer_name} is already taken. Please choose a different username.")
        else:
            # If the username is available, add the new customer to the database
            query = f"INSERT INTO users (username, password, email, phone, address) VALUES ('{customer_name}', '{customer_password}', '{customer_email}', '{customer_phone}', '{customer_address}')"
            c.execute(query)

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", f"{customer_name} has been added to the customer database.")



    def delete_customer_from_db(self):
        def display_customer():
            customer_num = customer_num_entry.get()

            conn = sqlite3.connect('1db1.db')
            c = conn.cursor()

        # Check if the customer exists
            query = f"SELECT * FROM users WHERE customer_num = '{customer_num}'"
            c.execute(query)
            customer = c.fetchone()

        # Delete the customer if it exists
            if customer:
                query = f"DELETE FROM users WHERE customer_num = '{customer_num}'"
                c.execute(query)
                conn.commit()

                result_label.config(text="Customer deleted successfully.")
                result_label.config(fg="green")

            else:
                result_label.config(text="Customer not found.")
                result_label.config(fg="red")

            conn.close()

    # create a new window for input and display
        customer_window = tk.Toplevel(self.master)
        customer_window.geometry("500x500")
        customer_window.configure(bg="#FFCCCB")
        customer_window.title("Delete Customer")

        customer_num_label = tk.Label(customer_window, text="Enter Customer Number To Delete:")
        customer_num_label.config(fg="red")
        customer_num_entry = tk.Entry(customer_window)
        submit_button = tk.Button(customer_window, text="DELETE", command=display_customer)
        submit_button.config(fg="green")


        result_label = tk.Label(customer_window, text="")
        customer_num_label.grid(row=0, column=0)
        customer_num_entry.grid(row=0, column=1)
        submit_button.grid(row=1, column=1)
        result_label.grid(row=2, column=0, columnspan=2)



root = tk.Tk()
CustomerGUI = CustomerGUI(root)
root.mainloop()