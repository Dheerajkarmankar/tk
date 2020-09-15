from tkinter import *
import tkinter.messagebox
import random
import time
from appointment import appo
import numpy as np
import pandas as pd
from gui2 import num

import os

root = Tk()
localtime = time.asctime(time.localtime(time.time()))


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("WELCOME")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        #####################################################################
        self.Username = StringVar()
        self.Password = StringVar()
        ######################################################################

        self.LabelTitle = Label(self.frame, text="Smart Home & Health Care System", fg="Navy Blue",
                                font=('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.LabelTitle = Label(self.frame, text=localtime, fg="Navy Blue", font=('arial', 25, 'bold'), bd=10)
        self.LabelTitle.grid(row=1, column=0, columnspan=2)

        ##########################    frames    #####################################################
        self.Loginframe1 = Frame(self.frame, width=1010, height=300, bd=20, relief='ridge')
        self.Loginframe1.grid(row=2, column=0)

        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=20, relief='ridge')
        self.Loginframe2.grid(row=3, column=0, pady=40)

        self.Loginframe3 = Frame(self.frame, width=1000, height=200, bd=20, relief='ridge')
        self.Loginframe3.grid(row=4, column=0, pady=2)

        ############################# login password  labels  ##########################################

        self.lblUsername = Label(self.Loginframe1, text="Username", font=('arial', 30, 'bold'), bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.Loginframe1, font=('arial', 30, 'bold'), bd=22, textvariable=self.lblUsername)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.Loginframe1, text="Password", font=('arial', 30, 'bold'), bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.Loginframe1, font=('arial', 30, 'bold'), bd=22, textvariable=self.lblPassword)
        self.txtPassword.grid(row=1, column=1)
        ###################################### buttons ########################################################

        self.btnLogin = Button(self.Loginframe2, text="Login", width=20, font=('arial', 20, 'bold'),
                               command=self.Login_Systems)
        self.btnLogin.grid(row=2, column=0)

        self.btnReset = Button(self.Loginframe2, text="Reset", width=20, font=('arial', 20, 'bold'), command=self.Reset)
        self.btnReset.grid(row=2, column=1)

        self.btnForgot = Button(self.Loginframe2, text="Forgot Details", width=20, font=('arial', 20, 'bold'),
                                command=self.Forgot_window)
        self.btnForgot.grid(row=2, column=2)

        self.btnEmergency = Button(self.Loginframe3, text="EMERGENCY(SOS)", width=20, font=('arial', 20, 'bold'),
                                   command=self.Emergency_window)
        self.btnEmergency.grid(row=2, column=1)

        self.btnExit = Button(self.Loginframe3, text="EXIT", width=20, font=('arial', 20, 'bold'), command=self.iExit)
        self.btnExit.grid(row=2, column=2)

    ################################## buttons register ####################################

    # self.btnregistration = Button(self.Loginframe3, text="registration", state = DISABLED, command=self.Registration_window, font=('arial', 20, 'bold'))
    # self.btnregistration.grid(row=0, column=0)
    #
    # self.btnmanagment = Button(self.Loginframe3, text="managment", state = DISABLED,command=self.Hospital_window, font=('arial', 20, 'bold'))
    # self.btnmanagment.grid(row=0, column=1)
    ############################  def login sysytems  ###########################################

    def Login_Systems(self):
        user = (self.Username.get())
        pas = (self.Password.get())

        if self.txtUsername.get() == "q" and self.txtPassword.get() == "q":
            self.Registration_window()
            # self.btnregistration.config(state = NORMAL)
            # self.btnmanagment.config(state = NORMAL)
        else:
            tkinter.messagebox.askokcancel('INCORRECT', 'You may have entered the wrong details')
            # self.btnregistration.config(state=DISABLED)
            # self.btnmanagment.config(state=DISABLED)
            self.txtUsername.delete(0, 'end')
            self.txtPassword.delete(0, 'end')
            self.txtUsername.focus()

    def Reset(self):
        # self.btnregistration.config(state=DISABLED)
        # self.btnmanagment.config(state=DISABLED)
        self.txtUsername.delete(0, 'end')
        self.txtPassword.delete(0, 'end')
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno('Exit', 'Are you sure')
        if self.iExit > 0:
            self.master.destroy()
            return

    ###########################  new windows  ########################################################################################################################################
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)

    def Forgot_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)

    def Emergency_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window5(self.newWindow)


class Window2:
    def __init__(self, master):


        self.master = master
        self.master.title("CATEGORY SELECTION")
        self.master.geometry('1000x600+20+20')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.CategoryTitle = Label(self.frame, text="Select The Category", fg="Navy Blue",
                                   font=('TimesRoman', 30, 'bold'), bd=20)
        self.CategoryTitle.grid(row=0, column=0, columnspan=3, pady=20)

        self.HomeFrame = Frame(self.frame, width=300, height=300, bd=20, relief='ridge')
        self.HomeFrame.grid(row=2, column=0, pady=40)

        self.HealthFrame = Frame(self.frame, width=300, height=300, bd=20, relief='ridge')
        self.HealthFrame.grid(row=2, column=3, pady=40)

        self.Homebtn = Button(self.HomeFrame, text="HOME SYSTEMS", width=15, height=6, fg='black',
                              bg='powder blue', font=('arial', 20, 'bold'),
                              command=num)
        self.Homebtn.grid(row=2, column=0)

        self.Healthbtn = Button(self.HealthFrame, text="HEALTH CARE\n SYSTEM", width=15, height=6, fg='black',
                                bg='powder blue', font=('arial', 20, 'bold'),
                                command=self.Healthcare_window)
        self.Healthbtn.grid(row=2, column=2)

    def Healthcare_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window6(self.newWindow)


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


class Window4:
    def __init__(self, master):
        self.master = master
        self.master.title("FORGOT DETAILS")
        self.master.geometry('600x300+80+80')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Forgetframe1 = Frame(self.frame, width=800, height=100, bd=6, relief=SUNKEN)
        self.Forgetframe1.grid(row=1, column=1, pady=40)

        self.Forgetframe2 = Frame(self.frame, width=200, height=50, bd=6, relief=SUNKEN)
        self.Forgetframe2.grid(row=2, column=1, pady=10)

        self.lblphone = Label(self.Forgetframe1, text=" Phone no", font=('arial', 15, 'bold'), fg='steel blue', bd=20)
        self.lblphone.grid(row=0, column=0)
        self.txtphone = Entry(self.Forgetframe1, font=('arial', 20, 'bold'), bd=10, textvariable=self.lblphone)
        self.txtphone.grid(row=0, column=1)

        self.btnLogin = Button(self.Forgetframe2, text="Enter", width=8, font=('arial', 15, 'bold'),
                               command=self.Forget_system)
        self.btnLogin.grid(row=2, column=0)

    def Forget_system(self):
        if self.txtphone.get() == "12345":
            tkinter.messagebox.askokcancel('Log-in Details', 'Username = q\n password = q')

        else:
            tkinter.messagebox.askokcancel('INCORRECT', 'WRONG PHONE NO')
            self.txtphone.delete(0, 'end')
            self.txtphone.focus()


class Window5:
    def __init__(self, master):
        self.master = master
        self.master.title("EMERGENCY")
        self.master.geometry('700x300+80+80')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Emergencyframe1 = Frame(self.frame, width=100, height=100, bd=10, bg='powder blue', relief='ridge')
        self.Emergencyframe1.grid(row=0, column=0, pady=40, padx=40)

        self.Emergencyframe2 = Frame(self.frame, width=120, height=100, bd=10, bg='powder blue', relief='ridge')
        self.Emergencyframe2.grid(row=0, column=1, pady=40, padx=40)

        self.Emergencyframe3 = Frame(self.frame, width=120, height=100, bd=10, bg='powder blue', relief='ridge')
        self.Emergencyframe3.grid(row=1, column=0, pady=40, padx=40)

        self.Emergencyframe4 = Frame(self.frame, width=120, height=100, bd=10, bg='powder blue', relief='ridge')
        self.Emergencyframe4.grid(row=1, column=1, pady=40, padx=40)

        self.btnEmergency1 = Button(self.Emergencyframe1, text="DOCTOR", width=15, font=('arial', 15, 'bold'),
                                    bg='powder blue', command=self.doctor)
        self.btnEmergency1.grid(row=0, column=0)

        self.btnEmergency2 = Button(self.Emergencyframe2, text="POLICE", width=15, font=('arial', 15, 'bold'),
                                    bg='powder blue', command=self.police)
        self.btnEmergency2.grid(row=0, column=0)

        self.btnEmergency3 = Button(self.Emergencyframe3, text="FIRE STATION", width=15, font=('arial', 15, 'bold'),
                                    bg='powder blue', command=self.station)
        self.btnEmergency3.grid(row=0, column=0)

        self.btnEmergency4 = Button(self.Emergencyframe4, text="NEIGHBOURS", width=15, font=('arial', 15, 'bold'),
                                    bg='powder blue', command=self.neighbours)
        self.btnEmergency4.grid(row=0, column=0)

    def doctor(self):
        tkinter.messagebox.showwarning('SOS', 'CALL DOCTOR')
        self.btnEmergency1.focus()

    def police(self):
        tkinter.messagebox.showwarning('SOS', 'CALL POLICE')
        self.btnEmergency2.focus()

    def station(self):
        tkinter.messagebox.showwarning('SOS', 'CALL FIRE STATION')
        self.btnEmergency3.focus()

    def neighbours(self):
        tkinter.messagebox.showwarning('SOS', 'CALL NEIGHBOURS')
        self.btnEmergency4.focus()


class Window6:
    def __init__(self, master):
        self.master = master
        self.master.title("HEALTH CARE SYSTEM")
        self.master.geometry('1200x600+50+50')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Prescribframe = Frame(self.frame, width=300, height=200, bd=10, bg='powder blue', relief='ridge')
        self.Prescribframe.grid(row=0, column=0, pady=40, padx=40)

        self.Appointframe = Frame(self.frame, width=300, height=200, bd=10, bg='powder blue', relief='ridge')
        self.Appointframe.grid(row=0, column=1, pady=40, padx=40)

        self.Hrecordframe = Frame(self.frame, width=300, height=200, bd=10, bg='powder blue', relief='ridge')
        self.Hrecordframe.grid(row=1, column=0, pady=40, padx=40)

        self.Billframe = Frame(self.frame, width=300, height=200, bd=10, bg='powder blue', relief='ridge')
        self.Billframe.grid(row=1, column=1, pady=40, padx=40)

        self.btnHealth1 = Button(self.Prescribframe, text="PRESCRIPTION", width=25, height=8,
                                 font=('arial', 15, 'bold'), bg='powder blue', command=self.Prescribe_window)
        self.btnHealth1.grid(row=0, column=0)

        self.btnHealth2 = Button(self.Appointframe, text="BOOK APPOINTMENT", width=25, height=8,
                                 font=('arial', 15, 'bold'), bg='powder blue', command=appo)
        self.btnHealth2.grid(row=0, column=0)

        self.btnHealth3 = Button(self.Hrecordframe, text="PREDICT HEALTH", width=25, height=8,
                                 font=('arial', 15, 'bold'), bg='powder blue', command=self.Health_window)
        self.btnHealth3.grid(row=0, column=0)

        self.btnHealth4 = Button(self.Billframe, text="BILL", width=25, height=8, font=('arial', 15, 'bold'),
                                 bg='powder blue', command=self.Bill_window)
        self.btnHealth4.grid(row=0, column=0)

    def Prescribe_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window7(self.newWindow)

    def Appointment_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window8(self.newWindow)

    def Health_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window9(self.newWindow)

    def Bill_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window8(self.newWindow)


class Window7:
    def __init__(self, master):
        self.master = master
        self.master.title("PRESCRIPTION")
        self.master.geometry('1000x500+50+50')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Itemframe1 = Frame(self.frame, width=100, height=100, bd=10, relief='ridge')
        self.Itemframe1.grid(row=0, column=0, padx=100, pady=50)

        self.lblinfo = Label(self.Itemframe1, font=('aria', 15, 'bold'), text="MORNING", fg="black", bg='sky blue',
                             bd=5)
        self.lblinfo.grid(row=0, column=0)

        self.Itemframe2 = Frame(self.frame, width=100, height=100, bd=10, relief='ridge')
        self.Itemframe2.grid(row=0, column=1, padx=100, pady=50)

        self.lblinfo = Label(self.Itemframe2, font=('aria', 15, 'bold'), text="AFTERNOON", fg="black", bg='sky blue',
                             bd=5)
        self.lblinfo.grid(row=0, column=0)

        self.Itemframe3 = Frame(self.frame, width=100, height=100, bd=10, relief='ridge')
        self.Itemframe3.grid(row=0, column=2, padx=100, pady=50)

        self.lblinfo = Label(self.Itemframe3, font=('aria', 15, 'bold'), text="EVENING", fg="black", bg='sky blue',
                             bd=5)
        self.lblinfo.grid(row=0, column=0)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" Vicodin", fg="Navy blue", anchor=W)
        self.item.grid(row=1, column=0)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" levothyroxine", fg="Navy blue", anchor=W)
        self.item.grid(row=2, column=0)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" prednisone", fg="Navy blue", anchor=W)
        self.item.grid(row=3, column=0)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" Amoxil ", fg="Navy blue", anchor=W)
        self.item.grid(row=4, column=0)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" Neurontin ", fg="Navy blue", anchor=W)
        self.item.grid(row=5, column=0)
        #####################################################################################
        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" Prinivil", fg="Navy blue", anchor=W)
        self.item.grid(row=1, column=1)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" Lipitor", fg="Navy blue", anchor=W)
        self.item.grid(row=2, column=1)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" levothyroxine", fg="Navy blue", anchor=W)
        self.item.grid(row=3, column=1)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" Amoxil ", fg="Navy blue", anchor=W)
        self.item.grid(row=4, column=1)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" Neurontin ", fg="Navy blue", anchor=W)
        self.item.grid(row=5, column=1)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" Zofran", fg="Navy blue", anchor=W)
        self.item.grid(row=6, column=1)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" Glucophage", fg="Navy blue", anchor=W)
        self.item.grid(row=7, column=1)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" prednisone", fg="Navy blue", anchor=W)
        self.item.grid(row=8, column=1)
        #########################################################################
        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" amoxicillin", fg="Navy blue", anchor=W)
        self.item.grid(row=1, column=2)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" gabapentin", fg="Navy blue", anchor=W)
        self.item.grid(row=2, column=2)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" Vicodin", fg="Navy blue", anchor=W)
        self.item.grid(row=3, column=2)

        self.item = Label(self.frame, font=('aria', 15, 'bold'), text=" isinopril", fg="Navy blue", anchor=W)
        self.item.grid(row=4, column=2)


class Window8:
    def __init__(self, master):

        self.master = master
        self.master.title("BILL PAYMENT")
        self.master.geometry('600x300+50+50')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Forgetframe1 = Frame(self.frame, width=800, height=100, bd=6, relief=SUNKEN)
        self.Forgetframe1.grid(row=1, column=1, pady=40)

        self.Forgetframe2 = Frame(self.frame, width=200, height=50, bd=6, relief=SUNKEN)
        self.Forgetframe2.grid(row=2, column=1, pady=10)

        self.lblphone = Label(self.Forgetframe1, text=" ENTER \nAMOUNT", font=('arial', 15, 'bold'), fg='steel blue',
                              bd=20)
        self.lblphone.grid(row=0, column=0)
        self.txtphone = Entry(self.Forgetframe1, font=('arial', 20, 'bold'), bd=10, textvariable=self.lblphone)
        self.txtphone.grid(row=0, column=1)

        self.btnLogin = Button(self.Forgetframe2, text="PAY", width=8, font=('arial', 15, 'bold'),
                               command=self.Forget_system)
        self.btnLogin.grid(row=2, column=0)

    def Forget_system(self):
        if self.txtphone.get() == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0:
            tkinter.messagebox.askokcancel('BILL PAYMENT', 'AMOUNT PAYED')

        else:
            tkinter.messagebox.askokcancel('INCORRECT', 'ENTER NUMERIC VALUES ONLY')
            self.txtphone.delete(0, 'end')
            self.txtphone.focus()


class Window9:
    def __init__(self, master):
        self.master = master
        self.master.title("HEALTH PREDICTION SYSTEM")
        self.master.geometry('800x300+50+50')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
                   'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
                   'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
                   'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
                   'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
                   'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
                   'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
                   'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
                   'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
                   'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
                   'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
                   'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
                   'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body',
                   'belly_pain',
                   'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite',
                   'polyuria', 'family_history', 'mucoid_sputum',
                   'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
                   'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
                   'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
                   'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
                   'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
                   'red_sore_around_nose',
                   'yellow_crust_ooze']

        self.disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
                        'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma',
                        'Hypertension',
                        ' Migraine', 'Cervical spondylosis',
                        'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid',
                        'hepatitis A',
                        'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis',
                        'Tuberculosis',
                        'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
                        'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
                        'Osteoarthristis',
                        'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection',
                        'Psoriasis',
                        'Impetigo']



        self.l2=[]
        for x in range(0,len(self.l1)):
            self.l2.append(0)

        #     # TESTING DATA df -------------------------------------------------------------------------------------
        self.df=pd.read_csv("Training.csv")

        self.df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
                                      'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
                                      'Migraine':11,'Cervical spondylosis':12,
                                      'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
                                      'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
                                      'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
                                      'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
                                      '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
                                      'Impetigo':40}},inplace=True)
        #


        self.X= self.df[self.l1]

        self.y = self.df[["prognosis"]]
        np.ravel(self.y)


        # TRAINING DATA tr --------------------------------------------------------------------------------
        self.tr=pd.read_csv("Testing.csv")
        self.tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
                                      'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
                                      'Migraine':11,'Cervical spondylosis':12,
                                      'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
                                      'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
                                      'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
                                      'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
                                      '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
                                      'Impetigo':40}},inplace=True)

        self.X_test= self.tr[self.l1]
        self.y_test = self.tr[["prognosis"]]
        np.ravel(self.y_test)

        self.Name = StringVar()
        self.Symptom1 = StringVar()
        self.Symptom1.set(None)
        self.Symptom2 = StringVar()
        self.Symptom2.set(None)
        self.Symptom3 = StringVar()
        self.Symptom3.set(None)



        # Heading
        self.w2 = Label(self.frame, justify=LEFT, text="Disease Predictor", fg="black")
        self.w2.config(font=("Times Roman", 30))
        self.w2.grid(row=1, column=1, columnspan=2, padx = 100, pady = 15)


        # labels



        self.S1Lb = Label(self.frame, text="Symptom 1", fg="yellow", bg="black")
        self.S1Lb.grid(row=7, column=0, pady=10, sticky=W)

        self.S2Lb = Label(self.frame, text="Symptom 2", fg="yellow", bg="black")
        self.S2Lb.grid(row=8, column=0, pady=10, sticky=W)

        self.S3Lb = Label(self.frame, text="Symptom 3", fg="yellow", bg="black")
        self.S3Lb.grid(row=9, column=0, pady=10, sticky=W)



        # entries
        self.OPTIONS = sorted(self.l1)


        self.S1En = OptionMenu(self.frame,self.Symptom1,*self.OPTIONS)
        self.S1En.grid(row=7, column=1)

        self.S2En = OptionMenu(self.frame, self.Symptom2,*self.OPTIONS)
        self.S2En.grid(row=8, column=1)

        self.S3En = OptionMenu(self.frame, self.Symptom3,*self.OPTIONS)
        self.S3En.grid(row=9, column=1)



        self.dst = Button(self.frame, text="PREDICT", command=self.DecisionTree,bg="green",fg="yellow")
        self.dst.grid(row=8, column=3,padx=10)

        self.t1 = Text(self.frame, height=1, width=40,bg="orange",fg="black")
        self.t1.grid(row=15, column=1, padx=10)







    #     # ------------------------------------------------------------------------------------------------------

    def DecisionTree(self):

        from sklearn import tree

        self.clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
        self.clf3 = self.clf3.fit(self.X,self.y)

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        self.y_pred=self.clf3.predict(self.X_test)
        print(accuracy_score(self.y_test, self.y_pred))
        print(accuracy_score(self.y_test, self.y_pred,normalize=False))
        # -----------------------------------------------------

        self.psymptoms = [self.Symptom1.get(),self.Symptom2.get(),self.Symptom3.get()]#,Symptom4.get(),Symptom5.get()]

        for k in range(0,len(self.l1)):
            # print (k,)
            for z in self.psymptoms:
                if(z==self.l1[k]):
                    self.l2[k]=1

        self.inputtest = [self.l2]
        self.predict = self.clf3.predict(self.inputtest)
        self.predicted=self.predict[0]

        h='no'
        for a in range(0,len(self.disease)):
            if(self.predicted == a):
                h='yes'
                break


        if (h=='yes'):
            self.t1.delete("1.0", END)
            self.t1.insert(END, self.disease[a])
        else:
            self.t1.delete("1.0", END)
            self.t1.insert(END, "Not Found")


app = Window1(root)
root.mainloop()
