
from flask import Flask,render_template,url_for,request
from bson.json_util import dumps
from werkzeug.utils import secure_filename

import os
import os.path

import pymongo
import json, ast
import os 
import uuid
import requests
import random 
#import urllib2
import datetime
#import urllib.request
from urllib.request import urlopen
from bson import json_util

from web3 import Web3
import smtplib

from flask_cors import CORS

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))


web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

#var greeterContract = new web3.eth.Contract([{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]);


address = web3.toChecksumAddress("0xb9eB51C2276550846E1F89E11b8a49AA86E9827E")



account_2 = '0x27Ece47447CB623AA002cd831C1e90E7855559Cf' # Fill me in


app = Flask(__name__)
CORS(app)


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["BlockChain"]

userColl = mydb["User"]

rtoColl = mydb["RTO"]

policeColl = mydb["Police"]

fineColl = mydb["Fine"]

coontractColl = mydb["Contract"]

vechileColl = mydb["Vechile"]

complaintColl = mydb["Complaint"]



@app.route('/user/details',methods=['POST'])
def userDetails():

    print("Hello world")
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))


 
 
    myquery = { "userID" : raw["userID"]}


    print(myquery)
    mydoc = userColl.find_one(myquery, {"_id":0})


    print(mydoc)

    if mydoc is not None:
        resp = {"success" : True, "message":"success","userObj": mydoc}
    else:
        return {"success" : False, "message":"Sorry no user found"}

    return resp



@app.route('/user/login',methods=['POST'])
def userLogin():

    print("Hello world")
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    userName = raw["userName"]
    password = raw["password"]
  
    print("here 1")
    print(userName)
    print(password)

 
 
    myquery = { "userName" : userName, "password": password,"approval": "ADMINAPPROVED"}


    print(myquery)
    mydoc = userColl.find_one(myquery, {"_id":0})


    print(mydoc)






    if mydoc is not None:
        resp = {"success" : True, "message":"success","userObj": mydoc}
    else:
        return {"success" : False, "message":"Sorry no user found"}

    return resp

@app.route('/rto/login',methods=['POST'])
def rtoLogin():

    print("Hello world")
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    userName = raw["userName"]
    password = raw["password"]
  
    print("here 1")
    print(userName)
    print(password)

 
 
    myquery = { "userName" : userName, "password": password}


    print(myquery)
    mydoc = rtoColl.find_one(myquery, {"_id":0})


    print(mydoc)

    if mydoc is not None:
        resp = {"success" : True, "message":"success","userObj": mydoc}
    else:
        return {"success" : False, "message":"Sorry no user found"}

    return resp






@app.route('/police/login',methods=['POST'])
def policeLogin():

    print("Hello world")
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    userName = raw["userName"]
    password = raw["password"]
  
    print("here 1")
    print(userName)
    print(password)

 
 
    myquery = { "userName" : userName, "password": password}


    print(myquery)
    mydoc = policeColl.find_one(myquery, {"_id":0})


    print(mydoc)

    if mydoc is not None:
        resp = {"success" : True, "message":"success","userObj": mydoc}
    else:
        return {"success" : False, "message":"Sorry no user found"}

    return resp

@app.route('/user/search',methods=['POST'])
def search():

    print("Hello world")
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    mobile = raw["mobile"]

  
    myquery = { "mobile" : mobile}


    print(myquery)
    mydoc = userColl.find_one(myquery, {"_id":0})


    print(mydoc)






    if mydoc is not None:
        resp = {"success" : True, "message":"success","userObj": mydoc}
    else:
        return {"success" : False, "message":"Sorry no user found"}

    return resp



@app.route('/admin/user/search',methods=['POST'])
def adminSearched():

    print("Hello world")
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    mobile = raw["mobile"]

  
    myquery = { "mobile" : mobile}


    print(myquery)
    mydoc = userColl.find_one(myquery, {"_id":0})


    print(mydoc)






    if mydoc is not None:
        resp = {"success" : True, "message":"success","userObj": mydoc}
    else:
        return {"success" : False, "message":"Sorry no user found"}

    return resp

    
@app.route('/user/register',methods=['POST'])
def registernew():
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
   # gggg=int(datetime.datetime.now().strftime("%s")) * 1000 
    dataUserID = str(uuid.uuid4())
    #before inserting check user is already registered or not
    userColl.insert_one({"userID": dataUserID,"userName": raw["userName"],"password": raw["password"],"approval": "PENDING", "emailID": raw["emailID"],"mobile": raw["mobile"],"address": raw["address"]  ,  "privatekey": raw["privatekey"] ,"accountID": raw["accountID"]  })
    return {"success" : True, "userID": dataUserID}



@app.route('/admin/register',methods=['POST'])
def adminregister():
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    dataUserID = str(uuid.uuid4())
    #before inserting check user is already registered or not
    rtoColl.insert_one({"rtoID": dataUserID,"userName": raw["userName"],"password": raw["password"]})
    return {"success" : True, "userID": dataUserID}




@app.route('/police/register',methods=['POST'])
def policeRegister():
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    dataUserID = str(uuid.uuid4())
    #before inserting check user is already registered or not
    policeColl.insert_one({"policeID": dataUserID,"userName": raw["userName"],"password": raw["password"]})
    return {"success" : True, "userID": dataUserID}



@app.route('/user/raisecomplaint',methods=['POST'])
def userRaiseComplaint():
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    dataUserID = str(uuid.uuid4())
    complaintColl.insert_one({"complaintID": dataUserID,"complaintDesc": raw["complaintDesc"]})
    return {"success" : True}





@app.route('/complaint/list',methods=['GET'])
def userList():
    mydoc = complaintColl.find()
    resp = dumps(mydoc)
    return resp





       
    
@app.route('/user/userID',methods=['POST'])
def findUserbyUserID():

    print("Hello world")
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    userID = raw["userID"]

    print("here 1")
    print(userID)
 
    myquery = { "userID" : userID}
    mydoc = userColl.find_one(myquery, {"_id":0})

    if mydoc is not None:
        resp = {"success" : True, "message":"success","userObj":mydoc}
    else:
        return {"success" : False, "message":"Sorry no user found"}

    return resp



@app.route('/user/getfinedetails',methods=['POST'])
def getFineDetails():

    print("Hello world")
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    userID = raw["userID"]

    print("here 1")
    print(userID)
 
    myquery = { "userID" : userID, "fineStatus": "UNPAID" }
    mydoc = fineColl.find_one(myquery, {"_id":0})

    if mydoc is not None:
        resp = {"success" : True, "message":"success","userObj":mydoc}
    else:
        return {"success" : False, "message":"Sorry no user found"}

    return resp




@app.route('/user/payfine',methods=['POST'])
def payFine():
    print("***********Payfine********")
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))


    myquery = { "userID" : raw["userID"], "fineStatus": "UNPAID" }
    mydoc = fineColl.find_one(myquery, {"_id":0})

    if mydoc is  None:
        print("ddds")
        return{"success" : False, "message":"success","userObj":mydoc}
 




    #gggg=int(datetime.datetime.now().strftime("%s")) * 1000 

    web3.eth.defaultAccount = web3.eth.accounts[0]



    dataUserID = str(uuid.uuid4())
    contract = web3.eth.contract(address=address, abi=abi)
    contractID = contract.functions.greet().call()

    print(contractID)

    coontractDoc = coontractColl.find().sort([('_id', -1)]).limit(1)
    print("hhhh")


    dbContractID =''

    for doc2 in coontractDoc:
        print(doc2)
        dbContractID = doc2.get('contractID')


    print(dbContractID)

    print("kkkk")

    if dbContractID == contractID:
        print("correct")        
        tx_hash = contract.functions.setGreeting(dataUserID).transact()
        coontractColl.insert_one({"contractID":dataUserID})
        #return {"success" : True}
    else:
        print("incorrect")
        #return {"success" : False}

    nonce = web3.eth.getTransactionCount(raw["accountID"])

    print("fdsfsfsdfsfdfdsfsfsfdsfsd")
    print(raw["fineAmount"])
    
    tx = {'nonce': nonce,'to':  account_2,'value': web3.toWei(raw["fineAmount"], 'ether'),'gas': 2000000,'gasPrice': web3.toWei('50', 'gwei'), }
    
    

    signed_tx =web3.eth.account.signTransaction(tx, raw["privatekey"])
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(web3.toHex(tx_hash))

   # fineColl.insert_one({"userID":  raw["userID"],"fineID":  dataFineID,"userName": raw["userName"], "emailID": raw["emailID"],"mobile": raw["mobile"],"address": raw["address"]  ,"accountID": raw["accountID"]  , "fineAmount": raw["fineAmount"]  , "dataTime": gggg})
    myquery = { "userID":  raw["userID"] , "fineStatus": "UNPAID"}

    print("raw")
    print(myquery)
    print(raw["userID"])
    print("rawclose")





    newvalues = { "$set": { "fineStatus": "PAID" } }

    fineColl.update_one(myquery, newvalues)


    return {"success" : True}



@app.route('/register/contract',methods=['POST'])
def registerContract():
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
   # gggg=int(datetime.datetime.now().strftime("%s")) * 1000 
    dataUserID = str(uuid.uuid4())
    contract = web3.eth.contract(address=address, abi=abi)
    contractID = contract.functions.greet().call()

    print(contractID)

    coontractDoc = coontractColl.find().sort([('_id', -1)]).limit(1)
    print("hhhh")


    dbContractID =''

    for doc2 in coontractDoc:
        print(doc2)
        dbContractID = doc2.get('contractID')


    print(dbContractID)

    print("kkkk")

    if dbContractID == contractID:
        print("correct")        
        tx_hash = contract.functions.setGreeting(dataUserID).transact()
        coontractColl.insert_one({"contractID":dataUserID})
        return {"success" : True}
    else:
        print("incorrect")
        return {"success" : False}


    #print(coontractDoc)

    #json_docs = []
    #for doc in coontractDoc:
     #   json_doc = json.dumps(coontractDoc, default=json_util.default)
      #  json_docs.append(json_doc)

    docs_list  = list(coontractDoc)
    dataList = json.dumps(docs_list, default=json_util.default)
   # print(dataList)
   # li = [item.get('contractID') for item in dataList[0]]
   # print(li)


    #before inserting check user is already registered or not
 #   userColl.insert_one({"userID": dataUserID,"userName": raw["userName"],"password": raw["password"], "emailID": raw["emailID"],"mobile": raw["mobile"],"address": raw["address"]  ,  "private_key": raw["private_key"] ,"accountID": raw["accountID"]  , "dataTime": gggg})
    return {"success" : True, "userID": "kk" }


@app.route('/create/fine',methods=['POST'])
def createFine():
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
  #  gggg=int(datetime.datetime.now().strftime("%s")) * 1000 
    dataFineID = str(uuid.uuid4())
    #before inserting check user is already registered or not
    fineColl.insert_one({"userID":  raw["userID"],"fineStatus": "UNPAID","fineID":  dataFineID,"userName": raw["userName"], "fineReason": raw["fineReason"],"emailID": raw["emailID"],"mobile": raw["mobile"],"address": raw["address"]  ,"accountID": raw["accountID"]  , "fineAmount": raw["fineAmount"] })
    fromaddr = 'shivakumarshivu1212@gmail.com'  
    toaddrs  = 'shivakumarshivu1212@gmail.com' 
    b = int(data["fineAmount"]) 
    b=b*100
    string = ""
    string = str(b)
    var = "Fine Has been registerd due to Traffic Rules Violation\nUser name: "+ data["userName"]+ "\n"+ "Fine Reason: "+data["fineReason"] + "\n"+"FineAmount:" + string
    msg = var
    username = 'shivakumarshivu1212@gmail.com'  
    password = 'thankstogmail'

    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.ehlo()
    server.starttls()
    server.login(username, password)  
    server.sendmail(fromaddr, toaddrs, msg)  
    server.quit()
    return {"success" : True, "userID": dataFineID}


"""@app.route('/create/fine',methods=['POST'])
def createFine():
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
  #  gggg=int(datetime.datetime.now().strftime("%s")) * 1000 
    dataFineID = str(uuid.uuid4())
    #before inserting check user is already registered or not
    fineColl.insert_one({"userID":  raw["userID"],"fineStatus": "UNPAID","fineID":  dataFineID,"userName": raw["userName"], "fineReason": raw["fineReason"],"emailID": raw["emailID"],"mobile": raw["mobile"],"address": raw["address"]  ,"accountID": raw["accountID"]  , "fineAmount": raw["fineAmount"] })
    fromaddr = 'shivakumarshivu1212@gmail.com'  
    toaddrs  = 'shivakumarshivu1212@gmail.com'  
    msg = 'Fine created'  

    username = 'shivakumarshivu1212@gmail.com'  
    password = 'thankstogmail'

    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.ehlo()
    server.starttls()
    server.login(username, password)  
    server.sendmail(fromaddr, toaddrs, msg)  
    server.quit()

    return {"success" : True, "userID": dataFineID}"""




@app.route('/user/listfine',methods=['GET'])
def listFine():
    mydoc = fineColl.find()
    resp = dumps(mydoc)
    return resp






@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'




@app.route('/user/admin/approve',methods=['POST'])
def adminApproveUser():
    data = request.get_json()
    print(data)
    raw = ast.literal_eval(json.dumps(data))
    myquery = { "userID":  raw["userID"] }
    #before inserting check user is already registered or not
    newvalues = { "$set": { "approval": "ADMINAPPROVED"} }

    userColl.update_one(myquery, newvalues)

    return {"success" : True}


@app.route('/user/addvechicle',methods=['POST'])
def addvechicle():
    data = request.get_json()
   # print(data)
    raw = ast.literal_eval(json.dumps(data))

    Number = raw["Number"]
    #print(Number)

    #dataUserID = str(uuid.uuid4())
   # before inserting check user is already registered or not
    vechileColl.insert_one({"Number": raw["Number"],"Name": raw["Name"],"Gmail": raw["Gmail"],"Rcnumber": raw["Rcnumber"],"Insurance": raw["Insurance"],"Emession": raw["Emession"],"Gmail": raw["Gmail"],"phone": raw["phone"]})

    mydoc = [i for i in vechileColl.find({"Number": Number})]
    resp = dumps(mydoc)
    a=(raw["Insurance"])
    b=a.split("-")
    x=int(b[0])
    y=int(b[1])
    z=int(b[2])
    res = x+y+z
    print(res)
    return {"success" : True, "Number": Number}



@app.route('/user/vechicleview',methods=['POST'])
def vechicleview():
    data = request.get_json()
   # print(data)
    raw = ast.literal_eval(json.dumps(data))

    Number = raw["Number"]

    #print(Number)

    dataUserID = str(uuid.uuid4())
   # before inserting check user is already registered or not
    #vechileColl.insert_one({"userID": dataUserID,"Number": raw["Number"],"Name": raw["Name"],"Gmail": raw["Gmail"],"Rcnumber": raw["Rcnumber"],"Insurance": raw["Insurance"],"Emession": raw["Emession"],"Gmail": raw["Gmail"] })

    mydoc = [i for i in vechileColl.find({"Number": Number})]
    resp = dumps(mydoc)
    print("********************************************")
  
    return resp

@app.route('/user/checkvalidaty',methods=['POST'])
def checkvalidaty():
    mydoc = vechileColl.find()
    resp = dumps(mydoc)
    res = json.loads(resp)
    print(type(res))
    #print(res[1])
    return resp


    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1111, threaded=True)
