import json
import os.path

if os.path.exists("text_files/config.json"):
    with open("text_files/config.json") as json_obj:
        car_data = json.load(json_obj)    
        if car_data["make"] == "" or car_data["model"] == "" or car_data["year_make"] == "":
            car_data["model"] = input("Please enter the model of the car: ")
            car_data["make"] = input("Please enter the make of the car: ")
            car_data["year_make"] = input("Please enter the year the car was made: ")
            with open("text_files/config.json", "w") as json_obj:
                json.dump(car_data, json_obj)
        else:
            print(car_data["make"]+ " "+ car_data["model"]+ " "+car_data["year_make"])
            val = input("Would you like to change the model of the car they drive? Yes or No?")
            if val == "Yes":
                car_data["make"] = input("Please enter the model of the car: ")
                with open("text_files/config.json", "w") as json_obj:
                    json.dump(car_data, json_obj)
            else:
                print("Thank you!")
else:
    with open("text_files/config.json") as json_obj:
            car_data["model"] = input("Please enter the model of the car: ")
            car_data["make"] = input("Please enter the make of the car: ")
            car_data["year_make"] = input("Please enter the year the car was made: ")
            json.dump(car_data, json_obj)
