import hashlib

def crack_sha1_hash(hash = "", use_salts = False):
    pfile = open("top-10000-passwords.txt", "r", encoding='utf-8')
    for x in pfile:
        pw = x.strip()
        if use_salts:
            sfile = open("known-salts.txt","r",encoding='utf-8')
            for y in sfile:
                newpw = pw+y.strip()
                if hashlib.sha1(str(newpw).encode('utf-8')).hexdigest() == hash:
                    return pw
                newpw = y.strip()+pw
                if hashlib.sha1(str(newpw).encode('utf-8')).hexdigest() == hash:
                    return pw
                
        else:
            if hashlib.sha1(str(pw).encode('utf-8')).hexdigest() == hash:
                return pw


    return "PASSWORD NOT IN DATABASE"

