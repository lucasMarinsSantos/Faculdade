print ("Splita e conta!\n")

import re

texto1 = re.sub(r"[^A-Za-z0-9\s]", "", '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you''').lower().split()

py = tuple("python")
texto2 = []

for palavra in texto1:
    if len(palavra) > 4 and any(letra in py for letra in palavra):
        texto2.append(palavra)
print (texto2)