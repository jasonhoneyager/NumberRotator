#############Number Rotator#############

def CaptureNumbers():
    ListObtained = False
    while not ListObtained:
        try:
            PrimaryArray = [int(List) for List in input("Please Enter Your Numbers, separted by a space: ").split(" ")]
        except ValueError:
            print("Please Enter Numbers Only: ")
            continue
        else:
            print("Your Original List is:",PrimaryArray)
            ListObtained = True 
    return PrimaryArray

def RotateRight(PrimaryArray):
    Rotation = 0
    while Rotation < 2:
        MoveRight = PrimaryArray.pop()
        PrimaryArray.insert(0, MoveRight)
        Rotation += 1
    RotatedArray = PrimaryArray
    print("Your Rotated List is:",RotatedArray)
    return RotatedArray     

def Addition(RotatedArray):
    AddedArray = [Digit + 5 for Digit in RotatedArray]
    print("Your Rotated List + 5 is:",AddedArray)    

def RunCode():
    PrimaryArray = CaptureNumbers()
    RotatedArray = RotateRight(PrimaryArray)
    Addition(RotatedArray)
    
##########################################################################################################

RunCode()