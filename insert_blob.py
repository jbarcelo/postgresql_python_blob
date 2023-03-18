import psycopg2

# This Function will open & convert the image or file data to binary data.


def convert_To_Binary(filename):
	with open(filename, 'rb') as file:
		data = file.read()
	return data


def insert_BLOB(S_No, FileName):
	""" insert a BLOB into a table """
	conn = None
	try:

		# connect to the PostgreSQL server & creating a cursor object
		conn = psycopg2.connect(database ="For_Practice", user = "postgres",
                        password = "postgres", host = "localhost",
                        port = "5432")

		# Creating a cursor with name cur.
		cur = conn.cursor()

		# Binary Data
		file_data = convert_To_Binary(FileName)

		# BLOB DataType
		BLOB = psycopg2.Binary(file_data)

		# SQL query to insert data into the database.
		cur.execute(
			"INSERT INTO blob_datastore(s_no,file_name,blob_data) VALUES(%s,%s,%s)", (S_No, FileName, BLOB))

		# Close the connection
		cur.close()

	except(Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			# Commit the changes to the database
			conn.commit()


insert_BLOB(1, 'Postgresql.png')

