# Birthday-Wisher
It automatically wishes Birthday or send messages on the scheduled time
# I Created an Automatic Birthday Wisher To Auto-Wish Friends In Python
In this tutorial we are going to create a Python application which will automatically wish someone on their birthday. This application will wish someone automatically on schedule. So let us see how to make it.

Let’s open our favourite IDE and create a file named main.py. Now we need to install a few models which will help this program to run, such as pandas, openpyxl etc. We will type the following in terminal/CMD to install the modules :

“pip install pandas”.
“pip install openpyxl”

Now we will create an excel sheet on that folder and open it. We will add the following rows, such as Sno, Name, Birthday, Dialogue, Year, Email. Now for testing purposes we will add a few entries to it. Now let's get back to the main.py file. Now we need to create a function which will read the excel file and extract data from it. We will use the pandas library for it. Now to send email we will use the smtplib library. We will be using Gmail for this application. Now we need to create a function which will send email using a gmail id. Now to use this service you need to enable less secure apps on the gmail account which you are going to use for sending the messages. Now our program is ready. Now to schedule the program you need to do the following:

* We need to create a task scheduler task which will run our main.py file on 12:00 am everyday so that it can check and wish that person on their respective birthday.
* To do that, you need to copy the path of the file.
* Now open the task scheduler.
* Now you need to click on  create a task and then triggers.
* Now click on new and set that as daily and time as 00:00:00 (for 12 am).
* Now get back to the general tab and add name and description.
* Now go to action then new and then click on browse.
* Now on program/script click browse and then choose python.exe by browsing and for arguments just paste the path of the file within the double quote.
* Now press ok and exit it.

Now our program is ready to run.
