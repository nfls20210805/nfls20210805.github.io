import pickle
a={}
c=[]
with open("new.pickle","rb") as f:
    new=pickle.load(f)
for i in new:
    a[i["username"]]=i["password"]
    c.append(i["username"])
    new.remove(i)
with open("name_password.pickle","wb") as f:
    pickle.dump(a,f)
with open("not_admin.pickle","wb") as f:
    pickle.dump(c,f)
