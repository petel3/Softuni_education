import re
pattern = r"\b_[A-Za-z]+\b"
text=input()
valid_variables=re.findall(pattern,text)
print(",".join([variables[1:] for variables in valid_variables]))