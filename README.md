# VideoTrim
Simple web application that trims and cuts video based off of user inputted trim points. The final edited video has optimal settings (container, encoding, bit rate, etc.) for youtube upload. Useful for quickly generating game film and highlights.

**Once you have cloned the directory to your local machine, follow the directions below:**
1. cd into VideoTrim directory
2. $pipenv install
3. $cd videotrim 
4. $pipenv run python manage.py runserver
5. Access application UI at http://127.0.0.1:8000/

**Running Application:**
1. Enter global path to video file
2. Add trim time. Add least 2 trim times are necessary. Therefore, if you want to trim and save the first 5 seconds of your video, add 0 and 5 as trim times. 
3. Click Trim button.
4. Edited video can be found in videotrim folder
