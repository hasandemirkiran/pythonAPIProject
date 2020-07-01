#This function checks if the given userid is int and between 1-10, not string of float 
def checkInputFormat(userID):
    if(isinstance(userID, int)):
        if(userID < 11 and userID > 0):
            return True
        else:
            return False 
    else:
        return False