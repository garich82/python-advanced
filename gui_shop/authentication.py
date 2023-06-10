from tkinter import Button, Entry
from canvas import root, frame
from helpers import clean_screen


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        width=20,
        height=3,
        borderwidth=0,
        command=register
    )

    login_button = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        width=20,
        height=3,
        borderwidth=0
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 315, window=login_button)


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")