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
* Perform database migration; 'python manage.py makemigrations add' (add is the app name)
* Finally execute 'python manage.py migrate'

 As I mentioned in my initial phone interview, I would like to explore new technologies and happy to learn so as a self learner. At first I thought to work on Java supported Play framework as my recent work/ experiences is on Java. But I considered this is an opportunity to explore Djano and have some idea on it. I feel very much happy and proud that the project (basic functionalities) has completed in a day, where I have to also read Django documentation and review Python. The project may be extended to have error checking, tabular display of result etc. But here I foucs on basic functionality and try to finish it by a day.mainly m

