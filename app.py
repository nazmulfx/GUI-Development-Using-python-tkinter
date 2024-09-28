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
        self.password = Entry(self.root, width=50, show="*")
        self.password.pack(pady=(10, 10), ipady=5)
        
        #submit button
        login_button = Button(self.root, text="Login", width=30, height=2)
        login_button.pack(pady=(10, 10))
        
        # register page ref
        label3 = Label(self.root, text="Not registered yet? Register here...")
        label3.pack(pady=(30, 10))
        register_button = Button(self.root, text="Register", width=30, height=2, command= self.register())  # when button clicked go to register gui
        register_button.pack()
        
    def register(self):
        print("Register Page") # checking in terminal button clicked or not
        
        # clearing GUI first
        self.gui_clear()
        

    def gui_clear(self):
        
        # looping through all packs and removing one by one from existing GUI
        for pack in self.root.pack_slaves():
            pack.destroy()
        
nlp = NLPApp()