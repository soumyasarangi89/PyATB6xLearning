def add_security(func):

    def wrapper():
        print("Security Check Passed!")
        print("Add Helmet, Gloves and Knee Pads!")
        func()
        print("After the ride, remove all the safety gear.")
        print("Ride Completed Successfully!")
        func()
    return wrapper

@add_security
def drive_ola_scooter():
    print("Driving an Ola Scooter!")

drive_ola_scooter()