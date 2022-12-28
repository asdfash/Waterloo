import hashlib

salt = 86879426
A_hash = "cd01a419235b5e283b12b7da8bbf53d04c89231c169d6ca4594227cde0ffa85e"
word_list = open('word_list.txt').read().split()
special_ls = "!?*$#&"

def brute(salt, A_hash, word_list, special_ls):
    hashcount = 0
    for word in word_list:
        if len(word) == 7:
            number = 0000
            while number < 10000:
                wordnum = word.capitalize() + str(number)
                for char in special_ls:
                    pw = wordnum + char
                    hashcount += 1
                    prefixedpw = str(salt) + pw
                    if str(hashlib.sha256(prefixedpw.encode('utf-8')).hexdigest()) == A_hash:
                        print("Password: " + str(pw))
                        print("Hashcount: " + str(hashcount))
                        return
                number += 1
        elif len(word) == 8:
            number = 000
            while number < 1000:
                wordnum = word.capitalize() + str(number)
                for char in special_ls:
                    pw = wordnum + char
                    hashcount += 1
                    prefixedpw = str(salt) + pw
                    if str(hashlib.sha256(prefixedpw.encode('utf-8')).hexdigest()) == A_hash:
                        print("Password: " + str(pw))
                        print("Hashcount: " + str(hashcount))
                        return
                number += 1
        elif len(word) == 9:
            number = 00
            while number < 100:
                wordnum = word.capitalize() + str(number)
                for char in special_ls:
                    pw = wordnum + char
                    hashcount += 1
                    prefixedpw = str(salt) + pw
                    if str(hashlib.sha256(prefixedpw.encode('utf-8')).hexdigest()) == A_hash:
                        print("Password: " + str(pw))
                        print("Hashcount: " + str(hashcount))
                        return
                number += 1
        elif len(word) == 10:
            number = 0
            while number < 10:
                wordnum = word.capitalize() + str(number)
                for char in special_ls:
                    pw = wordnum + char
                    hashcount += 1
                    prefixedpw = str(salt) + pw
                    if str(hashlib.sha256(prefixedpw.encode('utf-8')).hexdigest()) == A_hash:
                        print("Password: " + str(pw))
                        print("Hashcount: " + str(hashcount))
                        return
                number += 1

brute(salt, A_hash, word_list, special_ls)