from flask import Flask ,render_template,request

from project.utils import PriceDetection

import config

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome Sanket"

@app.route('/test')
def student():

    return render_template("index.html")
        
        
@app.route('/result', methods = ['POST', 'GET'])

def get():

    if request.method == 'POST':

        result = request.form

        CRIM     = result["CRIM"]
        ZN       = result["ZN"]
        INDUS    = result["INDUS"]
        CHAS     = result["CHAS"]
        NOX      = result["NOX"]
        RM       = result["RM"]
        AGE      = result["AGE"]
        DIS      = result["DIS"]
        RAD      = result["RAD"]
        TAX      = result["TAX"]
        PTRATIO  = result["PTRATIO"]
        B        = result["B"]
        LSTAT    = result["LSTAT"]

        

        obj = PriceDetection(CRIM, ZN,INDUS,CHAS,NOX,RM, AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
        data = obj.price_pred()

        return render_template("output.html", data = data)

    








if __name__ == "__main__":
    app.run(debug=True)