x=2.0
s=1.0
for k in range(10):
    print(f"At iteration {k} the value of s={s}")
    s = 0.5 * (s + (x/s))
print(f"Finally, the value of s={s}")
