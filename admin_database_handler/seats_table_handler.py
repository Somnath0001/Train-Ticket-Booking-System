# seats_table_handler.py

import sqlite3

# Open database connection to perform sql queries
con = sqlite3.connect('../ticket_booking.db')
cur = con.cursor()

# Code for creating seats table

# cur.execute('''create table if not exists seats
#             (trainNo int not null,
#             coachType text not null,
#             coachNo int not null,
#             seatNo int not null,
#             berth text,
#             berthType int,
#             isRac int,
#             primary key(trainNo, coachType, coachNo, seatNo)
#             )''')

# cur.execute('''insert into seats values(12345, 'A', 1, 1, 'Upper', 0, 0)''')

# Lets say train 12345 has
# coachA -> 3 -> 30 seats each
# coachB -> 7 -> 45 seats each
# coachC -> 15 -> 70 seats each

'''
# Code for populating insert command for seats table
trainNo = 12345
for i in range(0,100) :
    # print(trainNo)
    trainNo += 1
    berth = 'Upper'
    # code for coachA
    coachType = 'A'
    for coachNo in range(1, 4) :
        for seatNo in range(1, 31) :
            # print(trainNo, 'A', coachNo, seatNo, berth, 0, 0)
            cur.execute("insert or ignore into seats (trainNO, coachType, coachNo, seatNo, berth, berthType, isRac) values(?, ?, ?, ?, ?, ?, ?)",(trainNo, coachType, coachNo, seatNo, berth, 0, 0))
            if (berth == 'Upper') :
                berth = 'Lower'
                # print('pos1: ', berth)
            else :
                berth =  'Upper'
                # print('pos2: ', berth)
    # code for coachB
    coachType = 'B'
    for coachNo in range(1, 8) :
        for seatNo in range(1, 46) :
            # print(trainNo, 'A', coachNo, seatNo, berth, 0, 0)
            cur.execute("insert or ignore into seats (trainNO, coachType, coachNo, seatNo, berth, berthType, isRac) values(?, ?, ?, ?, ?, ?, ?)",(trainNo, coachType, coachNo, seatNo, berth, 0, 0))
            if (berth == 'Upper') :
                berth = 'Lower'
                # print('pos1: ', berth)
            else :
                berth =  'Upper'
                # print('pos2: ', berth)

    # code for coachC
    coachType = 'C'
    for coachNo in range(1, 13) :
        for seatNo in range(1, 71) :
            # print(trainNo, 'A', coachNo, seatNo, berth, 0, 0)
            cur.execute("insert or ignore into seats (trainNO, coachType, coachNo, seatNo, berth, berthType, isRac) values(?, ?, ?, ?, ?, ?, ?)",(trainNo, coachType, coachNo, seatNo, berth, 0, 0))
            if (berth == 'Upper') :
                berth = 'Lower'
                # print('pos1: ', berth)
            else :
                berth =  'Upper'
                # print('pos2: ', berth)

# Code for generating trainNo (12345 - 12445) : total 100 trains
trainNo = 12345
for i in range(0,100) :
    # print(trainNo)
    trainNo += 1
'''


# for row in cur.execute('''select * from seats where trainNO = 12346'''):
#     print(row)


# cur.execute("select * from seats where trainNo = 12422")
# print(cur.fetchall())

# Commit and close the database connection
# con.commit()
# con.close()