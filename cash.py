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

    routes = [
        ("boreti", 1.5),
        ("rafailovichi", 2.0),
        ("stefan", 2.5)
    ]
    results = []
    total_sum = 0.0
    for route_name, price_per_card in routes:
        start = int(input(f"{route_name.title()} start number: "))
        end = int(input(f"{route_name.title()} end number: "))
        cards = end - start + 1 if end > start else 0
        sum_result = cards * price_per_card
        total_sum += sum_result
        results.append((route_name, start, end, cards, sum_result))
        print(f'''
          {route_name.title()}: {sum_result}€ ({cards} cards)
          ''')
    print(f"Total: {total_sum}€")

    for route_name, start, end, cards, _sum in results:
        cursor.execute(f"INSERT INTO {route_name.title()} (driver_id, date, ticket_start, ticket_end, sum_tick) VALUES (%s, %s, %s, %s, %s)", (drivers_id, date, start, end, cards))

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