def right_justify(a):
    t=70-len(a)
    ans=" "*t+a
    print(ans)
print("Enter String: ")
a=input()
right_justify(a)
