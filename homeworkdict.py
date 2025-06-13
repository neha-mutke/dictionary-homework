
bigdb = {}

movies_2022 = {}

name1 = "Bhool Bhulaiyaa2"
name2 = "Brahmastra"

casting1 = ['Tabu', 'Kartik Aaryan', 'Kiara Advan' ]
casting2 = ["Amitabh Bachchan", "Ranbir Kapoor", "Alia Bhatt", "Mouni Roy", "Nagarjuna" ]

movies_2022["Bhool Bhulaiyaa2"] = ['Tabu', 'Kartik Aaryan', 'Kiara Advan']
movies_2022["Brahmastra"] = ["Amitabh Bachchan", "Ranbir Kapoor", "Alia Bhatt", "Mouni Roy", "Nagarjuna"]
print(type(movies_2022),movies_2022)

print("==================*******************========================****************===============")

movies_2023 = {}

name3 = "Pathaan"
name4 = "Tu Jhoothi Main Makkaar"

casting1 = ["SRK","Deepika Padukone","John Abraham","Dimple Kapadia","Ashutosh Rana"]
casting2 = ["Ranbir Kapoor","Shraddha Kapoor","Dimple Kapadia","Boney Kapoor","Kartik Aaryan"]

movies_2023["Pathaan"] = ["SRK","Deepika Padukone","John Abraham","Dimple Kapadia","Ashutosh Rana"]
movies_2023["Tu Jhoothi Main Makkaar"] =["Ranbir Kapoor","Shraddha Kapoor","Dimple Kapadia","Boney Kapoor","Kartik Aaryan"]  
print(movies_2023)

print("==================*******************========================****************===============")

movies_2024 = {}

name5 = "Shaitaan"
name6 = "Bade Miyan Chote Miyan"

casting1 = ["Ajay Devgn","R. Madhavan","Jyothika","Janki Bodiwala"]
casting2 = ["Akshay Kumar","Tiger Shroff","Manushi Chhillar","Alaya F"]

movies_2024["Shaitaan"] = ["Ajay Devgn","R. Madhavan","Jyothika","Janki Bodiwala"]
movies_2024["Bade Miyan Chote Miyan"] = ["Akshay Kumar","Tiger Shroff","Manushi Chhillar","Alaya F"]
print(movies_2024)

print("==================*******************========================****************===============")

movies_2025 = {}

name7 = "Kesari Chapter2" 
name8 = "Sikandar"

casting1 = [ "Akshay Kumar", "R. Madhavan", "Ananya Panday" ]
casting2 = ["Salman Khan","Rashmika Mandanna","Kajal Aggarwal", "Sanjay Kapoor", "Prateik Babbar"]

movies_2025["Kesari Chapter2"] = ["Akshay Kumar", "R. Madhavan", "Ananya Panday"]
movies_2025["Sikandar"] = ["Salman Khan","Rashmika Mandanna","Kajal Aggarwal", "Sanjay Kapoor", "Prateik Babbar"]
print(movies_2025)

print("==================*******************========================****************===============")
bigdb[2022]=movies_2022
bigdb[2023]=movies_2023
bigdb[2024]=movies_2024
bigdb[2025]=movies_2025
print(type(bigdb))
print(bigdb)

print("==================*******************========================****************===============")

## slicing the big dictionary
print(bigdb[2022][name1][0])  #Tabu
print(bigdb[2022][name2][0])  #Amitabh Bachchan
print(bigdb[2023][name3][0])  #SRK
print(bigdb[2023][name4][0])  #Ranbir kapoor
print(bigdb[2024][name5][0])  #Ajay devgan
print(bigdb[2024][name6][0])  #Akshay kumar
print(bigdb[2025][name7][0])  #Akshay kumar
print(bigdb[2025][name8][0])  #Salman khan
print(bigdb[2023][name3][2])  #john abhram random accesing

print("==================*******************========================****************===============")

print(bigdb.keys()) 

print("==================*******************========================****************===============")
 
print(bigdb.values()) 

print("==================*******************========================****************===============")
 
print(bigdb.items())

print("==================*******************========================****************===============")
for names in bigdb.keys():
    print(names,"====>",bigdb[names])

print("==================*******************========================****************===============")

n=input("enter name of actor you want to count :- ")
count=0
for year,dict in bigdb.items():
    for movie,cast in dict.items():
        for actor in cast:
            if actor==n :
                print(year)
                print(actor)
                print(movie)
                count+=1
print("movies on given actor work on :-",count)
            
print("==================*******************========================****************===============")

for k,v in bigdb.items():
    print(k,"===>",v)   

for t in bigdb.items():
    k,v=t            
print(t)

print("==================*******************========================****************===============")


count=0
search_value = input("Enter value to count: ") 
for k,v in bigdb.items():
    for cast in k and v :
        if cast ==  search_value :   
           count+=1
           print(cast,"===>",count,k,v)
         
print("==================*******************========================****************===============")


