from flask import Flask, render_template,request

import XGBClassifier as xgbclassifier

app =Flask(__name__)

@app.route("/",methods=['GET','POST'])
def marks():
    if request.method=="POST":
       
        gender = request.form.get('gender')
        #if gender = female
        #first col =1 ,sec col =0
        #if gender=male
        #first col =0 ,sec col =1
        if gender == "female":
            genderBinary=[1,0]
        elif gender=="male":
            genderBinary=[0,1]

        #hmoglobin
        hmg=float(request.form['hmg'])
        #Pack cell volume
        pckcv=float(request.form['pckcv'])
        #Red blood cell
        rbc=float(request.form['rbc'])
        #Mean Corpuscular volume(fl)
        mcv=float(request.form['mcv'])
        #Mean Corpuscular hemoglobin(pg)
        mch=float(request.form['mch'])
        #Mean Corpuscular hemoglobin concentration
        mchc=float(request.form['mchc'])
        #Red Blood cell distribution width
        rbcdw=float(request.form['rbcdw'])

        #White Blood cell count
        wbcc=float(request.form['wbcc'])

        #Neutrophils
        nphils=float(request.form['nphils'])
        #Lymphocytes
        lcytes=float(request.form['lcytes'])
        #Platelets
        platelets=float(request.form['platelets'])
        #HemoglobinA
        hmga=float(request.form['hmga'])
        #HemoglobinA2
        hmga2=float(request.form['hmga2'])
        #Hemoglobin F
        hmgf=float(request.form['hmgf'])

       # let array[0][0]=gender
        inputData=[]
        inputData=[genderBinary[0],genderBinary[1],hmg,pckcv,rbc,mcv,mch,mchc,rbcdw,wbcc,nphils,lcytes,platelets,hmga,hmga2,hmgf]

        print("the array is: ",inputData) 

        predicted=xgbclassifier.predictions(inputData)
        mp=predicted
    else:
        mp="-----"
     
    return render_template("index.html", my_pred = mp)


# @app.route("/sub",methods=['POST'])
# def submit():
#   if request.method == "POST":
#       name = request.form["username"]
#       return render_template("sub.html", n=name)

if __name__ == "__main__":
     app.run(debug=True)