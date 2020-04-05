import requests
import matplotlib.pyplot as plt
import datetime

try: 
    apiUrl = "https://covidtracking.com/api/us/daily"


    response = requests.get(apiUrl)
    
    print("Response code from server: "+str(response.status_code)) 

    data = response.json() 

    num = len(data) - 1
    count = 0
    
    dataList = []
    labels = []
    
    for x in range(0,num):
        dataList.append(data[count]["total"])
        labels.append(data[count]["date"])

        count += 1
        
    
    
    dataList.reverse() 
    labels.reverse()
    

    
    plt.bar(range(len(dataList)),dataList)
    plt.ylabel("Number of Cases")
    plt.xlabel("Date")
    plt.xticks(range(len(labels)),labels,rotation=90)
    plt.title("Number of new Covid 19 cases in the US")
    plt.show()
except ConnectionError: 
    print("ConnectionError LOL") 
except KeyError:
    print("Something in the api changed") 
        