from flask import Flask,render_template,request,jsonify
from utils import DaimondData
import config
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("Diamond_predict_price.html")

@app.route('/test')
def home_page():
    return render_template("test.html")
   
@app.route('/predict_price',methods=['GET','POST'])
def predict_price():
    if request.method == "GET":
        data=request.args.get
        print("Data: ",data)
        carat=eval(data('carat'))
        cut=data('cut')
        clarity=data('clarity')
        depth=eval(data('depth'))
        table=eval(data('table'))
        x=eval(data('x'))
        y=eval(data('y'))
        z=eval(data('z'))
        color=data('color')
        dia=DaimondData(carat,cut,clarity,depth,table,x,y,z,color)
        pred_price=dia.get_predicted_price()
        return render_template("Diamond_predict_price.html",prediction=pred_price)
    
    if request.method=="POST":
        data=request.form
        print("Data: ",data)
        carat=data['carat']
        cut=data['cut']
        clarity=data['clarity']
        depth=data['depth']
        table=data['table']
        x=data['x']
        y=data['y']
        z=data['z']
        color=data['color']
        dia=DaimondData(carat,cut,clarity,depth,table,x,y,z,color)
        pred_price=dia.get_predicted_price()
        return render_template("Diamond_predict_price.html",prediction=pred_price)



    


if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)