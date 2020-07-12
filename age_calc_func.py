###################### My own program to calculate age #####################
print('################################################')
print('############### Age Calculator #################')
print('############### Belaid Abdelhadi ###############')
print('################################################')
from datetime import datetime
birth_date = str(input('Your birth date in \'DD/MM/YYYY\' : '))
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
date =list((dt_string.split(' ')[0]).split('/'))
brth_date=birth_date.split('/')
age = [int(date[0])-int(brth_date[0]),
       int(date[1])-int(brth_date[1]),
       int(date[2])-int(brth_date[2])]
print(date)
print(brth_date)
age_tu=tuple(age)
def age_calc(age_tu):
    if age[0] < 0 and age[1] == 0:
        print('you are alomost',age[2])
        print('You are exactly ',age[2]-1,'years , and 11 months  and ,',30 + age[0],'days')
    elif age[0] >0 and age[1] < 0 :
        print('you are alomost',age[2])
        print('you are exactly',age[2]-1,'years ,and ',12 + age[1] ,'months and ' , age[0],'days')
    elif age[0] <0 and age[1] < 0 :
        print('you are alomost',age[2])
        print('you are exactly ',age[2]-1 ,'years and ',12 + age[1] ,'months and ',30 + age[0],'days')
    elif age[0] < 0 and age[1] > 0 :
        print('you are alomost',age[2])
        print('you are ',age[2],'years and ',age[1]-1,'months and ',30 + age[0])
    elif age[0] == 0 and age[1] == 0 :
        print('you are exactly ',age[2] )
    else:
        print('you are ',age[2],'years and ',age[1],'month and ',age[0],'days')
age_calc(age_tu)