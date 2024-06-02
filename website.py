from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS (app)
@app.route("/")
def hello_world():
    return "<p>Hello, World! 22228 yepta!</p>"



@app.route("/blala")
def info():
    return "Imformation about this site"

@app.route("/about")
def about():
    return "<i>This site was made yesterday</i>"

@app.route("/dividing")
def dividing():
    num1= int(request.args.get("num1"))
    num2= int(request.args.get("num2"))
    
    return f"if we take {num1} and divide it on {num2} we gonna get {num1 / num2}"
    

@app.route("/encrypt")
def encryption():
    input_text= request.args.get("input_text") 
    input_key= int(request.args.get("input_key"))
    output_text=encrypt(input_text, input_key)
    return {"succes":True, "encrypted_text": output_text}


def encrypt(text, key):
    output_txt = ""
    for c in text:
        address = ord(c) - 32
        address2 = address + key
        output_txt = output_txt + chr(address2 % 96 + 32)
    print(output_txt)
    return output_txt

app.run(host="0.0.0.0", port=9004)


