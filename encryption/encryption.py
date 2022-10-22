

def caesarEncrypt(text: str, offsets: int) -> str:

    lowerCase: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperCase: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    res = ""
    for i in text:
        if i in lowerCase:
            res += lowerCase[(lowerCase.index(i) + offsets) % 26]
        elif i in upperCase:
            res += upperCase[(upperCase.index(i) + offsets) % 26]
        else:
            res += i
    return res


input_text = input()
print(caesarEncrypt(input_text, 14))
