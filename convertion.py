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
    response+="<b> The next date is [yyyy-mm-dd] <b>"+str(y)+"-"+str(m)+"-"+str(d)+"</b><br>" 
   
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
