# Doctor's Appointment booking system

# Project Overview and Features
This project is built with basic python functiona can used by small clinics to manage their appointments or to digitialize their appointment booking system. This also provides the patients to register themseleves on their own and book a doctors appointment according to their will and wish, providing them with the possibility of booking and future appointment or to check their appointment status at ease. Also gives the patient the freedon to book their own doctor according to their issues with available time slots. Clinics can also use this as a way to store a patient's data.


# Features
1. **Book New Appointments**
When someone wants to book an appointment, they enter their name, phone number, and the date they want. The system asks what kind of problem they're dealing with (general health, bone issues, heart problems, etc.) and then shows available doctors and time slots. After they pick a slot, the program gives them a unique appointment number to keep track of their booking.
2.**Schedule Follow-Ups**
Provides already registered patients the option to schedule follow ups just using their previous appointment number, and allows them to enter a new date for the appointment with the choice for selection for doctor and avalaible time slot.
3.**Check Appointment Status**
Patients can quickly check when their appointment is by entering their appointment number. The system tells them the date they're booked for.
4.**Phone Number Validation**
A small but helpful feature, the system makes sure you enter a proper 10-digit phone number. If you type it wrong, it'll ask you to try again instead of accepting bad data.
5.**Appointment Number Generation system**
A appointment number is generated using the random module, this appointment number is 4 digit number(1000-9999) and is useful to store the patients data.

#Technologies Used
This Project is completely built on python with the latest version also known as Python 3.
**Using Modules** - To build the appointment number generation system, *Random* Module has been used to generate a 4 digit appointment number at random(1000-9999).

**OOP** - Defined a "Clinic" class at the start of the program to help store all the provided details regardong the patients, doctors and time and date.

**Dictionaries** - They are used to store the doctors and their available time slots for each speciality.

**Loops** - The entire program is written on a loop and can be run unless the user wishes to exit using the given commands.

**Conditional Statements** - If-elif-else statements are used throughout the function to provide the user with choices and perform different actions for different decision.

**Input and outputs** - Input statements are used to mainly get user's information and their choice and output functions like print are used to provide them with details that either stored or previously defined.


# Installation:
1. Make sure you have python 3 installed.
2. From here you can run the program 2 ways:
  i.  Clone the repository on to your machine and run clinic.py
  ii. You can install or copy clinic.py and save it and then run it on a compiler or an ide.


# Screenshots
**This screenshot shows the use of OOP in python (classes)**

<img width="859" height="351" alt="Screenshot 2025-11-24 091821" src="https://github.com/user-attachments/assets/aa02ac6a-e2fb-4dc3-95d6-6241c842fb9a" />



**Dictionaries used to save doctors and their slots**

<img width="638" height="292" alt="image" src="https://github.com/user-attachments/assets/f8453a56-e82b-4add-b976-87a4c2273a6f" />


**Loops with conditional statements**

<img width="1007" height="484" alt="image" src="https://github.com/user-attachments/assets/7d058694-d1a8-48ab-a506-97a39d334504" />

**Example Output**

<img width="638" height="702" alt="image" src="https://github.com/user-attachments/assets/cac385dc-7ad3-469a-a723-218916769829" />

# Improvements I need to make:
1. Only Remembers one appointment at a time for status check -- Everytime a new appoinment is booked, the previous ones get overwritten on, as everything is saved     on the same variable.
      Possible solution for this can be the use of lists, tuples and dictionaries to help save the data.

2. There is no permanent storage, that is when you exit the program, all saved information is gone as it is all on tmeporary memory.
       Possible Solution can be implementation of a database, which I am very curious to learn about.

3. No way to cancel appointment.

4. Date can range up to 99:99:9999, which is not valid.

5. The "Clinic" class isn't being used to its full potential, and was more so used to learn about classes and they can also be used for future improvements.

6. No way to check all appointments or the patient data at once.

# Personal Note
This was my first Python project and more so created as a test for myself to check upon on the few basics that I have learned in the past few weeks.
It a good learning experience for me and also has motivated me to learn more and build more projects concerning real world issues.
Thank You for going through my program, and if it helps, feel free to modify it and use it.


