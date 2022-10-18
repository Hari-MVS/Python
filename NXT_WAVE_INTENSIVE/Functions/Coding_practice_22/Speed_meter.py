def get_speed_status(speed):
    return "Normal" if speed<60 else "Warning" if speed>=60 and speed<80 else "Over Speed"


speed = int(input())
print(get_speed_status(speed))
