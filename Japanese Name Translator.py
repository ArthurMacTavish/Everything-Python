# Defines Var_Namedata_...
Var_Initial_NameData_naviteNormalName = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
Var_Initial_NameData_japanLikeName = ["ka", "zu", "mi", "te", "ku", "lu", "ji", "ri", "ki", "zu", "me", "ta", "rin", "to", "mo", "no", "ke", "shi", "ari", "chi", "do", "ru", "mei", "na", "fu", "z", "Ka", "Zu", "Mi", "Te", "Ku", "Lu", "Ji", "Ri", "Ki", "Zu", "Me", "Ta", "Rin", "To", "Mo", "No", "Ke", "Shi", "Ari", "Chi", "Do", "Ru", "Mei", "Na", "Fu", "Z", " "]

# Predefined Process
def nameBreakdown():
    global Var_nameBreakdown_Splitted
    Var_nameBreakdown_Splitted = list(UsrIn_NameData_nativeNormalName)

def getMaxValue():
    global Var_getMaxValue_MaxVal
    Var_getMaxValue_MaxVal = len(Var_nameBreakdown_Splitted)

def getValueIdentifier():
    global Var_getValueIdentifier_ValueID
    Var_getValueIdentifier_ValueID = []
    Var_getValueIdentifier_LooperAnchor = 0
    while Var_getValueIdentifier_LooperAnchor < Var_getMaxValue_MaxVal:
        Var_getValueIdentifier_ValueID.append(Var_Initial_NameData_naviteNormalName.index(Var_nameBreakdown_Splitted[Var_getValueIdentifier_LooperAnchor]))
        Var_getValueIdentifier_LooperAnchor = Var_getValueIdentifier_LooperAnchor + 1

def resembleName():
    global Var_resembleName_FinalName
    Var_resembleName_FinalName = (Var_Initial_NameData_japanLikeName[Var_getValueIdentifier_ValueID[0]])
    Var_resembleName_LooperAnchor = 1
    while Var_resembleName_LooperAnchor < Var_getMaxValue_MaxVal:
        Var_resembleName_FinalName = Var_resembleName_FinalName + (Var_Initial_NameData_japanLikeName[Var_getValueIdentifier_ValueID[Var_resembleName_LooperAnchor]])
        Var_resembleName_LooperAnchor = Var_resembleName_LooperAnchor + 1

# Magic Code
UsrIn_NameData_nativeNormalName = input('Type your name here: ')
nameBreakdown()
getMaxValue()
getValueIdentifier()
resembleName()
print("Here's your Japanese Name: " + Var_resembleName_FinalName)