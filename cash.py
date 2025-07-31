for cash_1 in range(5):
    name = input("Driver name: ")
    first_name = input("Driver first name: ")
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
    