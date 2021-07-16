import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    y=int(jsonObj['y'])
    m=int(jsonObj['m'])
    d=int(jsonObj['d'])
    k=""    
    if(y%4==0):
        if(y%100==0):
            if(y%400==0):
                k=k+'leapyear'
        else:
            k=k+'leapyear'

   #l initialization 
    if m in (1, 3, 5, 7, 8, 10, 12):
        l= 31
    elif m == 2:
        if k=='leapyear':
               l = 29
        else:
                l = 28
    else:
        l = 30
    if(d>l and m>12):
        response+="<b>Enter Correct date </b><br>"
    else:
        if d < l:
            d += 1
        else:
            d = 1
            if m == 12:
                m = 1
                y += 1
        
            else:
                m += 1

               
        response+="<b> The next date is [yyyy-mm-dd] <b>"+str(y)+"-"+str(m)+"-"+str(d)+"</b><br>" 
   
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
