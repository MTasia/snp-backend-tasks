import datetime


def date_in_future(n):
    now = datetime.datetime.now()
    day = datetime.timedelta(days=n)
    future_date = now + day
    return str(future_date.day) + "-" + str(future_date.month) + "-" + str(future_date.year) + " " + \
           str(future_date.hour) + ":" + str(future_date.minute) + ":" + str(future_date.second)


def main():
    n = 2
    date = date_in_future(n)
    print(date)


if __name__ == '__main__':
    main()
