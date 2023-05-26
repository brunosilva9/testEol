## Test Eol
App for Event visualization from the Eol platform.
BackEnd with Django api Framework and Frontend with ReactJs.
git clone https://github.com/brunosilva9/testEol.git
# Install the node package and make the static files 
npm i 

npm run build

----------------------------------------------------
# Data settings
In the folder ApiEol/data/
    you gonna find the file data_example, you need to delete that file and put the data from Eol(compressed.tar.gz).
    extract it with the name data.json
----------------------------------------------------
* If you need it you can start the virtual environment venv.

You need get python 3.X
And django for run the server

pip install django

pip install django-cors-headers


--------------------------------------------------

# Make migrations

python manage.py migrate

Wait until the script is finished, take near 4 minutes to complete 

--------------------
# Start the server

python manage.py runserver

