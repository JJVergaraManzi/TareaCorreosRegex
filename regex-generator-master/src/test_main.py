import main

Date1 = open("Mach_MSGID.txt", "r")

lines = Date1.readlines()
for i in range(0, len(lines)):
    a = generate_regex(lines)
    print(a)

    b = display_group(lines)
    print(b)

    c = extend_characters_list(lines)
    print(c)
