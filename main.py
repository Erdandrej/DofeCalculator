from datetime import datetime

from WalkingCalculator import WalkingCalculator

if __name__ == '__main__':
    goal = int(input("Goal kilometres : "))
    start_date = datetime.strptime(input("Start date (dd.mm.YYYY) : "), "%d.%m.%Y")
    end_date = datetime.strptime(input("End date (dd.mm.YYYY) : "), "%d.%m.%Y")
    file_path = "data/dofe.txt"
    walking_calculator = WalkingCalculator(goal, start_date, end_date, file_path)

    print("\n------------------Results------------------------")
    print("Kilometer average needed per day to achieve goal : ",
          walking_calculator.calculate_remaining_average())
    print("End date based on previous average : ",
          walking_calculator.calculate_trend_end_date())
    print("Potential distance : ",
          walking_calculator.calculate_potential_distance())
