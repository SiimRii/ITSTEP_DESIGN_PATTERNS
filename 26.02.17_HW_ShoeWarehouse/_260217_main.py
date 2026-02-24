
from _260217_ShoeController import ShoeController
from _260217_ShoeModel import ShoeModel
from _260217_ShoeView import ShoeView


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


model = ShoeModel()
view = ShoeView()
controller = ShoeController(model, view)


#---------------------------------------------- TESTY:

# 1) Pridanie 10 topanok
separator("TEST 1: Pridanie 10 topanok")
controller.add_shoes(1, "men", "sneakers", "white", 79.99, "Nike", 42)
controller.add_shoes(2, "women", "heels", "black", 59.99, "Zara", 38)
controller.add_shoes(3, "men", "boots", "brown", 120.00, "Timberland", 43)
controller.add_shoes(4, "women", "sneakers", "pink", 89.50, "Adidas", 39)
controller.add_shoes(5, "men", "running", "blue", 99.90, "Asics", 42)
controller.add_shoes(6, "women", "sandals", "beige", 34.99, "H&M", 37)
controller.add_shoes(7, "men", "formal", "black", 110.00, "Ecco", 44)
controller.add_shoes(8, "women", "boots", "black", 130.00, "DrMartens", 40)
controller.add_shoes(9, "men", "slides", "red", 19.99, "Puma", 41)
controller.add_shoes(10, "women", "flats", "white", 45.00, "CCC", 38)

separator("KONTROLA: Pocet topanok po pridani")
print("Ocakavam 10, mam:", len(model.get_all_shoes()))


# 2) Vypis vsetkych topanok
separator("TEST 2: Zobrazenie vsetkych topanok")
controller.display_all_shoes()


# 3) Vypis pre konkretnu velkost (existuje)
separator("TEST 3: Zobrazenie topanok pre velkost 42 (existuje)")
controller.display_shoes_in_specific_size(42)


# 4) Vypis pre konkretnu velkost (neexistuje)
separator("TEST 4: Zobrazenie topanok pre velkost 36 (neexistuje)")
controller.display_shoes_in_specific_size(36)


# 5) Celkova cena vsetkych topanok
separator("TEST 5: Celkova cena vsetkych topanok")
controller.get_price_of_all_shoes()


# 6) Mazanie existujuceho ID
separator("TEST 6: Mazanie topanok podla ID (existuje) - ID=3")
controller.delete_shoes(3)

separator("KONTROLA: Pocet topanok po vymazani ID=3")
print("Ocakavam 9, mam:", len(model.get_all_shoes()))


# 7) Mazanie neexistujuceho ID (nemalo by nic vypisat)
separator("TEST 7: Mazanie topanok podla ID (neexistuje) - ID=999")
controller.delete_shoes(999)

separator("KONTROLA: Pocet topanok po pokuse vymazat ID=999")
print("Ocakavam stale 9, mam:", len(model.get_all_shoes()))


# 8) Vypis po mazani
separator("TEST 8: Vypis vsetkych topanok po mazani")
controller.display_all_shoes()


# 9) Pokus o duplicitu (ID=2 uz existuje) - teraz sa ma vypisat didnt_add_shoes
separator("TEST 9: Pokus pridat duplicitne ID=2 (ma zlyhat)")
controller.add_shoes(2, "women", "heels", "black", 999.99, "FAKE", 38)

separator("KONTROLA: Pocet po pokuse o duplicitu")
print("Ocakavam stale 9, mam:", len(model.get_all_shoes()))


# 10) Pridanie noveho ID po duplikate (aby bolo vidno, ze pridavanie stale funguje)
separator("TEST 10: Pridanie noveho ID=11 (ma sa pridat)")
controller.add_shoes(11, "men", "sneakers", "green", 70.00, "NewBalance", 42)

separator("KONTROLA: Pocet po pridani ID=11")
print("Ocakavam 10, mam:", len(model.get_all_shoes()))


# 11) Vypis vsetkych po finalnych zmenach
separator("TEST 11: Finalny vypis vsetkych topanok")
controller.display_all_shoes()


# 12) Celkova cena po zmenach
separator("TEST 12: Celkova cena po zmenach")
controller.get_price_of_all_shoes()



