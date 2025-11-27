import pandas as pd
import matplotlib.pyplot as plt

#Load ISRO 1979-2023 mission launch dataset
sheet_id = '1gEADrXaokIpnIV90T1-3dkIiBNi5fH_6Y30d42SevOw'
xls = pd.ExcelFile(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx")
df = pd.read_excel(xls, 'ISRO mission launches', header = 0)

#r
df['Mission Name'] = df['Launch Date']
df['Launch Date'] = df['Launch Vehicle']
df['Launch Vehicle'] = df['Launch Vehicle.1']
df = df.drop(columns=['Launch Vehicle.1'])
df_new = df.dropna(subset="Orbit Type")
df_new2 = df_new.dropna(subset=['Application'])
df_new2 = df_new2.copy()
df_new2['Year'] = df_new2['Launch Date'].dt.year
def missions_by_applications(df):
    plt.clf()
    application_data = df_new2['Application'].value_counts()
    plt.figure(figsize=(8,8))
    application_data.plot(kind= 'pie', autopct='%1.0f%%')
    plt.title('ISRO (Indian Space Research Organization) Satelite Purposes from 1979-2023')
    plt.show()
    plt.pause(0.001) 
def missions_per_year(df):
    plt.clf()
    mission_annual_count = df['Year'].value_counts().sort_index()
    mission_annual_count.plot(kind='bar')
    plt.xlabel('Year')
    plt.ylabel('Launch Count')
    plt.title('ISRO Missions Per Year')
    plt.show()
    plt.pause(0.001)
def missions_by_vehicle(df):
    plt.clf()
    vehicle_number = df['Launch Vehicle'].value_counts()
    plt.figure(figsize=(11,6))
    vehicle_number.plot(kind= 'bar')
    plt.title('ISRO Missions by Launch Vehicle Type')
    plt.show()
    plt.pause(0.001) 
def missions_by_orbit(df):
    plt.clf()
    orbit_number = df_new2['Orbit Type'].value_counts()
    plt.figure(figsize=(11,6))
    orbit_number.plot(kind='barh')
    plt.xlabel('Orbit Type')
    plt.ylabel('Count')
    plt.title('ISRO (Indian Space Research Organization) Mission Launches by Orbit Type, 1979-2023')
    plt.show()
    plt.pause(0.001) 
def show_menu():
    print('---ISRO (Indian Space Research Organization) Mission Analysis, 1979-2023---')
    print('\n---Select from the menu below---')
    print('Option 1: Missions by Year')
    print('Option 2: Missions by Purpose')
    print('Option 3: Missions by Launch Vehicle')
    print('Option 4: Missions by Orbit Type')
    print('Option 5: EXIT')
def activate():
    while True:
        show_menu()
        selection = input('What do you want to analyze today? (Enter a number, 1-5) ')

        if selection == '1':
            missions_per_year(df_new2)
        elif selection == '2':
            missions_by_applications(df_new2)
        elif selection == '3':
            missions_by_vehicle(df_new2)
            plt.show
        elif selection == '4':
            missions_by_orbit(df_new2)
        elif selection == '5':
            print('Thanks for learning about ISRO!')
            break
        else:
            print('Please enter only a number between 1-5, and nothing else. Example: 5')
            
activate()

