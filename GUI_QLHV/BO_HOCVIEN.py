def CheckNullInput():
    return;

def Sex(str):
    if (str == 'Male'):
        return 1;
    elif(str == 'Female'):
        return 0;
    else:
        return 3;
    
def SexConvert(str):
    if (str == 1):
        return 'Male';
    elif (str == 0):
        return 'Female';
    else:
        return 'Unknown';
    

