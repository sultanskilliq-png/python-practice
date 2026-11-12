from datetime import datetime
now = datetime.now()

# print(now.day)
# timestamp = now.timestamp()
# print('timestamp', timestamp)


# # new_year= datetime(2027,1,1)
# # print(new_year.minute)
# from datetime import timedelta
# t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
# t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
# t3 = t1 - t2
# print("t3 =", t3)

# from datetime import datetime

# now = datetime.now()

# print(
#     f"Day: {now.day}, Month: {now.month}, Year: {now.year}, "
#     f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}"
# )

# print("Timestamp:", now.timestamp())

# print(now.strftime("%y:%m:%d"))


from datetime import datetime,date


# print("The time is:", now.strftime("%m/%d/%Y, %H:%M:%S"))


# date_string = "5 December, 2019"

# date_object = datetime.strptime(date_string, "%d %B, %Y")

# print(date_object)


# now = datetime.now()
# next_year = 1,1,2027
# culuct = next_year - now
# print(culuct)


# now = datetime.now()
# next_year = datetime(now.year + 10,2,1,23)
# result = next_year - now
# print(result)


# noww =datetime.now()
# next_year = datetime(now.year - 1,1,1)
# result = next_year - noww
# print(result)


# now = datetime(now)
# date_string = 'January 1, 1970'
# trans = datetime.strptime(date_string,'%B %d,%Y')
# print(trans)


# now = datetime.now()
# past_years = datetime(1970,1,1)
# result = now - past_years
# result_2 = result.days/365
# print(f'that your result bye bye: {result_2}')


# time_now = date (year=1970,month=1,d=1)
# time_now_2 = date (year=2026,month=1,day=1)
# result = time_now_2 - time_now
# print(f'hiiiiii bey bey {result}')


# arrivals = ["Ali", "Omar", "Sara", "Khaled"]
# name = "Sara"

# order = arrivals.index(name)
# print(order)  # 2
