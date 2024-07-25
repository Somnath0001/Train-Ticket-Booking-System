# loginBackend.py

import csv
import admin_database_handler.users_table_handler as uth

# Verify If User Id and Password exists and matches from db
def verifyCredential(userId, password):
    # returns string as per the condition

    # If userId exists
    if (uth.isUserIdExists(userId)) :
        # If password is matching
        if (uth.isPasswordMatching(userId, password)) :
            return 'verifiedUser'
        # If password is not matching
        else :
            return 'incorrectPassword'
    # If userId does not exist
    else :
        return 'invalidUser'


# verify if the password matches from db
# if genuine user, place him to dashboard
# if not genuine user, place him to login page

# # Verify If User Id and Password exists and matches from db
# def verifyCredential(userId, password):
#     # check if user exists
#     with open('users.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             # list index start from 0, thus 2938 is in data[1]
#             # print(row[0], userId)
#             if (row[0] == userId):
#                 # verify password
#                 if (row[1] == password):
#                     file.close()
#                     return 'verifiedUser'
#                 else:
#                     file.close()
#                     return 'incorrectPassword'
#
#         return 'invalidUser'

# print(verifyCredential('som', 'som1'))
