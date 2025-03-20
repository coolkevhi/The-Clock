import datetime
import os
import pytz

tz2 = ""
tz = ""
dd = ""
tz3 = ""
ts = ""
tm = ""
th = ""
ts2 = True
tm2 = True
th2 = True
tms = False
wd = ""
wd2 = 0
mm = ""
mm2 = 0
yy = ""
yy2 = True
amp = ""
wn = ""
wn2 = 0
dn = ""
dn2 = False
msg= ""
p = ""
tz2 = pytz.timezone("US/Eastern")

def decider():
   global th
   global th2
   global ts
   global ts2
   global tm
   global tm2
   global amp
   global tms
   global mm
   global mm2
   global yy
   global yy2
   global wd
   global wd2
   global wn2
   global wn
   global dn
   global dn2
   global msg
   global tz2
   global tz
   global dd
   global tz3
   global tz2

   tz = datetime.datetime.now(tz2)
   dd = tz.strftime("%d")
   tz3 = tz.strftime("%Z")

   if th2 == True:
       th = f"{tz.strftime("%I")}"
       amp = tz.strftime("%p")
   else:
       th = tz.strftime("%H")
       amp = ""
   if tm2 == True:
       tm = f":{tz.strftime("%M")}"
   else:
       tm = ""
   if ts2 == True and tm2 == True:
       if tms == True:
           ts = f":{tz.strftime("%S")}:{tz.strftime("%f")}"
       else:
           ts = f":{tz.strftime("%S")}"
   else:
       ts = ""
   if mm2 == 0:
       mm = tz.strftime("%B")
   elif mm2 == 1:
       mm = tz.strftime("%b")
   elif mm2 == 2:
       mm = tz.strftime("%m")
   if yy2 == True:
       yy = tz.strftime("%Y")
   else:
       yy = tz.strftime("%y")
   if wd2 == 0:
       wd = tz.strftime("%A")
   elif wd2 == 1:
       wd = tz.strftime("%a")
   elif wd2 == 2:
        wd = f"/WeekDay Number: {tz.strftime("%w")}/ "
   if wn2 == 0:
       wn = ""
   elif wn2 == 1:
       wn = f"\nWeek Number: {tz.strftime("%U")} "
   elif wn2 == 2:
       wn = f"\nWeek Number: {tz.strftime("%W")} "
   if dn2 == True and wn2 != 0:
       dn = f"Day Number: {tz.strftime("%j")}"
   elif dn2 == True and wn2 == 0:
       dn = f"\nDay Number: {tz.strftime("%j")}"
   else:
       dn = ""
   msg = ""

def main():
   print()
   print("Welcome to THE CLOCK")
   print()
   print("--------------------------------------------------")
   print()
   print(f"{th}{tm}{ts} {amp} {tz3}")
   print(f"{wd} {dd} {mm} {yy}{wn}{dn}")
   print()
   print("--------------------------------------------------")
   print()


def opt():
   global msg
   global p
   p = 0
   print("[T] Current Date and Time \n[S] Settings \n[X] Exit")
   decision = input(msg)
   if decision.lower() == "x":
       os.system("cls")
       print("Thanks for using The Clock (:")
       quit()
       msg = ""
   elif decision.lower() == "t":
       msg = ""
       refresh()
   elif decision.lower() == "s":
       set()
   else:
       msg = "Please put an available option: "
       redo()


def set():
    global p
    global msg
    global th
    global th2
    global ts
    global ts2
    global tm
    global tm2
    global amp
    global tms
    global mm
    global mm2
    global yy
    global yy2
    global wd
    global wd2
    global wn2
    global wn
    global dn
    global dn2
    global msg
    global tz2
    global tz
    global dd
    global tz3

    p = 1
    os.system("cls")
    main()
    print("[P] Preview Changes \n[W] WeekDay Settings \n[M] Month Settings \n[Y] Toggle Full/Short Year \n[H] Toggle Military/AM-PM \n[I] Toggle Minutes \n[S] Toggle Seconds(AUTO TOGGLES OFF IF MINUTES ARE TOGGLED OFF) \n[F] Toggle Microseconds(AUTO TOGGLES OFF IF MINUTES OR SECONDS ARE TOGGLED OFF) \n[T] Timezone Settings \n[D] Toggle Day Number \n[N] Week Number Settings \n[B] Back")
    decision = input(msg)
    if decision.lower() == "b":
        p = 0
        redo()
        msg = ""
    elif decision.lower() == "p":
        msg = ""
        refresh()
    elif decision.lower() == "w":
        wdset()
    elif decision.lower() == "m":
        mset()
    elif decision.lower() == "y":
        if yy2 == True:
            yy2 = False
        elif yy2 == False:
            yy2 = True
        redo()
    elif decision.lower() == "h":
        if th2 == True:
            th2 = False
        elif th2 == False:
            th2 = True
        redo()
    elif decision.lower() == "i":
        if tm2 == True:
            tm2 = False
        elif tm2 == False:
            tm2 = True
        redo()
    elif decision.lower() == "s":
        if ts2 == True:
            ts2 = False
        elif ts2 == False:
            ts2 = True
        redo()
    elif decision.lower() == "f":
        if tms == True:
            tms = False
        elif tms == False:
            tms = True
        redo()
    elif decision.lower() == "t":
        tzset()
    elif decision.lower() == "d":
        if dn2 == True:
            dn2 = False
        elif dn2 == False:
            dn2 = True
        redo()
    elif decision.lower() == "n":
        wnset()
    else:
        msg = "Please put an available option: "
        redo()

def redo():
    global p
    os.system("cls")
    main()
    if p == 0:
        opt()
    elif p == 1:
        set()
    elif p == 2:
        wdset()
    elif p == 3:
        mset()
    elif p == 4:
        wnset()
    elif p == 5:
        tzset()
def refresh():
    global p
    os.system("cls")
    decider()
    main()
    if p == 0:
        opt()
    elif p == 1:
        set()
    elif p == 2:
        wdset()
    elif p == 3:
        mset()
    elif p == 4:
        wnset()
    elif p == 5:
        tzset()

def wdset():
    global p
    global msg
    global wd2
    p = 2
    os.system("cls")
    main()
    print("WeekDay Settings")
    print("[S] Short \n[F] Full \n[N] Number \n[B] Back")
    decision = input(msg)
    if decision.lower() == "b":
        p = 1
        redo()
        msg = ""
    elif decision.lower() == "s":
        wd2 = 1
        redo()
    elif decision.lower() == "f":
        wd2 = 0
        redo()
    elif decision.lower() == "n":
        wd2 = 2
        redo()
    else:
        msg = "Please put an available option: "
        redo()
def mset():
    global p
    global msg
    global mm2
    p = 3
    os.system("cls")
    main()
    print("Month Settings")
    print("[S] Short \n[F] Full \n[N] Number \n[B] Back")
    decision = input(msg)
    if decision.lower() == "b":
        p = 1
        redo()
        msg = ""
    elif decision.lower() == "s":
        mm2 = 1
        redo()
    elif decision.lower() == "f":
        mm2 = 0
        redo()
    elif decision.lower() == "n":
        mm2 = 2
        redo()
    else:
        msg = "Please put an available option: "
        redo()
def wnset():
    global p
    global msg
    global wn2
    p = 4
    os.system("cls")
    main()
    print("Week Number Settings")
    print("[O] Off \n[S] By Sundays \n[M] By Mondays \n[B] Back")
    decision = input(msg)
    if decision.lower() == "b":
        p = 1
        redo()
        msg = ""
    elif decision.lower() == "o":
        wn2 = 0
        redo()
    elif decision.lower() == "s":
        wn2 = 1
        redo()
    elif decision.lower() == "m":
        wn2 = 2
        redo()
    else:
        msg = "Please put an available option: "
        redo()

def tzset():
    global p
    global msg
    global tz2
    p = 5
    os.system("cls")
    main()
    print("Set Timezone")
    print("[A] Alaska \n[L] Aleutian \n[R] Arizona \n[C] Central \n[I] East-Indiana \n[E] Eastern \n[H] Hawaii \n[R] Indiana-Starke \n[M] Michigan \n[O] Mountain \n[P] Pacific \n[N] Pacific-New \n[S] Samoa \n[B] Back")
    decision = input(msg)
    if decision.lower() == "b":
        p = 1
        redo()
        msg = ""
    elif decision.lower() == "a":
        tz2 = pytz.timezone("US/Alaska")
        redo()
    elif decision.lower() == "l":
        tz2 = pytz.timezone("US/Aleutian")
        redo()
    elif decision.lower() == "r":
        tz2 = pytz.timezone("US/Arizona")
        redo()
    elif decision.lower() == "c":
        tz2 = pytz.timezone("US/Central")
        redo()
    elif decision.lower() == "i":
        tz2 = pytz.timezone("US/East-Indiana")
        redo()
    elif decision.lower() == "e":
        tz2 = pytz.timezone("US/Eastern")
        redo()
    elif decision.lower() == "h":
        tz2 = pytz.timezone("US/Hawaii")
        redo()
    elif decision.lower() == "r":
        tz2 = pytz.timezone("US/Indiana-Starke")
        redo()
    elif decision.lower() == "m":
        tz2 = pytz.timezone("US/Michigan")
        redo()
    elif decision.lower() == "o":
        tz2 = pytz.timezone("US/Mountain")
        redo()
    elif decision.lower() == "p":
        tz2 = pytz.timezone("US/Pacific")
        redo()
    elif decision.lower() == "n":
        tz2 = pytz.timezone("US/Pacific-New")
        redo()
    elif decision.lower() == "s":
        tz2 = pytz.timezone("US/Samoa")
        redo()
    else:
        msg = "Please put an available option: "
        redo()

decider()
main()
opt()

