import pickle
a={}
d=[]
c=[]
with open("new.pickle","rb") as f:
    new=pickle.load(f)
for i in new:
    print(i["username"])
    b=input("y or n?\n")
    if b=="y":
        a[i["username"]]=i["password"]
        c.append(i["username"])
    else:
        d.append(i)
with open("name_password.pickle","wb") as f:
    pickle.dump(a,f)
with open("not_admin.pickle","wb") as f:
    pickle.dump(c,f)
with open("new.pickle","rb") as f:
    pickle.dump(d,f)
