#
# Number 13 Leet Code Problem
# Roman To Integer
#

def romanToInt(s: str) -> int:
    # Number conversions
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
    output = 0
    idx = 0
    while idx < len(s):
        # Detect binumerals
        if idx < len(s) - 1 and (conv[s[idx+1]] > conv[s[idx]]):
            output += conv[s[idx] + s[idx+1]]
            idx += 1
        else:
            output += conv[s[idx]]
        idx += 1
    return output
    
romanToInt("LIV")
    
    