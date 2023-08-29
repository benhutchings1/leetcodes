#
# Number 12 Leet Code Problem
# Integer to Roman
#

def intToRoman(num: int) -> str:
    conv = {
        "I":1,
        "IV":4,
        "V":5,
        "IX":9,
        "X":10,
        "XL":40,
        "L":50,
        "XC":90,
        "C":100,
        "CD":400,
        "D":500,
        "CM":900,
        "M":1000
    }
    # Remove largest possible value at a time
    out = ""
    while num != 0:
        for rn, val in reversed(conv.items()):
            if val <= num:
                out += rn
                num -= val
                break
    return out

print(intToRoman(20))