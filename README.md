# "Personal Assistant" application - Python Django project
The "Personal Assistant" application is designed as an everyday helper application for the user with the following features:
- **Address book.** Allows the user to add and edit contacts including phone numbers, addresses and even birthdays;
- **Notebook.** Allows the user to add and edit notes with titles and tags;
- **News.** Contains a summary of popular news: world, sports, finance, entertainment and technology;
- **Weather.** Displays a constant weather forecast at the user's location and also has the ability to display the weather forecast in any city in the world;
- **Currency Converter.** The scrooling line displays the current exchange rates, and the converter allows you to calculate the rates of the current currencies of the world;
- **Upload files.** The user's ability to upload and store files. The application automatically sorts files by type and stores them in separate folders.
## "Personal Assistant" install guide
### Install application "Personal Assistant"
Download ZIP file from repository, unpack it and copy.

### Install Pipenv
Pipenv is a new popular way of automatically creating a 'virtualenv' for the project. It creates Pipfile and Pipfile.lock.\
Install it by using pip:
```
pip install pipenv
```
For the application to work correctly, you need to install the necessary Python libraries. For the installation of the libraries, use the following command:
```
pipenv sync
```

### Database settings
To set up a database connection, enter the necessary settings for connecting to yor database in `settings.py` located in the application folder.

### API key settings
NEWS API key.\
For get NEWS API key go to https://newsapi.org and go through authorization. Then enter yor API key in NEWS_API_KEY in `settings.py` located in the application folder.\
WEATHER API key.\
For get NEWS API key go to https://openweathermap.org and go through authorization. Then enter yor API key in WEATHER_API_KEY in `settings.py` located in the application folder.

### Run the application
If everything has been installed correctly, run the development server.\
Use the following command:
```
python manage.py runserver
```
Open your favorite browser and check at `http://127.0.0.1:8000/`. You should see a login page that tells you the installation was successfull.\
Below an example:
![login_page_example](https://github.com/Ivan-Grigorev/GoIT_Block_2-Project/blob/main/login_page_example.png)

Great! Now to access all the functions of the application you need to go through authorization.
