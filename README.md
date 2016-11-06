# Import CSV file to DB
## How to run the application
* from the <FileUpload> app directory execute 'pyhton3 manage.py runserver' 
* Browse the url 'http://localhost:8000/add'
* By using 'Choose File' button choose an CSV file
* Upload the file using "Upload file" button

## Outcome

After uploading the CSV file, it will redirect to the result page where it shows total expenses  per
month (month appears as number format). This is to note that DB is not empty.

## Delete stored data
App's DB contents some pre stored data and to delete existing data follow the steps
* By using 'sqlite3' connect to DB using '.open db.sqlite3' (db.sqlite3 is the DB name)
* 'drop table add_employee'
* 'drop table add_taxinfo;
* 'drop table add_expenses'
* Perform database migration; 'python3 manage.py makemigrations add' (add is the app name)
* Finally execute 'python3 manage.py migrate'

 For the last 3-4 years, I am mostly working on Java or related technlogies. Reading the position details, I found my self excited to explore new technologies, if there is an opportunity. Instead of choosing jave based web framework, I have choosen Django/Python to explore new era and make a firm deadline of day 1/2 as not to make problem to my other daily activities.
  I feel very much happy and proud duw to complete he project with very basic requirements within a day. There are more we can add(exception, error handling, more user friendly display or interaaction) but my goal was on very basic and must needed features. Reading Django documentation and reviewing Python with implementation make me more self confident about my quick learning attitude. Having an opportunity, I strongly believe that I will be a quick contributor as well as exploring new technologies.

