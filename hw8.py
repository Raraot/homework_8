from datetime import datetime, timedelta


def main(users):
    
    d_now = datetime.now()
    d2 = {}
    list_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  # для правильного відображення важливо сформувати корректний словник
    n_list = list_day[d_now.weekday():]+list_day[:d_now.weekday()]+['Next Monday']
    for elem in n_list:
        d2[elem] = []                                                                          # словник із днем початку від сьогоднішнього дня тижня

    for n in users:
        k = n['birthday']
        dr_in_this_year = datetime(year=d_now.year, month=k.month, day=k.day)                   # дата др іменинника в цьому році
        delta_t = dr_in_this_year - d_now
        if -1<=delta_t.days<6:                                                                  # якщо др знаходиться від сьогодні і на неділю вперед
            day_w = datetime.strftime(dr_in_this_year, '%A')                                    # день тижня на який припадає др іменинника
            name_w = n['name']                                                                  # ім'я іменинника
            if 5<=dr_in_this_year.weekday()<=6 and delta_t.days>=4 and (5<=d_now.weekday()<=6 or d_now.weekday()==0):
                d2['Next Monday'].append(name_w)                                                # якщо зараз вихідні і др припадає на наст. вихідні - на наст. понеділок
            elif 5<=dr_in_this_year.weekday()<=6:                                               # якщо др припадає на вихідні то переносим на понеділок
                d2['Monday'].append(name_w)
            else:
                d2[day_w].append(name_w)

    for key, value in d2.items():                                                               # прінтуємо у правильному вигляді результат зі словника
        if len(value)>0:
            print(f"{key}: {', '.join(value)}")


users = [
    {'name': 'Vova', 'birthday': datetime(year=1983, month=8, day=1)}, 
    {'name': 'Sasha', 'birthday': datetime(year=1979, month=7, day=31)}, 
    {'name': 'Billy', 'birthday': datetime(year=1999, month=7, day=30)}, 
    {'name': 'Colin', 'birthday': datetime(year=1979, month=8, day=5)}
    ]

if __name__ == '__main__':
    main(users)