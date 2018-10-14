
list_of_users = [
                ['Pawel', 'pawel@gmail.com', '2010'],
                ['Piotr', 'piottre@gmail.com', '1958'],
                ['Georgina', 'georgia99@gmail.com', '1999'],
                ['Jolanta', 'jola.por87@wp.pl', '1987'],
                ['Karolina Maria', 'karola.maria.kwiatkowska.gmail.com', '1994'],
                ['Piotr', 'piotr58starachowski@gmail.com', '1958'],
                ['Piotr', 'piotr.konieczny@wp.pl', '1999'],
                ['Zenon', '123zenek@gmail.com', '1999'],
                ['Karolina', 'karolina626@gmail.com', "2015"]
                ]


message = "is under 18"

# [1] print user & message if user is under 18
for i in range(len(list_of_users)):
    user = list_of_users[i][0]
    age = 2018 - int(list_of_users[i][2])
    if age < 18:
        print(user, message)


# [2] print user name list if user data is valid  CREATE USERNAME LIST
list_with_users_info = []
for i in range(len(list_of_users)):
    user = list_of_users[i][0]
    age = 2018 - int(list_of_users[i][2])
    email = list_of_users[i][1]
    if user is not None and age <= 100:
        list_with_users_info.append(user)

print(list_with_users_info)

# [3]

for i in range(len(list_of_users)):
    email_list = []
    email = list_of_users[i][1]


print(email_list)
