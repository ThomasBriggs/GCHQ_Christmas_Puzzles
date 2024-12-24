text = "ISKGWIM KSWEBDU BN DFN LBIGSKSE BM IKBCWKBQX W QSWEBDU BDEBLWNBFD NF XFO MFQPBDU NGBM WECBNNSEQX ESPBFOM BDBNBWQQX ODKSWEWAQS CSMMWUS"

subs = {
    "I" : "P",
    "S" : "E",
    "K" : "R",
    "G" : "H",
    "W" : "A",
    "M" : "S",
    "K" : "R",
    "E" : "D",
    "B" : "I",
    "D" : "N",
    "U" : "G",
    
    # "C" : "M",
    # "L" : "C",
    # "N" : "T",
    # "F" : "O",
    # "Q" : "L",
    # "X" : "Y",
    # "O" : "U",
    # "P" : "V",
    # "A" : "B"
}

def sub(text, subs):
    output = []
    for i in text:
        if i == " ":
            output.append(" ")
        elif i in subs:
            output.append(subs[i])
        else:
            output.append("_")
    return "".join(output)

print(sub(text, subs))
print(text)

# print(sorted(list(subs.values())))
        

