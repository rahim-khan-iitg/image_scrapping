from flask import Flask,render_template,request
from functions import *
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=="POST":
        key=request.form.get('keyword')
        get_data(key)
        list_img=os.listdir("./static/images")
        list_img=["./static/images/"+i for i in list_img]
        return render_template("index.html",image=list_img)
    return render_template("index.html",image=[])

app.run(debug=True)