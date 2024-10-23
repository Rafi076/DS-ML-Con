def hours_to_minutes(hours):
    minutes = hours * 60
    return minutes

hours = int(input("Enter Hour: "))
minutes = hours_to_minutes(hours)
print(f"{hours} hours is equal to {minutes} minutes.")
