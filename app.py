from tkinter import *
from mydb import Database
from tkinter import messagebox

class NLPApp:
    
    def __init__(self):
        #create db object
        self.db = Database()
        
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
        # clearing gui first
        self.gui_clear()
        
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
        login_button = Button(self.root, text="Login", width=30, height=2, command=self.perform_login)
        login_button.pack(pady=(10, 10))
        
        # register page ref
        label3 = Label(self.root, text="Not registered yet? Register here...")
        label3.pack(pady=(30, 10))
        register_button = Button(self.root, text="Register", width=30, height=2, command=self.register)  # when button clicked go to register gui
        register_button.pack()
        
    def register(self):
        print("Register Page") # checking in terminal button clicked or not
        
        # clearing GUI first
        self.gui_clear()
        
        
        # Adding Header top of the App
        header = Label(self.root, text="NLP APP", bg="lightgray", fg="BLUE")
        header.pack(pady=(30, 30))
        header.config(font=("vardana", 24, "bold"))
        
        # Name
        label = Label(self.root, text="Enter your name")
        label.pack(pady=(10, 10))
        self.name = Entry(self.root, width=50)
        self.name.pack(pady=(10, 10), ipady=4)
        
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
        
        # Register button
        register_btn = Button(self.root, text="Register", width=30, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))
        
        # Login page ref
        label3 = Label(self.root, text="Already Registered? Login...")
        label3.pack(pady=(30, 10))
        login_btn = Button(self.root, text="Login", width=30, height=2, command=self.login)  # when button clicked go to register gui
        login_btn.pack()
        

    def gui_clear(self):
        
        # looping through all packs and removing one by one from existing GUI
        for pack in self.root.pack_slaves():
            # print(pack)
            pack.destroy()
            
    def perform_registration(self):
        
        # Fetch data from GUI
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()
        
        response = self.db.add_data_to_db(name, email, password)
        
        # response from db
        if response:
            # print("Registration Successful")
            messagebox.showinfo("success", "Registration Successful! You can now login.")
        else:
            # print("Email already exists.")
            messagebox.showerror("error", "Email already exist. Try with another email")
    
    def perform_login(self):
        
        # Fetch data from GUI
        email = self.email.get()
        password = self.password.get()
        
        response = self.db.check_data_to_db(email, password)
        
        # response from db
        if response:
            messagebox.showinfo("success", "Login successful")
            self.home()
        else:
            messagebox.showerror("error", "Incorrect username or password.")
            
    def home(self):
        self.gui_clear()
        
        # Adding Header top of the App
        header = Label(self.root, text="NLP APP", bg="lightgray", fg="BLUE")
        header.pack(pady=(30, 30))
        header.config(font=("vardana", 24, "bold"))
        
        # Sentiment Analysis
        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=30, height=2, command=self.sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))
        
        # Name Entity Recognition
        ner_btn = Button(self.root, text="Name Entity Recognition", width=30, height=2, command=self.name_entity_recognition)
        ner_btn.pack(pady=(10, 10))
        
        # Emotion Prediction
        emotion_btn = Button(self.root, text="Emotion Analysis", width=30, height=2, command=self.emotion_prediction)
        emotion_btn.pack(pady=(10, 10))
        
        
        # logout button
        logout_btn = Button(self.root, text="logout", width=30, height=2, command=self.login)
        logout_btn.pack(pady=(30, 10))
        
    
    def sentiment_analysis(self):
        pass
    
    def name_entity_recognition(self):
        pass
    
    def emotion_prediction(self):
        pass
        
nlp = NLPApp()