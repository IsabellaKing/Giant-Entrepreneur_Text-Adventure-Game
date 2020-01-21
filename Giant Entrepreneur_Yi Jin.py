#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on Sun Oct 13 18:37 2019

@Author: Yi Jin
"""

"""
DocString:

    1) Introduction:
    Just like the name of this game --- 'Giant Entrepreneur', it is designed 
    for the people who have a dream to be an entrepreneur but can not achieve
    it in their real life. Additionally, It can also be regarded as a 
    prep for those who are preparing to be a real entrepreneur.
    
    This game consists of four levels:
    Level 1: Start from scratich
    Level 2: Build up your team
    Level 3: Sell your product/service
    Level 4: Evaluate profit and loss
    
    2) Something I can improve:
    - The plot graph I made can only be shown in a seperate cell. 
      Maybe I need to learn more advanced knowledge about how to display a 
      plot graph in a pop-up screen.
    
"""
# Import all the packages and libraries needed

get_ipython().system('pip install pygame')
get_ipython().system('pip install Pillow')
import pygame
import time, sys, random
import matplotlib.pyplot as plt
from tqdm import tqdm
from sys import exit
from random import randint
from PIL import Image

# Background music may be loading for a few seconds.

### Intro ###

def intro():
    
    print("""
     $$$$$$\  $$\                      $$\     
    $$  __$$\ \__|                     $$ |    
    $$ /  \__|$$\  $$$$$$\  $$$$$$$\ $$$$$$\   
    $$ |$$$$\ $$ | \____$$\ $$  __$$\\_$$  _|  
    $$ |\_$$ |$$ | $$$$$$$ |$$ |  $$ | $$ |    
    $$ |  $$ |$$ |$$  __$$ |$$ |  $$ | $$ |$$\ 
    \$$$$$$  |$$ |\$$$$$$$ |$$ |  $$ | \$$$$  |
     \______/ \__| \_______|\__|  \__|  \____/ 
                                                                                                                                

    $$$$$$$$\            $$\                                                                                               
    $$  _____|           $$ |                                                                                              
    $$ |      $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\  
    $$$$$\    $$  __$$\\_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\ 
    $$  __|   $$ |  $$ | $$ |    $$ |  \__|$$$$$$$$ |$$ /  $$ |$$ |  \__|$$$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |$$ |  \__|
    $$ |      $$ |  $$ | $$ |$$\ $$ |      $$   ____|$$ |  $$ |$$ |      $$   ____|$$ |  $$ |$$   ____|$$ |  $$ |$$ |      
    $$$$$$$$\ $$ |  $$ | \$$$$  |$$ |      \$$$$$$$\ $$$$$$$  |$$ |      \$$$$$$$\ $$ |  $$ |\$$$$$$$\ \$$$$$$  |$$ |      
    \________|\__|  \__|  \____/ \__|       \_______|$$  ____/ \__|       \_______|\__|  \__| \_______| \______/ \__|      
                                                 $$ |                                                                  
                                                 $$ |                                                                  
                                                 \__|                                                                  

    Hello and welcome to GIANT ENTREPRENEUR!!!!!!
    Are you ready to build your own BUSINESS EMPIRE? """)

    pygame.mixer.init()
    pygame.mixer.music.load('BGM.wav')
    pygame.mixer.music.play(3)

intro()

### Game Start ###

def game_start():
    global player_name
    global gender
    global home_country
    global business_country
    global industry
    
    player_name = input("Future leader, may I have your name please? ")
    print(f"\n{player_name}, welcome on board!\n")
    
    gender = input("""
    Are you a Male/Female entrepreneur?
    * Please enter Male or Female """)

    if gender == 'Male':
        print(f"\nMr. {player_name}, do you know who is the most 高富帅 guy in the world?\n")
        input("<Press Enter to continue>")
        print("\nYep! Entrepreneur!\n")
    
    elif gender == 'Female':
        print(f"\nMs. {player_name}, do you know who is the most 白富美 lady in the world?\n")
        input("<Press Enter to get the answer!>\n")
        print("\nYep! Entrepreneur!\n")
    
    else:
        print("\nOops! I can not recognize you! Are you an alien?\n")
            
    home_country = input("\nWhich country are you from?\n")
    
    business_country = input("""
    Are you going to build a local business or a foreign one
    * Please enter Local or Foreign """)

    industry = input("\nWhich industry are you heading to?\n")

    print("\nWell...please give me a moment to make an entrepreneur profile for you! :)\n")
    
    number_of_elements = 20

    for i in tqdm(range(10)):
        time.sleep(0.5)
    print('Done')
    
    print("\nOK! Your profile is here for you!")

    print(f"""\nName: {player_name}\nGender: {gender}\nHome Country: {home_country}\nBusiness Country: {business_country}\nIndustry: {industry}""")

    input("<Press Enter to step into the next page>\n")

    for i in tqdm(range(10)):
        time.sleep(0.5)
    print("\nLoading to Level 1: Start from Scratch-------------------------------\n")

    for i in tqdm(range(10)):
        time.sleep(0.5)

    print("""
     +-+-+-+-+-+ +-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+
     |L|e|v|e|l| |1|:| |S|t|a|r|t| |f|r|o|m| |S|c|r|a|t|c|h|
     +-+-+-+-+-+ +-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+                                                                                    
    """)

game_start()


### Level 1: Start from scratch ###

def level_1():
    
    business_name = input("\nGive your business a terrific name!\n")

    product_name = input("\nWhat kind of product/service do you want to provide?\n")

    answer = 2
    while answer != 1 :
    
        fundraising_amount = input("""
        How much do you think an entrepreneur of a microbusiness needs to start up a business?

        1) >= $3,000
        2) < $3,000

        * Please Enter 1 or 2 """)
    
        if fundraising_amount == '1':
            print(f"Well done! {business_name} is totally ready to do the fundraising now!")
            answer = 1
            break
    
        elif fundraising_amount == '2':
            print("""
            Starting up a business with an amount of money less than $3,000 could be harsh,
            but you can still seek help from various fundraising channels!
            """)
            input("<Press Enter to have another try!>")
            break
    
        else:
            print("Your Answer is Invalid!")
            input("<Press Enter to have another try!>")
            continue   

    input("<Press Enter to continue>")

    capital = 100000
    response = 0      # 0 here stands for N
    while response != 1:     # 1 here stands for Y
        fundraising_channel = input("""
        Congratulations! You've received a $100,000 from an investor called Mr. Morgan!
        Do you wanna accept his offer? 
        Or, you prefer requesting a loan from the bank?

        1) Accept the offer from the Mr. Morgan
        2) Ask for a bank loan

        * Please Enter 1 or 2 """)

        if fundraising_channel == '1':
            print("Smart move!")
            input("<Press Enter to continue>")
            break
    
        elif fundraising_channel == '2':
            print("Asking for a bank loan may be a harder way for a startup business to gain large funds")
        
            choice = input("<Are you sure to do this? Y/N>")
            
            if choice == 'Y':
                input("<Press Enter to continue>")
                response = 1
                break
                
            elif choice == 'N':
                input("<Press Enter to have another try!>")
                continue
                
            else:
                print("Something Went Wrong!")
                input("<Press Enter to do it again!>")
                continue
    
        else:
            print("Your Answer is Invalid!")
            input("<Press Enter to have another try!>")

    print("\nNow you got your first bucket of money!\nAre you ready to set up your office?\nDo you feel excited?🤩")

    input("<Press Enter to continue>")

    chairs_unit_price = 45.99
    chairs_number = int(input("""
    How many chairs do you need? Let's suppose one chair costs $45.99
    *Please enter a valid number """))

    tables_unit_price = 129.87
    tables_number = int(input("""
    How many tables do you need? Let's suppose one table costs $129.87
    *Please enter a valid number """))

    computers_unit_price = 829.68
    computers_number = int(input("""
    How many computers do you need? Let's suppose one computer costs $829.68
    *Please enter a valid number """))

    telephones_unit_price = 87.63
    telephones_number = int(input("""
    How many telephones do you need? Let's suppose one telephone costs $87.63
    *Please enter a valid number """))

    shelves_unit_price = 109.43
    shelves_number = int(input("""
    How many shelves do you need? Let's suppose one shelf costs $109.43
    *Please enter a valid number """))

    printers_unit_price = 387.95
    printers_number = int(input("""
    How many printers do you need? Let's suppose one printer costs $387.95
    *Please enter a valid number """))
      
    stationery_cost = float(input("""
    How much do you think will be spent on stationeries, 
    like pens, staplers, papers, notebooks, etc.
    *Please enter a valid number --- no currency sign or comma """))

    wifi_fee_first_month = float(input("""
    How much do you think will be spent on wifi in the office for the first month?
    *Please enter a valid number --- no currency sign or comma """))

    rent_first_month = float(input("""
    How much do you think will be spent on rent for the first month?
    *Please enter a valid number --- no currency sign or comma """))

    utilities_first_month = float(input("""
    How much do you think will be spent on utilities for the first month?
    *Please enter a valid number --- no currency sign or comma """))

    print("\nDo you want to know your total cost for the first month setup?\nGive me a second to calculate for you.")

    for i in tqdm(range(10)):
        time.sleep(0.5)         

    chairs_total_cost = chairs_unit_price*chairs_number
    tables_total_cost = tables_unit_price*tables_number
    computers_total_cost = computers_unit_price*computers_number
    telephones_total_cost = telephones_unit_price*telephones_number
    shelves_total_cost = shelves_unit_price*shelves_number
    printers_total_cost = printers_unit_price*printers_number

    total_cost = chairs_total_cost + tables_total_cost + computers_total_cost + telephones_total_cost + shelves_total_cost + printers_total_cost + stationery_cost + wifi_fee_first_month + rent_first_month + utilities_first_month
    total_cost = round(total_cost, 2)
    
    print('So, the total cost for office setup would be:', total_cost)

    input("<Press Enter to continue>")

    print("""
    Good job! Now you have successfully completed the setup phase for your business!😎
    Do you like your office?
    """)
    
    # The image is extracted from https://www.bdiusa.com/working
    myImage = Image.open("office.jpg");
    myImage.show()     

    input("<Press Enter to step into the next page>\n")
    
    for i in tqdm(range(10)):
        time.sleep(0.5)
    print("\nLoading to Level 2: Build up Your Team-------------------------------\n")

    for i in tqdm(range(10)):
        time.sleep(0.5)

    print("""
     +-+-+-+-+-+ +-+-+ +-+-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+-+
     |L|e|v|e|l| |2|:| |B|u|i|l|d| |u|p| |Y|o|u|r| |T|e|a|m|
     +-+-+-+-+-+ +-+-+ +-+-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+-+
    """)
    return total_cost

### Level 2: Build up your team ###
def level_2(total_cost):

    print("""
    Now everything in the office is ready!!!Yay~✌️
    It's time for talent hunt!!!!!!!!!!!!!!!
    """)

    input("<Press Enter to continue>")

    print("""
    Just sit a while and think......
    What kinds of talents are you searching for according to the industry and business nature？
    And how much are you going to pay them each month?
    """)

    input("<Press Enter to continue>")

    print("""
    Based on the current financial condition, you can only recruit 5 talents to join your team so far.
    Please be Careful with Your Decision!!!
    """)

    input("<Press Enter to enter thinking time>")

    for i in tqdm(range(10)):
        time.sleep(0.5)
    print("\nThinking time is over!\n")

    talent_1_type = input("Enter Talent_1 Job Type: ")
    talent_2_type = input("Enter Talent_2 Job Type: ")
    talent_3_type = input("Enter Talent_3 Job Type: ")
    talent_4_type = input("Enter Talent_4 Job Type: ")
    talent_5_type = input("Enter Talent_5 Job Type: ")

    talent_1_salary = float(input("Enter Talent_1 Monthly Salary\n*Please enter a valid number --- no currency sign or comma "))
    talent_2_salary = float(input("Enter Talent_2 Monthly Salary\n*Please enter a valid number --- no currency sign or comma "))
    talent_3_salary = float(input("Enter Talent_3 Monthly Salary\n*Please enter a valid number --- no currency sign or comma "))
    talent_4_salary = float(input("Enter Talent_4 Monthly Salary\n*Please enter a valid number --- no currency sign or comma "))
    talent_5_salary = float(input("Enter Talent_5 Monthly Salary\n*Please enter a valid number --- no currency sign or comma "))

    list = [[talent_1_type, talent_1_salary],
            [talent_2_type, talent_2_salary],
            [talent_3_type, talent_3_salary],
            [talent_4_type, talent_4_salary],
            [talent_5_type, talent_5_salary]]

    for talent in list:
        print(talent)

    total_labor_cost = talent_1_salary + talent_2_salary + talent_3_salary + talent_4_salary + talent_5_salary
    total_labor_cost = round(total_labor_cost, 2)
    print('The total labor cost would be', total_labor_cost)
    
    total_cost = total_cost + total_labor_cost
    total_cost = round(total_cost, 2)
    print('So, the total cost now is going to be', total_cost)

    input("<Press Enter to step into the next page>\n")

    for i in tqdm(range(10)):
        time.sleep(0.5)
    print("\nLoading to Level 3: Sell your product/service-------------------------------\n")

    for i in tqdm(range(10)):
        time.sleep(0.5)

    print("""
     +-+-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |L|e|v|e|l| |3|:| |S|e|l|l| |y|o|u|r| |P|r|o|d|u|c|t|/|S|e|r|v|i|c|e|
     +-+-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                                                                   
    """)

    return total_cost


### Level 3: Sell you product/service ###
def level_3(total_cost):

    n = 500
    unit_cost = 14.99
    print("""
    Now your employees have completed 500 products/services production.
    Let's assume that the cost of each piece is $14.99.
    Your current task is going to sell as many products/services as you can to your customers.
    """)

    input("<Press Enter to enter thinking time>")

    print("Relax and give yourself a few seconds to think about who's gonna be your target customer group?")

    for i in tqdm(range(10)):
        time.sleep(0.5)
    print("Loading to thinking time-------------------------------")

    for i in tqdm(range(10)):
        time.sleep(0.5)

    target_customer = input("Enter your target customer group: ")

    promotion_method = input("""
    How are you going to let your customers know your products/services?
    For example: by Social Media/by Ads on TV or Internet/by billboards...
    """)
    promotion_cost = float(input("""
    If you are gonna implement your promotion method,
    how much do you think it will cost you?
    *Please enter a valid number --- no currency sign or comma
    """))

    market_place = input("""Well, now your customers may gradually start to know your products/services.
    Where are you gonna sell them?
    For example: on the official website/ in the brick and mortar stores...
    """)

    unit_retail_price = float(input("How much do you think is the most appropriate unit price for the products/services,\nwhich can cover the cost? "))

    total_cost = total_cost + n*unit_cost + promotion_cost
    total_cost = round(total_cost, 2)
    print('Now your total cost is: ', total_cost)

    input("<Press Enter to continue>")

    # sales in 1 month
    print('Since you have 500 completed products/services to sell', 'considering of the cost per unit is $14.99', 'you set the retail price as', unit_retail_price)
    print("Now, let's predict how's your total sales gonna be in the first month")
    input("<Press Enter to see the total sales prediction>")

    n = 500
    accumulated_sales = 0
    lst = []
    day = 1

    while day <= 30: 
        for days in range (0, 30):
            daily_sales = random.randint(0, 30)
            accumulated_sales = accumulated_sales + daily_sales
            lst.append(daily_sales)
            day += 1

    print(lst)
    print("The number in the list is the daily sales you are expected to achieve in the 1st month.")
    print('And, the toal sales in 1st month is:', accumulated_sales)
    
    # x axis values 
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    
    # corresponding y axis values 
    y = lst
    
    # plotting the points 
    plt.plot(x, y)
    
    # naming the x axis 
    plt.xlabel('day') 
    # naming the y axis 
    plt.ylabel('sales') 
  
    # giving a title to the graph 
    plt.title('First Month Sales') 
  
    # show the plot 
    plt.show() 
    
    input("<Press Enter to see how much you may earn in the 1st month>")

    if accumulated_sales == 500:
        total_revenue = unit_retail_price * accumulated_sales
        total_revenue = round(total_revenue, 2)
        print("Good job! Your existing products/services are all sold out!")
        print('And, your total revenue in 1st month is:', total_revenue)

    elif accumulated_sales < 500:
        total_revenue = unit_retail_price * accumulated_sales
        total_revenue = round(total_revenue, 2)
        print("Unfortunately, you have some products/services not being sold.")
        print('And, your total revenue in 1st month is:', total_revenue)

    elif accumulated_sales > 500:
        total_revenue = unit_retail_price * 500
        total_revenue = round(total_revenue, 2)
        print("""
        Evidently, your customers love your products/services! 
        However, you can only sell 500 pieces at most.
        Some of them have already preordered your products/services!
        What you need to do is to produce more next month!
        """)
    
    input("<Press Enter to step into the next page>\n")

    for i in tqdm(range(10)):
        time.sleep(0.5)
    print("\nLoading to Level 4: Evaluate profit and loss\n")

    for i in tqdm(range(10)):
        time.sleep(0.5)

    print("""
     +-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+ 
     |L|e|v|e|l| |4|:| |E|v|a|l|u|a|t|e| |P|r|o|f|i|t| |a|n|d| |L|o|s|s| 
     +-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+                                                                                   
    """)
    
    return total_cost, total_revenue

### Level 4: Evaluate profit and loss
def level_4(total_cost, total_revenue):
    
    print("Now let's see how's your business condition in the 1st month.")
    input("<Press Enter to continue>")
    
    capital = 100000
    revenue = capital + total_revenue
    
    if revenue > total_cost:
        print('Your total revenue is: ', revenue)
        print('Your total cost is: ', total_cost)
        print("YAY~ You've Made Profit!!!!!!")
        
        # The image is extracted from https://www.tripadvisor.com/Attraction_Review-g60763-d104365-Reviews-Empire_State_Building-New_York_City_New_York.html
        input("<Press Enter to retrieve your own Business Empire!!!")
        myImage = Image.open("Empire State Building.jpg");
        myImage.show()
        
    elif revenue == total_cost:
        print('Your total revenue is: ', revenue)
        print('Your total cost is: ', total_cost)
        print("You Realized Break-even!")
        
    elif revenue < total_cost:
        print('Your total revenue is: ', revenue)
        print('Your total cost is: ', total_cost)
        print("You've made a loss.")
        fail()
        
    print(f"{player_name}: Would you like to play again? (Yes/No)")
    replay = input("> ")
    replay = replay.lower()
    
    if replay == 'yes':
        game_start()
        
    else:
        print(f"{player_name}: Thanks for playing!")
        exit(0)
        
def fail():
    print("You've failed, but thanks for playing!")
    input('<Press any key to exit>\n')
    exit(0)

def main():
    a = level_1()
    b = level_2(a)
    c,d = level_3(b)
    e = level_4(c,d)
    
main()

