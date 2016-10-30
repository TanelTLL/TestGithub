from time import sleep
sisestatud_pin = ""
katseid = 3
while sisestatud_pin != "1234" and katseid > 0:
    print("Sisesta PIN-kood:")
    print("Jäänud on " + str(katseid) + " katset.")
    katseid -= 1
    sisestatud_pin = input()
if sisestatud_pin == "1234":
    print("Sisenesid pangaautomaati!")
else:
    print("Vale kood, programm lõpetab 3 sekundi pärast")
    i = 3
while i > 0:
    print(i)
    i -= 1
    sleep(1)
kontoseis = 1000
print("Kontol on " + str(kontoseis) + "EUR")
print("Sisesta mitu EUR soovid välja võtta ")
soovitud_raha = int(input())
if soovitud_raha <= kontoseis:
    kontoseis = kontoseis - soovitud_raha
    print("Välja võetud: " + str(soovitud_raha) + " eurot.")
else:
    print("Kontol ei ole nii palju raha!")    
print("Pangakontol on nüüd: " + str(kontoseis) + " eurot.")