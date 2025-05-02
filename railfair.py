
def rail_fare(distance, day, time):
    if distance < 5:
        fare = 3.00
    elif distance < 12:
        fare = 4.00
    else:
        fare = 5.00
    if day == "Saturday" or day == "Sunday":
        fare *= 0.9
    elif 10.00 <= time < 16.00:
        fare *= 0.9
    return fare

# What do these return?
# (a) `rail_fare(4, "Monday", 8.00)`
# (b) `rail_fare(15, "Saturday", 14.00)`
# (c) `rail_fare(8, "Tuesday", 18.00)`
