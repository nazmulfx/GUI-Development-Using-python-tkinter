import json

class Database:
    
    def add_data_to_db(self, name, email, password):
        
        with open("db.json", "r") as rf:
            database = json.load(rf)   # store existing data by opening file in read format
            
        # checking if the user is exist
        if email in database:
            return 0
        else:
            database[email] = [name, password]
            
            with open("db.json", "w") as wf:
                json.dump(database, wf)     # dump means writing in the database
            return 1
        
    def check_data_to_db(self, email, password):
        
        with open("db.json", "r") as rf:
            database = json.load(rf)
        
        if email in database:
            if database[email][1] == password:
                return 1
            else:
                return 0
        else:
            return 0