from fastapi import FastAPI
import pyodbc

app = FastAPI()

# Replace with your actual SQL Server connection details
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\localDB1;DATABASE=CBEDEV001;Trusted_Connection=yes;'
)


@app.get("/rooms")
def get_rooms():
    cursor = conn.cursor()
    cursor.execute("SELECT room_number, room_description, room_price, room_floor, room_type FROM Rooms")
    rows = cursor.fetchall()
    result = [
        {
            "room_number": row[0],
            "room_description": row[1],
            "room_price": row[2],
            "room_floor": row[3],
            "room_type": row[4]
        }
        for row in rows
    ]
    return result
