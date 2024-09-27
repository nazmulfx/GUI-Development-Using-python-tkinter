from tkinter import *

class NLPApp:
    
    def __init__(self):
        
        # login GUI Load
        self.root = Tk()
        self.root.title("NLP App")
        # self.root.iconbitmap("resources/favicon.ico") #icon
        self.root.geometry("500x500")
        self.root.config(bg="lightgray")
        
        # my methods
        self.login()
        
        # this will be below
        self.root.mainloop()    # holding GUI in the screen
        
    def login(self):
        
        # Adding Header top of the App
        header = Label(self.root, text="NLP APP", bg="lightgray", fg="BLUE")
        header.pack(pady=(30, 30))
        header.config(font=("vardana", 24, "bold"))
        
        # email
        label1 = Label(self.root, text="Enter your Email")
        label1.pack(pady=(10, 10))
        self.email = Entry(self.root, width=50)
        self.email.pack(pady=(10, 10), ipady=4)
        
        # password
        label2 = Label(self.root, text="Enter your password")
        label2.pack(pady=(10, 10))
        self.password = Entry(self.root, width=50)
        self.password.pack(pady=(10, 10), ipady=5)
        
        #submit button
        button = Button(self.root, text="Login")
        button.pack(pady=(10, 10))
        
        # register page ref
        label3 = Label(self.root, text="Not registered yet? Register here...")
        label3.pack(pady=(30, 10))
        button = Button(self.root, "Register")
        button.pack()
        
nlp = NLPApp()