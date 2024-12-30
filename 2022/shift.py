def shift(input, shift_amount):

    output = []
    mod_shift_amount = abs(shift_amount) % 26
    mod_shift_amount = int(mod_shift_amount * (shift_amount/abs(shift_amount)))
    for i in input:
        if (i != " " and i != "."):
            output.append(chr(ord(i)+(mod_shift_amount)))
        else:
            output.append(i)

    return "".join(output)

print(shift("xibu4xpset beesftt jt", -1))
print(shift("pvucpbse.hsje.sfkpjot", -1))