import datetime


def date_in_future(n):
    now = datetime.datetime.now()
    day = datetime.timedelta(days=n)
    future_date = now + day
    return future_date


def main():
    n = 22
    date = date_in_future(n)
    print(date)


if __name__ == '__main__':
    main()

