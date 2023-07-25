from flask import Blueprint,jsonify,request
from  sqlalchemy.sql import text
from db import db
import datetime

landing_blueprint = Blueprint('landing_blueprint',__name__)

@landing_blueprint.route('/products')
def products():

     tdate=datetime.datetime.today().strftime('%Y-%m-%d')

     # Log number of visitors for date
     sqlChkVisitors=text('SELECT COUNT(id) AS today_count,count FROM visitors_log WHERE date= :tdate')
     todayData=db.engine.execute(sqlChkVisitors,tdate=tdate)
     resultTodayData=todayData.fetchall()
     todayVisitorsCount=resultTodayData[0].today_count
     numberOfVisitors=resultTodayData[0].count
    
     if todayVisitorsCount == 0:
 
        sqlInsVisitors=text('INSERT INTO visitors_Log(date,count)VALUES(:tdate,1)')
        db.engine.execute(sqlInsVisitors,tdate=tdate)
     
     else:
        newVisitorCount=numberOfVisitors + 1
        sqlUpdVisitors=text('UPDATE visitors_log SET count=:newVisitorCount WHERE date=:tdate')
        db.engine.execute(sqlUpdVisitors,newVisitorCount=newVisitorCount,tdate=tdate)

     sqlProducts = text('SELECT * FROM product')
     resultSet = db.engine.execute(sqlProducts)
     resultData = resultSet.fetchall()

     jsondata = jsonify([dict(row) for row in resultData])
     return jsondata



@landing_blueprint.route('/save-contact-data',methods=['POST'])
def saveContactData():

    f_name = request.form['name']
    f_email = request.form['email']
    f_mobile = request.form['mobile']
    f_comment = request.form['comments']
     
    tdate=datetime.datetime.today().strftime('%Y-%m-%d')

    sqlSave=text('INSERT INTO contacts(name,email,mobile,comments,date)vALUES(:name,:email,:mobile,:comments,:todaydate)')
    db.engine.execute(sqlSave,name=f_name,email=f_email,mobile=f_mobile,comments=f_comment,todaydate=tdate)
  
    return 'data save succesfully'

@landing_blueprint.route('/ad-click')
def adClick():

    tdate = datetime.datetime.today().strftime('%Y-%m-%d')

    # Log ad click 
    sqlAdClick = text('SELECT COUNT(id) AS adrow_count,total_clicks FROM ad_clicks WHERE date = :tdate')
    adClickData = db.engine.execute(sqlAdClick,tdate = tdate)
    resAdclickData = adClickData.fetchall()
    adClickRowCount = resAdclickData[0].adrow_count
    totalAdClickForDay = resAdclickData[0].total_clicks

    if adClickRowCount == 0:

        sqlInsAd = text('INSERT INTO ad_clicks (date,total_clicks) VALUES (:tdate,1)')
        db.engine.execute(sqlInsAd,tdate = tdate)

    else:

        newAdCount = totalAdClickForDay + 1
        sqlUpdVisitors = text('UPDATE ad_clicks SET total_clicks = :newAdCount WHERE date = :tdate')
        db.engine.execute(sqlUpdVisitors,newAdCount = newAdCount,tdate = tdate)
        return "add click logged succesfully"