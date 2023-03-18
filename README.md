# BLOB in python+postgreSQL

This repo reproduces the code of [this tutorial](https://www.geeksforgeeks.org/handling-postgresql-blob-data-in-python/) to show how to insert and retrieve a BLOB in postgreSQL using python.

We use the following table

```
CREATE TABLE blob_datastore
(
    s_no integer,
    file_name character varying,
    blob_data bytea
)
```

I had to 
```
 pip install psycopg2 
```

And, to do that, first I had to 
```
sudo apt install postgresql-common
sudo apt install libpq-dev
```
