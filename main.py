# libraries
import os
import sys

# variables
"""
Weights for each type of formula
"""
tsunami_weights = [0.25, 0.2, 0.15, 0.25, 0.1, 0.05]
volcano_weights = [0.3, 0.3, 0.2, 0.2]

"""
Maximum values, for each formula. 
T{var} - for tsunami, V{var} - for volcano
"""
TD = 50  # meters, maximum plate displacement
TW = 30  # meters, maximum water level change
TH = 10  # kilometers, maximum depth of tsunami core
TF = 100  # quakes per event, maximum frequency

VH = 40  # kilometers, maximum ash plume height
VG = 50000  # tons per day, maximum gas emissions
VL = 5  # kilometers cubed, maximum lava flow volume

"""
Sectors data
name = [buidling density per square kilometer, 
        number of people per square kilometer,
        average price per square meter,
        Average building/house area in square meters]
"""

sectorsNames = [
    "Hokkaido",
    "Tohoku",
    "Kanto",
    "Chubu",
    "Kansai",
    "Chugoku",
    "Shikoku",
    "Kyushu"
]

sectors = [
    [500, 64, 350000, 135],
    [700, 130, 450000, 115],
    [1500, 1200, 1200000, 80],
    [800, 300, 650000, 95],
    [1000, 600, 750000, 85],
    [600, 200, 550000, 105],
    [500, 200, 450000, 115],
    [700, 300, 650000, 100]
]

"""
Miscellaneous
"""
# colors
wht = "\033[0m"
red = "\033[31m"
grn = "\033[32m"
blu = "\033[34m"
ylw = "\033[33m"

winWelcome = [
    f"{grn}Welcome to Seismic Activity Expert System{wht}",
    "SAESv1.0",
    f"Made by {grn}ap{wht}, {grn}suksa{wht}, {grn}mark{wht}",
    f"{grn}To start press ENTER{wht}"
]

winStart = [
    f"{blu}[1] Change sector data.{wht}",
    f"{blu}[2] Change weights or other constants.{wht}",
    f"{grn}[3]{wht} Calculate Earthquake Destruction Formula.",
    f"{grn}[4]{wht} Calculate Tsunami Destruction Formula.",
    f"{grn}[5]{wht} Calculate Volcano Eruption Destruction Formula.",
    f"{red}[0] Exit.{wht}"
]

winSector = [
    f"{ylw}Pick a sector.{wht}",
    f"{grn}[1]{wht} Hokkaido",
    f"{grn}[2]{wht} Tohoku",
    f"{grn}[3]{wht} Kanto",
    f"{grn}[4]{wht} Chubu",
    f"{grn}[5]{wht} Kansai",
    f"{grn}[6]{wht} Chugoku",
    f"{grn}[7]{wht} Shikoku",
    f"{grn}[8]{wht} Kyushu",
    f"{ylw}[0] Return to previous screen{wht}"
]

winVar = [
    f"{ylw}Pick variable to change.{wht}",
    f"{ylw}Example: 3 0.35{wht}",
    "Tsunami Weights",
    f"{grn}[1]{wht} Weight for Plate Displacement = {tsunami_weights[0]}",
    f"{grn}[2]{wht} Weight for Water Level Change = {tsunami_weights[1]}",
    f"{grn}[3]{wht} Weight for Depth of Core = {tsunami_weights[2]}",
    f"{grn}[4]{wht} Weight for Frequency = {tsunami_weights[3]}",
    f"{grn}[5]{wht} Weight for Tsunami Impact Factor = {tsunami_weights[4]}",
    f"{grn}[6]{wht} Weight for Miscellaneous Effects = {tsunami_weights[5]}",
    "Volcano Weights",
    f"{grn}[7]{wht} Weight for Ash Plume Height = {volcano_weights[0]}",
    f"{grn}[8]{wht} Weight for Gas Emissions = {volcano_weights[1]}",
    f"{grn}[9]{wht} Weight for Lava Flow Volume = {volcano_weights[2]}",
    f"{grn}[10]{wht} Weight for Volcano Impact Factor = {volcano_weights[3]}",
    "Maximum Values for Tsunami",
    f"{grn}[11]{wht} Maximum Plate Displacement (TD) = {TD} meters",
    f"{grn}[12]{wht} Maximum Water Level Change (TW) = {TW} meters",
    f"{grn}[13]{wht} Maximum Depth of Core (TH) = {TH} kilometers",
    f"{grn}[14]{wht} Maximum Frequency (TF) = {TF} quakes per event",
    "Maximum Values for Volcano",
    f"{grn}[15]{wht} Maximum Ash Plume Height (VH) = {VH} kilometers",
    f"{grn}[16]{wht} Maximum Gas Emissions (VG) = {VG} tons per day",
    f"{grn}[17]{wht} Maximum Lava Flow Volume (VL) = {VL} kilometers cubed",
    f"{ylw}[0]{wht} Return to previous screen"
    ]

"""
Main program
"""

class Window:
    """
    Main class for handling terminal window

    ...

    Methods
    -------
    windowClear():
        Clears the terminal window using sys fucntion

    windowUpdate(linesPack):
        Prints the lines in the terminal, separating them with empty line
    
    windowHandler():
        Main function to handle windows (niggerlicious)
    """
    def __init__(self):
        """
        Setting the mode for the program
        """
        self.mode = -1

    def windowClear(self):
        """
        Clears the terminal window using sys fucntion
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def windowUpdate(self, linesPack):
        """
        Prints the lines in the terminal, separating them with empty line
        
        ...

        Parameters
        ----------
            linesPack : list
                list containing lines to print out
        """
        self.windowClear()
        for line in linesPack:
            print(line)
            print()

    def windowHandler(self):
        """
        Main function to handle windows (niggerlicious)
        """
        if self.mode == -1:
            self.windowUpdate(winWelcome)
            input()
            self.mode = 0

        elif self.mode == 1:
            self.windowClear()
            sys.exit()

        elif self.mode == 0:
            self.windowUpdate(winStart)
            user = input("Input: ")
            while True:
                if user in ("1", "2", "3", "4", "5", "0"):
                    self.mode = int(user) + 1
                    break
                else:
                    self.windowUpdate(winStart)
                    user = input("Input: ")

        elif self.mode == 2:
            self.windowUpdate(winSector)
            user = input("Input: ")
            while True:
                if user in ("1", "2", "3", "4", "5", "6", "7", "8", "0"):
                    if user == "0":
                        self.mode = 0
                        break

                    sector_index = int(user) - 1
                    while True:
                        self.windowClear()
                        print(f"{ylw}Pick data to change for sector:{wht} {grn}{sectorsNames[sector_index].upper()}{wht}.")
                        print(f"{ylw}Example: 3 650000{wht}")
                        print(f"{grn}[1]{wht} Building density per square kilometer = {sectors[sector_index][0]}")
                        print(f"{grn}[2]{wht} Number of people per square kilometer = {sectors[sector_index][1]}")
                        print(f"{grn}[3]{wht} Average price per square meter = {sectors[sector_index][2]}")
                        print(f"{grn}[4]{wht} Average building/house area in square meters = {sectors[sector_index][3]}")
                        print(f"{ylw}[0] Return to previous screen{wht}")

                        user_input = input("Input: ").split()
                        if not user_input:
                            print(f"{red}Invalid input! Please enter valid data.{wht}")
                            continue

                        if user_input[0] == "0":
                            break

                        try:
                            data_index = int(user_input[0]) - 1
                            new_value = int(user_input[1])

                            if 0 <= data_index < len(sectors[sector_index]):
                                sectors[sector_index][data_index] = new_value
                                print(f"{grn}Updated successfully! New value: {sectors[sector_index][data_index]}{wht}")
                            else:
                                print(f"{red}Invalid data index! Please select a number between 1 and 4.{wht}")
                        except (ValueError, IndexError):
                            print(f"{red}Invalid input format! Please use the format: <field_number> <new_value>.{wht}")
                        input(f"{blu}Press ENTER to continue...{wht}")
                    self.windowUpdate(winSector)
                    user = input("Input: ")

        elif self.mode == 3:
            global TD, TW, TH, TF, VH, VG, VL, tsunami_weights, volcano_weights

            while True:
                options = [
                    f"{ylw}Pick variable to change.{wht}",
                    f"{ylw}Example: 3 0.35{wht}",
                    "Tsunami Weights",
                    f"{grn}[1]{wht} Weight for Plate Displacement = {tsunami_weights[0]}",
                    f"{grn}[2]{wht} Weight for Water Level Change = {tsunami_weights[1]}",
                    f"{grn}[3]{wht} Weight for Depth of Core = {tsunami_weights[2]}",
                    f"{grn}[4]{wht} Weight for Frequency = {tsunami_weights[3]}",
                    f"{grn}[5]{wht} Weight for Tsunami Impact Factor = {tsunami_weights[4]}",
                    f"{grn}[6]{wht} Weight for Miscellaneous Effects = {tsunami_weights[5]}",
                    "Volcano Weights",
                    f"{grn}[7]{wht} Weight for Ash Plume Height = {volcano_weights[0]}",
                    f"{grn}[8]{wht} Weight for Gas Emissions = {volcano_weights[1]}",
                    f"{grn}[9]{wht} Weight for Lava Flow Volume = {volcano_weights[2]}",
                    f"{grn}[10]{wht} Weight for Volcano Impact Factor = {volcano_weights[3]}",
                    "Maximum Values for Tsunami",
                    f"{grn}[11]{wht} Maximum Plate Displacement (TD) = {TD} meters",
                    f"{grn}[12]{wht} Maximum Water Level Change (TW) = {TW} meters",
                    f"{grn}[13]{wht} Maximum Depth of Core (TH) = {TH} kilometers",
                    f"{grn}[14]{wht} Maximum Frequency (TF) = {TF} quakes per event",
                    "Maximum Values for Volcano",
                    f"{grn}[15]{wht} Maximum Ash Plume Height (VH) = {VH} kilometers",
                    f"{grn}[16]{wht} Maximum Gas Emissions (VG) = {VG} tons per day",
                    f"{grn}[17]{wht} Maximum Lava Flow Volume (VL) = {VL} kilometers cubed",
                    f"{ylw}[0]{wht} Return to previous screen"
                ]
                self.windowUpdate(options)
                user = input("Input: ").split()

                if not user or user[0] == "0":
                    self.mode = 0
                    break
                try:
                    variable_index = int(user[0])
                    new_value = float(user[1])

                    if 1 <= variable_index <= 6:
                        tsunami_weights[variable_index - 1] = new_value
                        print(f"{grn}Updated successfully! New tsunami weight: {tsunami_weights[variable_index - 1]}{wht}")

                    elif 7 <= variable_index <= 10:
                        volcano_weights[variable_index - 7] = new_value
                        print(f"{grn}Updated successfully! New volcano weight: {volcano_weights[variable_index - 7]}{wht}")

                    elif variable_index == 11:
                        TD = int(new_value)
                        print(f"{grn}Updated successfully! New TD (Maximum Plate Displacement): {TD} meters{wht}")
                    elif variable_index == 12:
                        TW = int(new_value)
                        print(f"{grn}Updated successfully! New TW (Maximum Water Level Change): {TW} meters{wht}")
                    elif variable_index == 13:
                        TH = int(new_value)
                        print(f"{grn}Updated successfully! New TH (Maximum Depth of Core): {TH} kilometers{wht}")
                    elif variable_index == 14:
                        TF = int(new_value)
                        print(f"{grn}Updated successfully! New TF (Maximum Frequency): {TF} quakes per event{wht}")

                    elif variable_index == 15:
                        VH = int(new_value)
                        print(f"{grn}Updated successfully! New VH (Maximum Ash Plume Height): {VH} kilometers{wht}")
                    elif variable_index == 16:
                        VG = int(new_value)
                        print(f"{grn}Updated successfully! New VG (Maximum Gas Emissions): {VG} tons per day{wht}")
                    elif variable_index == 17:
                        VL = int(new_value)
                        print(f"{grn}Updated successfully! New VL (Maximum Lava Flow Volume): {VL} kilometers cubed{wht}")
                    else:
                        print(f"{red}Invalid selection! Please select a valid variable index.{wht}")

                except ValueError:
                    print(f"{red}Invalid input format! Use the format: <variable_number> <new_value>.{wht}")
                except IndexError:
                    print(f"{red}Invalid variable number! Try again.{wht}")
                except Exception as e:
                    print(f"{red}Unexpected error: {e}{wht}")
                input(f"{blu}Press ENTER to continue...{wht}")
        
        elif self.mode == 4:
            self.windowUpdate(winSector)
            user = input("Pick a sector: ")
            
            if user not in map(str, range(1, 9)):
                print(f"{red}Invalid sector! Returning to main menu...{wht}")
                input(f"{blu}Press ENTER to continue...{wht}")
                self.mode = 0
                return

            sector_index = int(user) - 1
            sector_name = sectorsNames[sector_index]
            sector_data = sectors[sector_index]

            try:
                depth = float(input(f"Enter Depth of epicenter (in kilometers): "))
                magnitude = float(input(f"Enter Magnitude (Richter scale): "))
                intensity = float(input(f"Enter Intensity (intensity scale): "))
                frequency = int(input(f"Enter Frequency (number of tremors per event): "))
                
                if depth <= 0 or magnitude <= 0 or intensity <= 0 or frequency <= 0:
                    print(f"{red}All values must be positive numbers! Returning to main menu...{wht}")
                    input(f"{blu}Press ENTER to continue...{wht}")
                    self.mode = 0
                    return

                numerator = 1 * 10 * 10
                denominator = depth * magnitude * intensity
                disaster_coefficient = min(1, (numerator / denominator) * frequency)

                building_density = sector_data[0]
                average_area = sector_data[3]
                price_per_sq_meter = sector_data[2]
                price = building_density * average_area * price_per_sq_meter

                damage_in_yen = disaster_coefficient * price

                population_density = sector_data[1]
                victims = disaster_coefficient * population_density

                print(f"\n{ylw}Earthquake Impact Calculation for Sector: {grn}{sector_name}{wht}")
                print(f"{blu}Depth: {grn}{depth} km{wht}")
                print(f"{blu}Magnitude: {grn}{magnitude} Richter scale{wht}")
                print(f"{blu}Intensity: {grn}{intensity} intensity scale{wht}")
                print(f"{blu}Frequency: {grn}{frequency} tremors/event{wht}")
                print(f"{red}Disaster Coefficient: {grn}{disaster_coefficient:.4f}{wht}")
                print(f"{red}Estimated Damage (in Yen): {grn}{damage_in_yen:,.2f} JPY{wht}")
                print(f"{red}Estimated Victims: {grn}{int(victims)} people{wht}\n")
                input(f"{blu}Press ENTER to continue...{wht}")

            except ValueError:
                print(f"{red}Invalid input! Please enter valid numerical values.{wht}")
                input(f"{blu}Press ENTER to return to main menu...{wht}")
            except Exception as e:
                print(f"{red}Unexpected error: {e}{wht}")
                input(f"{blu}Press ENTER to return to main menu...{wht}")
            
            self.mode = 0

        elif self.mode == 5:
            self.windowUpdate(winSector)
            user = input("Pick a sector: ")
            
            if user not in map(str, range(1, 9)):
                print(f"{red}Invalid sector! Returning to main menu...{wht}")
                input(f"{blu}Press ENTER to continue...{wht}")
                self.mode = 0
                return

            sector_index = int(user) - 1
            sector_name = sectorsNames[sector_index]
            sector_data = sectors[sector_index]

            try:
                D = float(input(f"Enter Plate Displacement (D) in meters (0 - {TD}): "))
                W = float(input(f"Enter Water Level Change (W) in meters (0 - {TW}): "))
                H = float(input(f"Enter Depth of Tsunami Core (H) in kilometers (0 - {TH}): "))
                M = float(input("Enter Magnitude (M) on the Richter scale (0 - 10): "))
                I = float(input("Enter Intensity (I) on the intensity scale (0 - 10): "))
                F = float(input(f"Enter Frequency (F) (0 - {TF}): "))

                if D < 0 or W < 0 or H < 0 or M < 0 or I < 0 or F < 0:
                    print(f"{red}All values must be positive! Returning to main menu...{wht}")
                    input(f"{blu}Press ENTER to continue...{wht}")
                    self.mode = 0
                    return

                D = min(D, TD)
                W = min(W, TW)
                H = min(H, TH)
                F = min(F, TF)

                destruction = (
                    tsunami_weights[0] * (D / TD) +
                    tsunami_weights[1] * (W / TW) +
                    tsunami_weights[2] * (H / TH) +
                    tsunami_weights[3] * (M / 10) +
                    tsunami_weights[4] * (I / 10) +
                    tsunami_weights[5] * (F / TF)
                )


                tsunami_destruction = min(1, destruction)

                building_density = sector_data[0] 
                average_area = sector_data[3] 
                price_per_sq_meter = sector_data[2] 
                price = building_density * average_area * price_per_sq_meter

                damage_in_yen = tsunami_destruction * price

                population_density = sector_data[1]
                victims = tsunami_destruction * population_density

                print(f"\n{ylw}Tsunami Impact Calculation for Sector: {grn}{sector_name}{wht}")
                print(f"{blu}Plate Displacement (D): {grn}{D} meters{wht}")
                print(f"{blu}Water Level Change (W): {grn}{W} meters{wht}")
                print(f"{blu}Depth of Tsunami Core (H): {grn}{H} kilometers{wht}")
                print(f"{blu}Magnitude (M): {grn}{M}{wht}")
                print(f"{blu}Intensity (I): {grn}{I}{wht}")
                print(f"{blu}Frequency (F): {grn}{F} events{wht}")
                print(f"{red}Tsunami Destruction Estimate: {grn}{tsunami_destruction:.4f}{wht}")
                print(f"{red}Estimated Damage (in Yen): {grn}{damage_in_yen:,.2f} JPY{wht}")
                print(f"{red}Estimated Victims: {grn}{int(victims)} people{wht}\n")
                input(f"{blu}Press ENTER to continue...{wht}")

            except ValueError:
                print(f"{red}Invalid input! Please enter valid numerical values.{wht}")
                input(f"{blu}Press ENTER to return to main menu...{wht}")
            except Exception as e:
                print(f"{red}Unexpected error: {e}{wht}")
                input(f"{blu}Press ENTER to return to main menu...{wht}")
            
            self.mode = 0

        elif self.mode == 6:
            self.windowUpdate(winSector)
            user = input("Pick a sector: ")

            if user not in map(str, range(1, 9)):
                print(f"{red}Invalid sector! Returning to main menu...{wht}")
                input(f"{blu}Press ENTER to continue...{wht}")
                self.mode = 0
                return

            sector_index = int(user) - 1
            sector_name = sectorsNames[sector_index]
            sector_data = sectors[sector_index]

            try:
                M = float(input("Enter Eruption Magnitude (M) on a scale of 0 - 8: "))
                H = float(input(f"Enter Ash Plume Height (H) in kilometers (0 - {VH}): "))
                G = float(input(f"Enter Gas Emissions (G) in tons/day (0 - {VG}): "))
                L = float(input(f"Enter Lava Flow Volume (L) in cubic kilometers (0 - {VL}): "))

                if M < 0 or H < 0 or G < 0 or L < 0:
                    print(f"{red}All values must be positive! Returning to main menu...{wht}")
                    input(f"{blu}Press ENTER to continue...{wht}")
                    self.mode = 0
                    return

                M = min(M, 8)
                H = min(H, VH)
                G = min(G, VG)
                L = min(L, VL)

                destruction = (
                    volcano_weights[0] * (M / 8) +
                    volcano_weights[1] * (H / VH) +
                    volcano_weights[2] * (G / VG) +
                    volcano_weights[3] * (L / VL)
                )
                volcano_destruction = min(1, destruction)

                building_density = sector_data[0]
                average_area = sector_data[3]
                price_per_sq_meter = sector_data[2]
                price = building_density * average_area * price_per_sq_meter

                damage_in_yen = volcano_destruction * price
                population_density = sector_data[1]
                victims = volcano_destruction * population_density

                print(f"\n{ylw}Volcano Eruption Calculation for Sector: {grn}{sector_name}{wht}")
                print(f"{red}Volcano Destruction Estimate: {grn}{volcano_destruction:.4f}{wht}")
                print(f"{red}Estimated Damage (in Yen): {grn}{damage_in_yen:,.2f} JPY{wht}")
                print(f"{red}Estimated Victims: {grn}{int(victims)} people{wht}\n")
                input(f"{blu}Press ENTER to continue...{wht}")

            except ValueError:
                print(f"{red}Invalid input! Please enter valid numerical values.{wht}")
                input(f"{blu}Press ENTER to return to main menu...{wht}")
            except Exception as e:
                print(f"{red}Unexpected error: {e}{wht}")
                input(f"{blu}Press ENTER to return to main menu...{wht}")
            
            self.mode = 0


mainWindow = Window()
while True:
    mainWindow.windowHandler()
