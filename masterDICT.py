#MASTER DICTIONNAIRE
#1
dik = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
val = list(dik.values())
print(val)
#2
val = input("Tape yon valè: ")
if val.startswith("{") and val.endswith("}"):
    print("Valè a gen akolad devan ak dèyè.")
else:
    print("Valè a pa gen akolad devan ak dèyè.")
#3
dik = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
k = dik.keys()
for key in k:
    print(key)
#4
dik = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
v = dik.values()
for val in v:
    print(val)
#5
dik= {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
new_dik = dict(dik)
print(new_dik)
#6
dik = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}
for kle, valè in dik.items():
    if isinstance(valè, str):  # Tcheke si valè a se yon chenn
        dik[kle] = '_' + valè + '_'
print(dik)
#7
import re
dik = {"a": "12", "b": "abc", "c": "12r", "d": "90"}
new_dik = {}
for kle, valè in dik.items():
    if re.match('^\d+$', valè):  
        new_dik[kle] = valè
print(new_dik)
#8
dik = {"a": 1, "b": 2}
lis_tipl = [(kle, valè) for kle, valè in dik.items()]
print(lis_tipl)
#9
lis_tipl = [("a", 1), ("b", 2)]
dik = {kle: valè for kle, valè in lis_tipl}
print(dik)
#10
dik1 = {"a": 1, "b": 2, "c": 3}
dik2 = {"b": 10, "c": 20, "d": 30}
new_dik = {}
for kle, valè in dik1.items():
    if kle in dik2:
        new_dik[kle] = str(valè) + str(dik2[kle])
print(new_dik)
