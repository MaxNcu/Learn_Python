from flaskext.mysql import MySQL
mysql = MySQL()

def db(sql):
    cursor = mysql.get_db().cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for d in data:
        print(d[3], SEX[d[4]])
    return jsonify({'code': 200})