import pickle

def return_dict():
    try:
        with open("data.dat" , "rb") as f:
            email_dict = pickle.load(f)
    
    except EOFError:
        email_dict = {}
        
    return email_dict

def add_id(name : str , email: str):
    dictionary = return_dict()
    dictionary[email] = name
    
    with open("data.dat" , "wb") as f:
        pickle.dump(dictionary, f)
        