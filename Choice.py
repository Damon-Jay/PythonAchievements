print("Je wekker gaat om 08:00 en je moet om 10:00 op school zijn. Wat doe je? Blijf je SLAPEN of STA je op?")
choice1 = input().upper()

if choice1 == 'STA':
	print("Je staat op en gaat je klaarmaken voor school")
	
elif choice1 == 'SLAPEN':
	print("Slaap, Slaap, Slaap, Stik in speeksel, slaap meer")     
else:
    print(choice1, " wasn't a valid choice")


print("Je bent uit je bed en je moet naar school ga je ETEN of NIET?")
choice2 = input().upper()

if choice2 == 'ETEN':
	print("Je eet een lekker broodje met ham en kaas")
	
elif choice2 == 'NIET':
	print("Je gaat met een lege maag naar school")     
else:
    print(choice2, " wasn't a valid choice") 

print("Je gaat naar school alleen ga je met de TREIN of ga je met de AUTO?")
choice3 = input().upper()

if choice3 == 'TREIN':
	print("Je gaat met de trein naar school")
	
elif choice3 == 'AUTO':
	print("je gaat met de auto naar school")     
else:
    print(choice3, " wasn't a valid choice") 

x = int(input("Oke je bent bij de enige echte apie hein en je wilt een broodje gehaktbal kopen van 2 euro. Hoeveel heb jij in je portomonee zitten?"))

if x <2:
    print("Je hebt te weinig doekoe om je brood te kopen")
elif x <5:
    print("Je kan je brood kopen maar verder niks")
else:
    print("Je heb meer dan genoeg om eten te halen maar je wilt liever burger king dus je gaat in de 2de pauze naar burger king")

print("Je bent op school in de les van python en je moet werk maken. ga je WERKEN of LUIEREN?")
choice4 = input().upper()

if choice4 == 'WERKEN':
	print("Je maakt netjes je werk af")
	
elif choice4 == 'LUIEREN':
	print("De docent wordt boos en gooit je de klas uit")     
else:
    print(choice4, " wasn't a valid choice")    