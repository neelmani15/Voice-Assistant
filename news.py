import requests
api_address="https://newsapi.org/v2/top-headlines?country=in&apiKey=5f31aabdc1a0491a9bb8e6fa7dcb4ee3"
json_data = requests.get(api_address).json()
#print(json_data)
arr=[]
arr1=[]
def news():
    for i in range(5):
        arr.append("Number"+ str(i+1) +":" + json_data["articles"][i]["title"]+".")
        arr1.append("Description: "+json_data["articles"][i]["description"]+".")
    return arr,arr1
#array,array1=news()
#for i in range(len(array)):
#    print(array[i])
#    print(array1[i])
#print(array)
#print(array1)
