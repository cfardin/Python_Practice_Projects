alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    

def cc(d, t, k):
    k %= 26
    txt = ''
    if d == 'd':
        k*= -1
    for char in t:
        if char in alphabet:
            position = alphabet.index(char)
            txt += alphabet[position + k]
        else:
            txt += char
    return txt



run = True
while run:
    deriction = input("Type 'E' for encode and 'D' for decode : ").lower()
    text = input("Enter the message : ").lower()
    key = int(input("The shift number: "))

    print(cc(deriction, text, key))
    again = input("Do you wanna continue it again ? type Y/N").lower()
    if again == 'n':
        run = False
