import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Welcome Message
print("\nWelcome to the Food Adulteration Analysis Tool!")

# Define the menu data
menu_data = {
    1: "Samples Tested(Dataframe)",
    2: "Civil Cases on Food Adulteration(Dataframe)",
    3: "Criminal Cases on Food Adulteration(Dataframe)",
    4: "Penalties Levied(Dataframe)",
    5: "Product Category Distribution",
    6: "Commonly Adulterated Products",
    7: "Samples Tested vs. Adulterated (Line Graph)",
    8: "Percentage of Adulterants Used",
    9: "Highest and Lowest Adulteration Rates",
    10: "Exit"
}

# Menu Options as a Series
menu_options = pd.Series(menu_data)

# Display the Menu
print("\nFood Adulteration Analysis Menu:")
print(menu_options)

# Load the initial information CSV file
information = pd.read_csv("C://Users//sherin//Desktop//IP project//ip-main//New folder//information.csv")

# Start the interactive menu loop
while True:
    # Get User Choice
    choice = int(input("\nEnter your choice: "))

    # Handle User Choice
    if choice == 1:
        # Samples Tested
        data1 = pd.read_csv("C://Users//sherin//Desktop//IP project//samples.csv")
        sample = pd.DataFrame(data1)
        print("Samples tested for adulteration:")
        print(sample)
        print("_______________________________________________________________________")

    elif choice == 2:
        # Civil Cases
        data2 = pd.read_csv("C://Users//sherin//Desktop//IP project//civil.csv")
        civil = pd.DataFrame(data2)
        civil = civil.replace('NA', np.nan)
        print("Civil Cases on Food Adulteration:")
        print(civil)
        print("_______________________________________________________________________")

    elif choice == 3:
        # Criminal Cases
        data3 = pd.read_csv("C://Users//sherin//Desktop//IP project//criminal cases.csv")
        criminal_cases = pd.DataFrame(data3)
        criminal_cases = criminal_cases.replace('NA', np.nan)
        print("Criminal Cases on Food Adulteration:")
        print(criminal_cases)
        print("_______________________________________________________________________")

    elif choice == 4:
        # Penalties Levied
        data4 = {'Year': ['2020', '2021', '2022', '2023'],
                 'No_of_samples': [69850, 77530, 91570, 88310],
                 'Percentage_of_non_conforming_samples': [22, 23, 25, 27]}
        penalty = pd.DataFrame(data4)
        print("A.Number of non conforming samples")
        print(penalty)
        print("_______________________________________________________________________")
        data_4 = {'No_of_Cases_Launched': [11200, 12670, 15360, 17600],
                  'Total_Conviction': [2300, 2650, 3010, 4380],
                  'Amount_Raised_by_Penalties_Rs': [146729087, 159834617, 193459153, 239120874]}
        penalty2 = pd.DataFrame(data_4)
        print("Penalties levied on adulterated foods:")
        print(penalty2)
        print("_______________________________________________________________________")

    elif choice == 5:
        # Product Category Distribution
        data5 = {
            'Product Category': ['Fishery and seafood products', 'Vegetable and vegetable products', 'Fruit and fruit products',
                                 'Non-chocolate candy and chewing gum', 'Bakery products/dough/mix/icing',
                                 'Spices, flavors, and salts', 'Cheese and cheese products'],
            '1998-2004': [1800, 1300, 900, 700, 600, 500, 400],
            '2005-2013': [2300, 1600, 1200, 900, 800, 700, 600]
        }
        product = pd.DataFrame(data5)
        product.plot(kind='barh', x='Product Category', figsize=(10, 6), color=['#1f77b4', '#ff7f0e'], width=0.7)
        plt.title('Product Quantity Distribution (1998-2004 vs 2005-2013)')
        plt.xlabel('Quantity')
        plt.ylabel('Product Category')
        plt.legend(title='Year Range')
        plt.savefig("C://Users//sherin//Desktop//IP project//ip-main//images//multiple bar.png")
        plt.show()

    elif choice == 6:
        # Commonly Adulterated Products(Pie Chart)
        slices = [30, 24, 31, 12, 3]
        Category = ['Fruits', 'Vegetables', 'Dairy Products', 'Spices', 'Other Products']
        exp = [0, 0, 0.2, 0, 0]
        plt.pie(slices, labels=Category, startangle=90, explode=exp, shadow=True, autopct='%.1F%%')
        plt.title('Commonly Adulterated Food Products')
        plt.legend()
        plt.savefig("C://Users//sherin//Desktop//IP project//ip-main//images//pie chart.png")
        plt.show()

    elif choice == 7:
        # Samples Tested vs. Adulterated (Line Graph)
        categories = ['2011-12', '2012-13', '2013-14']
        values1 = [64593, 69949, 72200]
        values2 = [8247, 10380, 13571]
        values3 = [6845, 5840, 10235]
        x = np.arange(len(categories))
        plt.plot(x, values1, label='No.of Samples Examined', color='green', linestyle='dotted', marker='o')
        plt.plot(x, values2, label='No.of Samples found Non-Conforming', color='purple', linestyle='dotted', marker='o')
        plt.plot(x, values3, label='No.of prosecutions Launched', color='pink', linestyle='dotted', marker='o')
        plt.xlabel('Years')
        plt.xticks(x, categories)
        plt.ylabel('Values')
        plt.title('Samples Tested and Found Adulterated')
        plt.legend()
        plt.savefig("C://Users//sherin//Desktop//IP project//ip-main//images//Line graph.png")
        plt.show()

    elif choice == 8:
        # Percentage of Adulterants Used (Histogram)
        adulterants = ['Water', 'Urea', 'Starch', 'AR', 'RF', 'Sorbitol', 'Glucose', 'C-Sugar', 'AS', 'Na-Soda', 'S&P', 'V. Oil',
                       'Formalin', 'H202', 'B-Acid', 'Detergent', 'H.Chlorite']
        positive_percentages = [91.0, 27.0, 15.0, 9.0, 24.0, 3.0, 10.0, 31.0, 13.0, 11.0, 19.0, 19.0, 20.0, 15.0, 12.0, 4.0, 5.0]
        plt.figure(figsize=(10, 6))
        plt.bar(adulterants, positive_percentages, align='edge', color='skyblue', width=1, edgecolor='black')
        plt.xlabel('Adulterant')
        plt.ylabel('Positive (%)')
        plt.title('Percentage of Adulterants used in the foods')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig("C://Users//sherin//Desktop//IP project//ip-main//images//Histogram.png")
        plt.show()

    elif choice == 9:
        # Highest and Lowest Adulteration Rates
        dataa = {'Uttar Pradesh': 52.32, 'Tamil Nadu': 45.39, 'Jharkhand': 41.68}
        datab = {'Arunachal Pradesh': 3.78, 'Goa': 5.67, 'Uttarakhand': 4.63}
        highest = pd.Series(dataa)
        print("Highest adulteration rate in India by State:")
        print(highest)
        print("_______________________________________________________________________")
        lowest = pd.Series(datab)
        print("Lowest adulteration rate in India by State:")
        print(lowest)
        print("_______________________________________________________________________")
        # Combine both highest and lowest into a DataFrame for plotting
        data_combined = pd.DataFrame({
            'Highest Adulteration': highest,
            'Lowest Adulteration': lowest
        })

        # Plotting the bar graph
        data_combined.plot(kind='bar', figsize=(10, 6), color=['pink', 'paleturquoise'])
        plt.title('Highest vs. Lowest Adulteration Rates by State')
        plt.xlabel('States')
        plt.ylabel('Adulteration Rate (%)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.legend(title="Adulteration Rates")
        plt.savefig("C://Users//sherin//Desktop//IP project//ip-main//images//bar graph.png")
        plt.show()

    elif choice == 10:
        # Exit
        print("Thank you for using the Food Adulteration Analysis Tool!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 10.")
