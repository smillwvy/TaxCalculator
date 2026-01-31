import sqlite3

def addIncomes(user, empl, savings):
    connection = sqlite3.connect("taxcalculator.db")
    cursor = connection.cursor()
    query = "INSERT INTO Incomes (empl, savings) VALUES (?, ?)"
    cursor.execute(query, (empl, savings))
    connection.commit()
    print("Saved")

def retrieveIncomes():
    connection = sqlite3.connect("taxcalculator.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Incomes")    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return rows


if __name__ == "__main__":
    addIncomes(1, 30000, 1250)
    retrieveIncomes()