from RegexGenerator import RegexGenerator

Date1 = open("Mach_MSGID.txt", "r")

lines = Date1.readlines()
ArrRegex= []

f = open("Regex/"+"Regex-"+"MachMsgId"+".txt","a")
for i in range(0, len(lines)):
    theRegex = RegexGenerator(lines[i])
    ArrRegex.append(theRegex)
    f.write(ArrRegex+'\n')
    print(ArrRegex[i].get_regex())