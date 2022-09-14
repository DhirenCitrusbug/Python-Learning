import re

txt = "htls35 jkjjkjjkj 394j ijd jkjjkj ER%343222 43OP2328932"
x = re.findall("[A-Z]{2}[\d]{7}",txt)
print(x)
x = re.search("jkj",txt)
print(x.group())


txt = "htls35 jkjjkjjkj 394j ijd jkjjkj ER.#343222 43OP2328932"
x = re.findall("[A-Z]{2}[^A-Za-z0-9\s]{2}[\d]{2}",txt)
print(x)



t = "The rain in Spain"
c = re.compile("\s")
y = re.sub("\s",'9',t)
print(y)