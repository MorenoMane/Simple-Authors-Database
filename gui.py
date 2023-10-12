import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect('app.db')
    return conn

# Function to insert appointment data into the database
def insert_appointment():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO Appointments(App_Num, Date, Patient_ID, Doc_ID) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (app_num_entry.get(), date_entry.get(), patient_id_entry.get(), doc_id_entry.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Appointment created successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to update appointment data in the database
def update_appointment():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "UPDATE Appointments SET Date=?, Patient_ID=?, Doc_ID=? WHERE App_Num=?"
        cursor.execute(query, (date_entry.get(), patient_id_entry.get(), doc_id_entry.get(), app_num_entry.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Appointment updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete appointment data from the database
def delete_appointment():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "DELETE FROM Appointments WHERE App_Num=?"
        cursor.execute(query, (app_num_entry.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Appointment deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to perform INNER JOIN between Appointments and PATIENT_INFO tables
def join_appointments_patients():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM Appointments INNER JOIN PATIENT_INFO ON Appointments.Patient_ID = PATIENT_INFO.Patient_ID"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        appointments_text.delete(1.0, tk.END)
        for row in rows:
            appointments_text.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to perform INNER JOIN between Appointments and Doctors tables
def join_appointments_doctors():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM Appointments INNER JOIN Doctors ON Appointments.Doc_ID = Doctors.Doc_ID"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        appointments_text.delete(1.0, tk.END)
        for row in rows:
            appointments_text.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to display all data from the PATIENT_INFO table
def display_patients():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM PATIENT_INFO"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        appointments_text.delete(1.0, tk.END)
        for row in rows:
            appointments_text.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to display all data from the Doctors table
def display_doctors():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM Doctors"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        appointments_text.delete(1.0, tk.END)
        for row in rows:
            appointments_text.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_appointment_by_key():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM Appointments WHERE App_Num = ?"
        cursor.execute(query, (app_num_entry.get(),))
        row = cursor.fetchone()
        conn.close()
        if row:
            appointments_text.delete(1.0, tk.END)
            appointments_text.insert(tk.END, f"{row}\n")
        else:
            messagebox.showinfo("Result", "Appointment not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main application window
app = tk.Tk()
app.title("Appointments GUI")

# Labels and Entry widgets for appointment information
tk.Label(app, text="Appointment Number:").grid(row=0, column=0)
app_num_entry = tk.Entry(app)
app_num_entry.grid(row=0, column=1)

tk.Label(app, text="Date:").grid(row=1, column=0)
date_entry = tk.Entry(app)
date_entry.grid(row=1, column=1)

tk.Label(app, text="Patient ID:").grid(row=2, column=0)
patient_id_entry = tk.Entry(app)
patient_id_entry.grid(row=2, column=1)

tk.Label(app, text="Doctor ID:").grid(row=3, column=0)
doc_id_entry = tk.Entry(app)
doc_id_entry.grid(row=3, column=1)

tk.Label(app, text="Search Appointment by Key:").grid(row=9, column=0)
search_key_entry = tk.Entry(app)
search_key_entry.grid(row=9, column=1)

# Text widget to display appointments data from the database
appointments_text = tk.Text(app, width=70, height=10)
appointments_text.grid(row=4, columnspan=2)

# Buttons to perform actions on appointment data
tk.Button(app, text="Create Appointment", command=insert_appointment).grid(row=5, column=0)
tk.Button(app, text="Update Appointment", command=update_appointment).grid(row=6, column=0)
tk.Button(app, text="Delete Appointment", command=delete_appointment).grid(row=6, column=1)
tk.Button(app, text="Search", command=search_appointment_by_key).grid(row=9, column=2)


# Buttons to perform JOIN operations
tk.Button(app, text="Join Appointments & Patients", command=join_appointments_patients).grid(row=7, column=0)
tk.Button(app, text="Join Appointments & Doctors", command=join_appointments_doctors).grid(row=7, column=1)

# Buttons to display all data from the PATIENT_INFO and Doctors tables
tk.Button(app, text="Display Patients", command=display_patients).grid(row=8, column=0)
tk.Button(app, text="Display Doctors", command=display_doctors).grid(row=8, column=1)

# Start the main event loop
app.mainloop()
