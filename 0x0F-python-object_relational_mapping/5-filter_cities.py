#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
lists all cities of that state, using the
database hbtn_0e_4_usa
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    cont = 0
    sql = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
    sql_s = sql.cursor()
    sql_s.execute("""SELECT cities.id, cities.name, states.name
                     FROM cities
                     LEFT JOIN states ON cities.state_id = states.id
                     ORDER BY cities.id ASC""")
    db = sql_s.fetchall()
    for states in db:
        if states[2] == argv[4]:
            if cont > 0:
                print(", ", end="")
            print(states[1], end="")
            cont += 1
    print()
    sql_s.close()
    sql.close()
