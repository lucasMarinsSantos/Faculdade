print ("Splita e separa!\n")
import re

texto1 = re.sub(r"[^A-Za-z0-9\s]", "", '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you''').lower().split()
texto2 = [] 
py = tuple("python")
for palavra in texto1:
    if palavra[0] in py or palavra[-1] in py:
        texto2.append(palavra)
print (texto2)