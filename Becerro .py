import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import csv

# Define colors
BG_COLOR = "red"
BUTTON_COLOR = "#87CEEB"  # Sky blue color
TEXT_COLOR = "black"

def add_bill():
    bill_name = bill_name_entry.get()
    due_date = due_date_entry.get()

    if not bill_name or not due_date:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    # Append bill details to the listbox
    bill_details = f"{bill_name} - Due: {due_date}"
    bill_listbox.insert(tk.END, bill_details)

    # Clear entry fields after adding bill
    bill_name_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)

def delete_bill():
    # Get the selected bill from the listbox
    selected_index = bill_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Warning", "Please select a bill to delete.")
        return
    bill_listbox.delete(selected_index)

def remind_bills():
    # Get current date
    current_date = datetime.now().date()

    # Check if any bills are due today
    for i in range(bill_listbox.size()):
        bill_details = bill_listbox.get(i)
        due_date_str = bill_details.split(" - Due: ")[1]
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        if due_date == current_date:
            bill_name = bill_details.split(" - Due: ")[0]
            messagebox.showinfo("Bill Reminder", f"Don't forget to pay your {bill_name} today!")

# Create main window
root = tk.Tk()
root.title("Bill Reminder")
root.configure(bg=BG_COLOR)  # Set background color

# Bill Name
bill_name_label = tk.Label(root, text="Bill Name:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10, "bold"))
bill_name_label.grid(row=0, column=0, padx=5, pady=5)
bill_name_entry = tk.Entry(root)
bill_name_entry.grid(row=0, column=1, padx=5, pady=5)

# Due Date
due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):", bg=BG_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10, "bold"))
due_date_label.grid(row=1, column=0, padx=5, pady=5)
due_date_entry = tk.Entry(root)
due_date_entry.grid(row=1, column=1, padx=5, pady=5)

# Add Bill Button
add_bill_button = tk.Button(root, text="Add Bill", command=add_bill, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10, "bold"))
add_bill_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Delete Bill Button
delete_bill_button = tk.Button(root, text="Delete Bill", command=delete_bill, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10, "bold"))
delete_bill_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Bill Listbox
bill_listbox = tk.Listbox(root, width=50)
bill_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Remind Bills Button
remind_bills_button = tk.Button(root, text="Remind Bills", command=remind_bills, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 10, "bold"))
remind_bills_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()