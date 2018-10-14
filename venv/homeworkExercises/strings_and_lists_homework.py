"""
In SuperCigarette company questionaries are collected everyday by hostesses. 
By end of each day secretary inserts values into system. 
Each record is name, email and age of a user.
There is a need to automate:
        - creating unique usernames (just for the list provided below, no database of course!)
        - creating dedicated string message for under age user
        - validate email
        - validate age
        - prepare dedicated message for under age user
        - proper exceptions handling is nice thing to have
Our programmer had time just to do some of the work.
Please finish what he started so main() function gives us what is described above
"""

list_of_users = [
                ['Pawel', 'pawel@gmail.com', '1956'],
                ['Piotr', 'piottre@gmail.com', '1958'],
                ['Georgina', 'georgia99@gmail.com', '1999'],
                ['Jolanta', 'jola.por87@wp.pl', '1987'],
                ['Karolina Maria', 'karola.maria.kwiatkowska.gmail.com', '1994'],
                ['Piotr', 'piotr58starachowski@gmail.com', '1958'],
                ['Piotr', 'piotr.konieczny@wp.pl', '1999'],
                ['Zenon', '123zenek@gmail.com', '1999'],
                ['Karolina', 'karolina626@gmail.com', '2000']
                ]

def create_usernames_list(list_with_users_info):
        """
        Function adds new username to a list if all fields from questionarie are valid
        param: list_with_users_info, list with user relevanat information
        return: list with new unique usernames
        """

        # defining the new list
        # list_with_users_info = []
        # add new username to the list if all fields from questionaria are valids. This means:
        # - name != null
        # - email has proper validation
        # - age != null


def create_message_for_underage_user(user: string, age: int) -> str:
        """
        param: user, string users name
        param: age, int with age of a user
        return: string message with unique value for specific user
        """
        message = "Dear USER, your age AGE is less then 18, which is needed for parchusing nicotine products. \
                   You can still join our community but with limited rights for parchuse."

        # print me
        for i in range(len(list_of_users)):
            user = list_of_users[i][0]
            age = 2018 - int(list_of_users[i][2])
            if age < 18:
                print(user, message)

def validate_email(email: str) -> bool:
        """
        param: email, string with email
        return: True if email is valid, False if invalid
        """
        return True

def validate_age(age: int) -> bool:
        return True

def create_list_of_full_rights_users(list_with_users_info: list) -> list:
        pass

def create_list_of_underage_users(list_with_users_info: list) -> list:
        pass

def prepare_data(list_with_users_info):
        """
        Method should return list of users that are fully priviliged and list of underage users if their data (email, age) is valid
        """
        full_rights_users = create_list_of_full_rights_users(list_with_users_info)
        underage_users = create_list_of_underage_users(list_with_users_info)
        return full_rights_users, underage_users

def main():
        full_rights_users, underage_users = prepare_data(list_of_users)
        usernames_catA = create_usernames_list(full_rights_users)
        usernames_catB = create_usernames_list(underage_users)
        print("All users that are fully privilieged: ", usernames_catA)
        print("All users that are underage: ", usernames_catB)
        for under_age_user in underage_users:
                print("Sending message to email {}".format(email))
                print("Message body:\n", create_message_for_underage_user(user, age))
