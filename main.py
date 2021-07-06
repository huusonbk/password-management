import random
from tkinter import *
from tkinter import messagebox
import json

def save():
    website = input_web.get()
    email = input_email.get()
    password = input_pw.get()
    if len(website) ==0:
        website_ok = messagebox.showinfo(title="Missing website",message="Type website di mày")
    elif len(email) == 0:
        email_ok = messagebox.showinfo(title="Missing email", message="Type email di mày")
    elif len(password) ==0:
        password_ok = messagebox.showinfo(title="Missing password",message="Type password di mày")
    else:
        new_data = { website: {"email":email,
                               'password':password
                               }}

        is_ok = messagebox.askokcancel(title=website, message= f"Please check your Account/Password:\nEmail: {email}\nPassword: {password}\nIs it ok ma?")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    # reading old data
                    data = json.load(data_file)
                    # update old data with new data
                    data.update(new_data)
                    with open("data.json", "w") as data_file:
                        # saving
                        json.dump(data, data_file, indent=4)
            except:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            finally:
                input_web.delete(0, END)
                input_pw.delete(0, END)

def search_pass():
    web = input_web.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            if len(data[web]) > 0:
                messagebox.showinfo(title=f"{web}",message=f"website: {web}\nemail: {data[web]['email']}\npassword: {data[web]['password']}")

        except:
            messagebox.showinfo(title="error",message="No information")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
#Password Generator Project
def pw_generate():
    input_pw.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw_letter = [random.choice(letters) for char in range(nr_letters)]
    pw_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    pw_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = pw_letter + pw_symbols + pw_numbers

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char


    print(f"Your password is: {password}")
    input_pw.insert(END, password)

    return password


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# My pass
canvas = Canvas(width=200, height=200, highlightthickness=1)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# time_text = canvas.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME, 35 ,"bold"))
canvas.grid(column=1, row=0)

# website_label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
# email_user
email_user = Label(text="Email/Username:")
email_user.grid(row=2, column=0)
# Password
password = Label(text="Password:")
password.grid(row=3, column=0)


# Website input
input_web = Entry()
input_web.grid(column=1, row=1,sticky="EW")
input_web.focus()

# Email input
input_email= Entry()
input_email.grid(column=1, row=2, columnspan=2,sticky="EW")
input_email.insert(END, "huusonbkhcm@gmail.com")

# Password input
input_pw= Entry()
input_pw.grid(column=1, row=3,sticky="EW")

# Generate button
search_button = Button(text="Search", command = search_pass)
search_button.grid(column=2, row=1,sticky="EW")


# Generate button
generate_button = Button(text="Generate Password", command = pw_generate)
generate_button.grid(column=2, row=3,sticky="EW")

# Add button
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2,sticky="EW")

window.mainloop()