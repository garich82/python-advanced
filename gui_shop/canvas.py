from tkinter import Tk, Canvas


def create_root():
    root_inner = Tk()
    root_inner.geometry("700x600")
    root_inner.title("GUI Shop")
    root_inner.resizable(False, False)

    return root_inner


def create_frame():
    frame_inner = Canvas(root, width=700, height=700)
    frame_inner.grid(row=0, column=0)

    return frame_inner


root = create_root()
frame = create_frame()