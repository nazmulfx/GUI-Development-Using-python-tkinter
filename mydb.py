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
                json.dump(database, wf)
            return 1