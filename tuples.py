tuple = ("english", "maths", "bio", "chem", "geo", "PE")

print(tuple)

s1,s2,s3,s4,s5,s6 = tuple

print(f"Subject 1 : {s1}")
print(f"Subject 2 : {s2}")
print(f"Subject 3 : {s3}")
print(f"Subject 4 : {s4}")
print(f"Subject 5 : {s5}")
print(f"Subject 6 : {s6}")

print(tuple[1:4])
print(tuple[:5])
print(tuple[2:])
print(tuple[:])

nes_t=(2,3,4,54,3,12,3,[7,4,2,3],(54,3,5))
nes_t[7][0]=6
print(nes_t[7])