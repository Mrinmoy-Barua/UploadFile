# Import CSV file to DB
## How to run the application
* from the <FileUpload> app directory execute 'pyhton manage.py runserver' 
* Browse the url 'http://localhost:8000/add'
* By using 'Choose File' button choose an CSV file
* Upload the file using "Upload file" button

## Outcome

After uploading the CSV file, it will redirect to the result page where it shows total expenses  per
month (month appears as number format)

## Delete stored data
App's DB contents some pre stored data and to delete existing data follow the steps
* By using 'sqlite3' connect to DB using '.open db.sqlite3' (db.sqlite3 is the DB name)
* 'drop table add_employee'
* 'drop table add_taxinfo;
* 'drop table add_expenses'
*
