from flask import *
app=Flask(__name__)
#........ insert data......
emp=[
    {'id':0,'name':'shalini','address':'kkl'},
    {'id':1,'name':'lini','address':'mtm'},
    {'id': 2, 'name': 'shalu', 'address': 'tn'}
]
# .....create default page......
@app.route('/')
def home():
    return 'welcome'
# ...run....
# .....read the data......
@app.route('/api',methods=['GET'])
def getapi():
    return jsonify(emp)
# .....run...
# ......given to the id get the particular data...
@app.route('/all/emp',methods=['GET'])
def allapi():
    if 'id' in request.args:
        id=int(request.args['id'])
    else:
        return 'error'
    a=[]
    for i in emp:
        if i['id']==id:
            a.append(i)
    return jsonify(a)
# ....run....http://127.0.0.1:5000/all/emp?id=0
# ............post (create)method.......
@app.route('/emp',methods=['POST'])
def createapi():
    emp4={'id':3,'name':'ashika','address':'tvm'}
    emp.append(emp4)
    return jsonify({"created data":emp4})
# ...not run in url,run in postman..
# .....put(update) method....
@app.route('/emp/<int:id>',methods=['PUT'])
def updateemp(id):
    emp[id]['name']='elgin'
    return jsonify({"name updated":emp[id]})
# ....run in postman..http://127.0.0.1:5000/emp/1.
# .......delete the data...
@app.route('/emp/<int:id>',methods=['DELETE'])
def deletedata(id):
    emp.remove(emp[id])
    return jsonify({'data deleted':True})
# .....run......
if __name__=='__main__':
    app.run(debug=True)