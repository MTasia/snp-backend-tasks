import datetime


def date_in_future(n = 0):
    now = datetime.datetime.now()
    day = datetime.timedelta(days=n)
    future_date = now + day
    return (str(future_date.day) if future_date.day >= 10 else "0" + str(future_date.day)) + "-" + \
           (str(future_date.month) if future_date.month >= 10 else "0" + str(future_date.month)) + "-" + \
           (str(future_date.year)) + " " + \
           (str(future_date.hour) if future_date.hour >= 10 else "0" + str(future_date.hour)) + ":" + \
           (str(future_date.minute) if future_date.minute >=10 else "0" + str(future_date.minute)) + ":" + \
           (str(future_date.second) if future_date.second >= 10 else "0" + str(future_date.second))


def main():
    n = 70
    date = date_in_future(n)
    print(date)


if __name__ == '__main__':
    main()
