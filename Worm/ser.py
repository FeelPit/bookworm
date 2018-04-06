from __future__ import print_function
import mysql.connector


def sql(name):
	cnx = mysql.connector.connect(user='root', password='root',
	                              host='127.0.0.1',
	                              database='testik')
	cursor = cnx.cursor()
	sept = ("""SELECT 
					id 
				FROM 
					testik.book 
				WHERE 
					name={};""".format(name))
	cursor.execute(sept)	
	results = cursor.fetchall()
	if results:
		cursor.execute("""SELECT 
								price 
						  FROM 
						  		testik.book 
						  WHERE 
						  		name = {};""".format(name))
		res = cursor.fetchall()
		cnx.commit()
		cnx.close()
		fin = res[0][0]
		return(fin)
	else:
		cnx.commit()
		cnx.close()
		fin = None
		return(fin)


