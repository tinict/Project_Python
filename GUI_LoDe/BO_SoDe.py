import random

Nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
Memory = [];

def check(Memory, str):
    for i in Memory: 
        if (i == str):
            return 1;
    return 0;

def Giai7(Nums):
    Winner = [];
    for i in range(0,4):
        num = str(random.choice(Nums)) + str(random.choice(Nums));
        while(check(Memory, num) != 0):
            num = str(random.choice(Nums)) + str(random.choice(Nums));
        Memory.append(num);
        Winner.append(num);
    return Winner;

def Giai6(Nums):
    Winner = [];
    for i in range(0,3):
        num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        while(check(Memory, num) != 0):
            num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        Memory.append(num);
        Winner.append(num);
    return Winner;
        
def Giai5(Nums):
    Winner = [];
    for i in range(0,6):
        num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        while(check(Memory, num) != 0):
            num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        Memory.append(num);
        Winner.append(num);
    return Winner;

def Giai4(Nums):
    Winner = [];
    for i in range(0,4):
        num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        while(check(Memory, num) != 0):
            num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        Memory.append(num);
        Winner.append(num);
    return Winner;

def Giai3(Nums):
    Winner = [];
    for i in range(0,6):
        num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        while(check(Memory, num) != 0):
            num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        Memory.append(num);
        Winner.append(num);
    return Winner;

def Giai2(Nums):
    Winner = [];
    for i in range(0,2):
        num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        while(check(Memory, num) != 0):
            num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        Memory.append(num);
        Winner.append(num);
    return Winner;

def Giai1(Nums):
    Winner = [];
    for i in range(0,1):
        num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        while(check(Memory, num) != 0):
            num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        Memory.append(num);
        Winner.append(num);
    return Winner;

def GiaiDD(Nums):
    Winner = [];
    for i in range(0,1):
        num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        while(check(Memory, num) != 0):
            num = str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums)) + str(random.choice(Nums));
        Memory.append(num);
        Winner.append(num);
    return Winner;
