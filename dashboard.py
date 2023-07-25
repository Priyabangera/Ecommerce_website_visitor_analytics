from flask import Blueprint,jsonify,request
from  sqlalchemy.sql import text
from db import db
import datetime

dashboard_blueprint = Blueprint('dashboard_blueprint',__name__)


@dashboard_blueprint.route('/today-visitors')
def todayVisitors():

    tdate=datetime.datetime.today().strftime('%Y-%m-%d')

    sqlTVisitors  = text('SELECT count FROM visitors_log WHERE date = :tdate')
    resultDataVisitors=db.engine.execute(sqlTVisitors,tdate = tdate)
    todayVisitorsData=resultDataVisitors.fetchall()

    jsonData = jsonify([dict(row) for row in todayVisitorsData])
    return jsonData

@dashboard_blueprint.route('/ad-click-data')
def adClickData():

    tdate = datetime.datetime.today().strftime('%Y-%m-%d')

    sqlAdisitors = text('SELECT total_clicks FROM ad_clicks WHERE date = :tdate')
    resultDataAds = db.engine.execute(sqlAdisitors,tdate = tdate)
    todayAdsData = resultDataAds.fetchall()

    jsondata = jsonify([dict(row) for row in todayAdsData])
    return jsondata

@dashboard_blueprint.route('/contacts-count')
def contactCount():

    tdate = datetime.datetime.today().strftime('%Y-%m-%d')

    sqlContactSql = text('SELECT COUNT(id) AS contact_count_today FROM contacts WHERE date = :tdate')
    contactData = db.engine.execute(sqlContactSql,tdate = tdate)
    conatactResData = contactData.fetchall()

    jsondata = jsonify([dict(row) for row in conatactResData])
    return jsondata

@dashboard_blueprint.route('/contact-list-table')
def contactListTable():

    tdate = datetime.datetime.today().strftime('%Y-%m-%d')    

    sqlContactListSql = text('SELECT * FROM contacts WHERE date = :tdate')
    contactList = db.engine.execute(sqlContactListSql,tdate = tdate)  
    contactResListData = contactList.fetchall()

    jsondata = jsonify([dict(row) for row in contactResListData])
    return jsondata

@dashboard_blueprint.route('/bar-graph-data')
def dashboardData():

    x = ''
    for m in range(1,13):

        sqlMonthGraph = text('SELECT SUM(count) AS month_visitor_count FROM visitors_log WHERE MONTH(date) = :month')
        monthVisitor = db.engine.execute(sqlMonthGraph,month = m)
        monthVisitorData = monthVisitor.fetchall()
        monthVisitorCount = monthVisitorData[0].month_visitor_count

        x+= '{"month":"'+str(monthVisitorCount)+'"},'

    x = x[:-1]
    jsondata = '['+x+']'
    return jsondata





