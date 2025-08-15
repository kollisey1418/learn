import psycopg2
import logging
from datetime import datetime


# logging setup
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,

)
# cannection to database
conn = psycopg2.connect(
    dbname="db_learning",
    user="postgres",
    password="0000",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()


for cash_1 in range(5):
# logic for tickets control
    name = input("Driver name: ")
    last_name = input("Driver last name: ")
    cursor.execute("SELECT id FROM drivers WHERE first_name = %s AND last_name =%s", (name, last_name))
    result_dr = cursor.fetchone()
    if result_dr:
        drivers_id = result_dr[0]
    else:
        cursor.execute("INSERT INTO drivers (first_name, last_name) VALUES (%s, %s) RETURNING id", (name, last_name))
        drivers_id = cursor.fetchone()[0]
    while True:
        date = input("Today's date: ")
        try:
            date = datetime.strptime(date, '%y-%m-%d').date()
            break
        except ValueError:
            logging.warning(f"Wrong date formate: {date}")
            print("You have entered date in an invalid format date. Please, enter date in YY-MM-DD")
    boreti_start = int(input("Boreti start number: "))
    boreti_end = int(input("Boreti end number: "))
    rafailovichi_start = int(input("Rafailovichi start number: "))
    rafailovichi_end = int(input("Rafailovichi end number: "))
    stefan_start = int(input("Sveti Stefan start number: "))
    stefan_end = int(input("Sveti Stefan end number: "))
    cards_b = int(boreti_end - boreti_start + 1) if boreti_end > boreti_start else 0
    cards_r = int(rafailovichi_end - rafailovichi_start + 1) if rafailovichi_end > rafailovichi_start else 0
    cards_s = int(stefan_end - stefan_start + 1) if stefan_end > stefan_start else 0
    result_b = float(cards_b * 1.5)
    result_r = float(cards_r * 2)
    result_s = float(cards_s * 2.5)
    sum_result = float(result_b + result_r + result_s)
    print(f'''
          Boreti: {result_b}€ ({cards_b} cards)
          Rafailovichi {result_r}€ ({cards_r} cards)
          Sveti Stefan {result_s}€ ({cards_s} cards)
          Total: {sum_result}€
          ''')
    cursor.execute("INSERT INTO boreti (driver_id, date, ticket_start, ticket_end, sum_tick) VALUES (%s, %s, %s, %s, %s)", (drivers_id, date, boreti_start, boreti_end, cards_b))
    cursor.execute("INSERT INTO rafailovichi (driver_id, date, ticket_start, ticket_end, sum_tick) VALUES (%s, %s, %s, %s, %s)", (drivers_id, date, rafailovichi_start, rafailovichi_end, cards_r))
    cursor.execute("INSERT INTO stefan (driver_id, date, ticket_start, ticket_end, sum_tick) VALUES (%s, %s, %s, %s, %s)", (drivers_id, date, stefan_start, stefan_end, cards_s))

# fuel consumption
    mileage = float(input("Kilometers per day: "))  
    liters = float(input(f"Liters pet day: "))
    price = float(1.35)
    cons = ((liters / mileage) * 100)
    print(f"Fuel consumption per 100 km: {cons:.2f} liters per 100km")

    cursor.execute("INSERT INTO fuel (driver_id, date, kilometrs, liters, price_per_liter) VALUES (%s, %s, %s, %s, %s)", (drivers_id, date, mileage, liters, price))

# effeciency
    fuel_cost_total = (liters * price)
    eff_per_km = ((sum_result - fuel_cost_total) / mileage)
    print(f'''
            Fuel cost: {fuel_cost_total:.2f}€
            Effeciency: {eff_per_km:.2f}€ per km
        ''')

    cursor.execute("INSERT INTO summary (driver_id, date, total_income, fuel_cost, effeciency_per_km) VALUES (%s, %s, %s, %s, %s)", (drivers_id, date, cons, fuel_cost_total, eff_per_km))
    conn.commit()
    cursor.close()
    conn.close()