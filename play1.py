from tkinter import *
from tkinter import ttk
from exercise1 import *


# reset the tree view
def reset_tree():
    global tree
    tree = ttk.Treeview(root)
    tree["columns"] = ("account_num", "balance", "limit")
    tree.column("account_num", width=150)
    tree.column("balance", width=150)
    tree.column("limit", width=150)
    tree.heading("#0", text="Name")
    tree.heading("account_num", text="Account Number")
    tree.heading("balance", text="Balance")
    tree.heading("limit", text="Overdraft Limit")


# update the tree view
def update_tree():
    tree.delete(*tree.get_children())
    for i in range(0, len(dictionary_of_accounts), 1):
        account = list(dictionary_of_accounts.values())[i]
        name = account.name
        account_number = account.account_number
        balance = account.get_balance()
        limit = account.credit_line
        tree.insert("", i, account_number, text=name, values=(account_number, balance, limit))
    tree.event_generate("<FocusOut>")


# select an element from the tree
def selected_tree(*args):
    global selected_item
    global selected_account
    selected_account = None
    action_frame.pack()
    selected_item = tree.item(tree.focus())
    selected_values = selected_item['values']
    if selected_values == "":
        return
    selected_number = selected_values[0]
    selected_account = dictionary_of_accounts[selected_number]


# when the user chose an option (deposit, withdraw or transfer)
def change_dropdown(*args):
    option = tkvar.get()
    action_frame.pack()
    WDTFrame.grid(row=3, column=1)
    selected_tree(None)
    if option == "Deposit":
        withdraw_button.pack_forget()
        transfer_button.pack_forget()
        to_account_label.pack_forget()
        to_account_entry.pack_forget()
        deposit_button.pack(side=LEFT)
    if option == "Withdraw":
        deposit_button.pack_forget()
        transfer_button.pack_forget()
        to_account_label.pack_forget()
        to_account_entry.pack_forget()
        withdraw_button.pack(side=LEFT)
    if option == "Transfer":
        withdraw_button.pack_forget()
        deposit_button.pack_forget()
        to_account_label.pack(side=LEFT)
        to_account_entry.pack(side=LEFT)
        transfer_button.pack(side=LEFT)


# when the user clicked on the deposit button
def deposit_clicked(account, amount):
    if account is None:
        print("choose an account to deposit to")
        return
    if not amount.isdigit():
        print("the amount should be a positive number")
        return
    account.deposit(int(amount))
    update_tree()


# when the user clicked on the withdraw button
def withdraw_clicked(account, amount):
    if account is None:
        print("choose an account to withdraw from")
        return
    if not amount.isdigit():
        print("the amount should be a positive number")
        return
    account.withdraw(int(amount))
    update_tree()


# when the user clicked on the transfer button
def transfer_clicked(account, amount, another_account):
    if account is None:
        print("choose an account to transfer from")
        return
    if not amount.isdigit():
        print("the amount should be a positive number")
        return
    if not another_account.isdigit():
        print("the number of the other account should be a positive number")
        return
    if int(another_account) not in dictionary_of_accounts.keys():
        print("the account you wanted to transfer to (number " + another_account + "), is not in the dictionary")
        return
    account.transfer(int(amount), dictionary_of_accounts[int(another_account)])
    update_tree()

# create the root frame
root = Tk()

# create, reset and update the tree view
reset_tree()
update_tree()
tree.pack()

# connect left mouse click event to "selected_tree" function
tree.bind("<ButtonRelease-1>", selected_tree)

# create the action frame
action_frame = Frame(root)

# create the string variable
tkvar = StringVar(action_frame)

# the choices of the drop down menu
choices = {"Deposit", "Withdraw", "Transfer"}

# set the default option
tkvar.set("Choose Action")

# create the drop down menu
popupMenu = OptionMenu(action_frame, tkvar, *choices)
popupMenu.grid(row=2, column=1)

# action lable
Label(action_frame, text="Action").grid(row=1, column=1)

# link function to change drop down
tkvar.trace('w', change_dropdown)

# create the withdraw deposit transfer frame
WDTFrame = Frame(action_frame)

# create and set the amount label
amount_label = Label(WDTFrame, text="Amount: ")
amount_label.pack(side=LEFT)

# create and set the amount entry
amount_entry = Entry(WDTFrame)
amount_entry.pack(side=LEFT)

# create the withdraw button
withdraw_button = Button(WDTFrame, text="Withdraw",
                         command=lambda: withdraw_clicked(selected_account, amount_entry.get()))

# create the deposit button
deposit_button = Button(WDTFrame, text="Deposit",
                        command=lambda: deposit_clicked(selected_account, amount_entry.get()))

# create the transfer button
transfer_button = Button(WDTFrame, text="Transfer",
                         command=lambda: transfer_clicked(selected_account, amount_entry.get(), to_account_entry.get()))

# create the to_account label
to_account_label = Label(WDTFrame, text="To Account: ")

# create the to_account entity
to_account_entry = Entry(WDTFrame)

# start the GUI
root.mainloop()
