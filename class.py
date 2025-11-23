from datetime import datetime as dt


class clinic():
    def __init__(self, date, time_start, time_end, doctor, room_no, cost, name, ph_no):
        self.date = date
        self.time_start = time_start
        self.time_end = time_end
        self.doctor = doctor
        self.room_no = room_no
        self.cost = cost
        self.name = name
        self.ph_no = ph_no


reason = int(
    input("Reason for Consultation: \n1.New Appointment \n2.Followup \n(1 or 2):"))
if reason == 1:
    print("--New Appointment--")
    date = input("Enter the date for appointment(dd:mm:yyyy):")
    diagnosis = input("Kindly describe the problem you are facing: \n"
                      "1.General\n"
                      "2.Orthopedic(Bone-related)\n"
                      "3.Heart-related\n"
                      "4.\n")


elif reason == 2:
    print("--Followup--")


else:
    print("Invalid Choice")
