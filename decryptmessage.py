def decrypt(encrypted_message):
    answer = []
    code = "8251220"
    i = 0
    idx = 0
    #print(chr(ord(encrypted_message[(i):(i+1)])))
    while i < len(encrypted_message):
        #print(chr(ord(encrypted_message[i])))
        #if not a letter
        if not encrypted_message[i].isalpha():
            answer.append(chr(ord(encrypted_message[i])))
        else:
            #if upper case
            if encrypted_message[i].istitle():
                answer.append(chr(((ord(encrypted_message[i]) - 65 - int(code[idx])) % 26) + 65))
                idx = (idx + 1)%len(code)

            #else lower case
            else:
                answer.append(chr(((ord(encrypted_message[i]) - 97 - int(code[idx])) % 26) + 97))
                idx = (idx + 1)%len(code)

        i += 1
    return "".join(answer)