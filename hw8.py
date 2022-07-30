from datetime import datetime, timedelta


def main(users):

    d = {'Monday':[], 'Tuesday':[], 'Wednesday':[], 'Thursday':[], 'Friday':[], 'Saturday':[], 'Sunday':[]}
    d_now = datetime.now()
    for n in users:
        k = n['birthday']
        dr_in_this_year = datetime(year=d_now.year, month=k.month, day=k.day)    # дата др іменинника в цьому році
        delta_t = dr_in_this_year - d_now
        
        if ((d_now.weekday()*-1)-3)<=delta_t.days<=(6-d_now.weekday()):          # якщо др знаходиться від минулої Сб до поточної Нд відносно сьогоднішнього дня тижня
            day_w = datetime.strftime(dr_in_this_year, '%A')                     # день тижня на який припадає др іменинника
            name_w = n['name']                                                   # ім'я іменинника
            if 5<=dr_in_this_year.weekday()<=6 and delta_t.days<-3:              # якщо др припадає на минулі вихідні то додаємо данні на понеділок
                d['Monday'].append(name_w)
            else:
                d[day_w].append(name_w)
    for key, value in d.items():                                                 # прінтуємо у правильному вигляді результат
        if len(value)>0:
            print(f"{key}: {', '.join(value)}")




users = [
    {'name': 'Vova', 'birthday': datetime(year=1983, month=7, day=23)}, 
    {'name': 'Sasha', 'birthday': datetime(year=1979, month=7, day=25)}, 
    {'name': 'Billy', 'birthday': datetime(year=1999, month=4, day=24)}, 
    {'name': 'Colin', 'birthday': datetime(year=1979, month=7, day=29)}
    ]

if __name__ == '__main__':
    main(users)
