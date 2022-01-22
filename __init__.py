from flask import*
import pickle

app=Flask(__name__)

app.secret_key = 'vdfunvugueehwufety834whr9u34wi3jirw3icjkfsnvsguwehtu39eiir9283'

with open("new.pickle","rb") as f:
    new=pickle.load(f)

with open("admin.pickle","rb") as f:
    admin=pickle.load(f)

with open("name_password.pickle","rb") as f:
    n_p=pickle.load(f)

with open("name.pickle","rb") as f:
    allname=pickle.load(f)

@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/loginagain")
def loginagain():
    return render_template("login_again.html")

@app.route("/admin")
def foradmin():
    return render_template("admin.html")

@app.route('/main')
def main():
    return render_template("main.html",name=session["username"])

@app.route("/goregister")
def goregister():
    return render_template("register.html")

@app.route("/different")
def different():
    return render_template("different.html")

@app.route("/goregister/register",methods=["POST"])
def register():
    name=request.form.get("username")
    pas=request.form.get("password")
    repa=request.form.get("repassword")
    if name in allname:
        return redirect("/samename")
    else:
        if pas==repa:
            user={"username":name,"password":pas}
            new.append(user)
            allname.append(name)
            with open("name.pickle","wb") as f:
                pickle.dump(allname,f)
            with open("new.pickle","wb") as f:
                pickle.dump(new,f)
            return redirect('/index')
        else:
            return redirect("/different")
            
@app.route("/samename")
def samename():
    return render_template("same_name.html")
            
@app.route("/gocp")
def gocp():
    return render_template("change_password.html")

@app.route("/w/<n>")
def welcome(n):
    return render_template("welcome.html",name=n)

@app.route("/wp")
def wp():
    return render_template("without_password.html")

@app.route("/wn")
def wn():
    return render_template("without_username.html")

@app.route("/rp")
def rp():
    return render_template("wrong_password.html")

@app.route("/rn")
def rn():
    return render_template("wrong_username.html")

@app.route("/gologin")
def gologin():
    return render_template("login.html")

@app.route("/gologin/login",methods=["POST"])
def login():
    name=request.form.get("username")
    pas=request.form.get("password")
    if name:
        if pas:
            if name in n_p:
                if n_p[name]==pas:
                    flag=0
                    for ad in admin:
                        if name==ad:
                            flag=1
                            break
                    if flag==1:
                        session["username"]="admin"
                        return redirect("/admin")
                    else:
                        session["username"]=name
                        return redirect(url_for("welcome",n=name))
                else:
                    return redirect("/rp")
            else:
                return redirect("/rn")
        else:
            return redirect("/wp")
    else:
        return redirect("/wn")

@app.route("/gocp/cp",methods=["POST"])
def cp():
    name=request.form.get("username")
    pas=request.form.get("password")
    newpas=request.form.get("newpassword")
    if name:
        if pas:
            if name in n_p:
                if n_p[name]==pas:
                    n_p[name]=newpas
                    return redirect("/loginagain")
                else:
                    return redirect("/rp")
            else:
                return redirect("/rn")
        else:
            return redirect("/wp")
    else:
        return redirect("/wn")

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/index")

app.run(host="0.0.0.0")
















































