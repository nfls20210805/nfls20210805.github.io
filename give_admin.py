import pickle
a=[]
with open("not_admin.pickle","rb") as f:
    new=pickle.load(f)
for i in new:
    print(i)
    b=input("y or n?\n")
    if b=="y":
        a.append(i)
with open("admin.pickle","wb") as f:
    pickle.dump(a,f)
