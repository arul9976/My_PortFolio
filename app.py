a = 'hAck3rr4nk'

def decryptPass(passwd):
    print(passwd)
    decrypt = []

    def Func(dcrypted, text):
        num = any([char.isdigit() for char in dcrypted])
        Uchar = any([char.isupper() for char in dcrypted])
        Lchar = any([char.islower() for char in dcrypted])
        if(num and Uchar and Lchar):
            rmovingChr = [char for char in passwd if char not in dcrypted]
            # print(rmovingChr)
            b = f"{dcrypted}*"
            decrypt.append(b)
            findChr(''.join(rmovingChr))
            
        else:
            rmovingChr = text[2:]
            a = ''.join(f'{dcrypted}0')
            decrypt.append(a)
            findChr(rmovingChr)

    def findChr(text):
        decrypting = []
        for lcase in text:
            if lcase.isdigit() and len(decrypting) < 4:
                decrypting.append(lcase)
                decrypting.reverse()

        for lcase in text:
            if lcase.isupper() and len(decrypting) < 4:
                decrypting.append(lcase)


        for lcase in text:
            if lcase.islower() and len(decrypting) < 4:
                decrypting.append(lcase)
                n = [char for char in decrypting if char.islower()]
                if(len(n) > 1):
                    decrypting = []
                    Func(''.join(n), text)
                    break

        password = ''.join(decrypting)
        decrypting = []
        # decrypt.append(password)
        return password
    Func(findChr(passwd), '')
    return ''.join(decrypt)[:-1]
    
print(decryptPass(a))