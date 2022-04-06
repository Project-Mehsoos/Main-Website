from flask import Flask, render_template, request, redirect
import email_getter
print ("Importing successfully done")
app = Flask(__name__, template_folder="main")

@app.route("/")
def home():
    return render_template("main_website.html")

@app.route("/project_mehsoos")
def mehsoos():
    return render_template("project_mehsoos.html")

@app.route("/submit" , methods = ["GET" , "POST"])
def new_user():
    if request.method == "POST":
        name = request.form['Name1']
        email = request.form['Email1']
        
        email_getter.add_id(name , email)
        print ("Redirected from main website")
    return redirect("/#newsletter")

@app.route("/message" , methods = ["GET" , "POST"])
def send_mail_main():
    if request.method == "POST":
        name = str(request.form['Name2'])
        email = str(request.form['Email2'])
        message = str(request.form['Message2'])
        
        body = f'''
Name    : {name}
Email   : {email}
Message : {message}'''
        
        print (body)
        
        #email_sender.send_email(body)
        print ("Redirected from main contact form")
        
    return redirect("/?#contact")

@app.route("/project_mehsoos/contact" , methods = ["GET" , "POST"])
def send_mail_mehsoos():
    if request.method == "POST":
        name = request.form['Name']
        email = request.form['Email']
        message = request.form['Message']
        
        body = f'''
Name    : {name}
Email   : {email}
Message : {message}'''
        
        print (body)
        
        #email_sender.send_email(body)
        print ("Redirected from project mehsoos website")
        
    return redirect("/project_mehsoos?#connect")
        
if __name__ == "__main__":
    app.run(debug=True)
    
