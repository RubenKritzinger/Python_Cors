famous_people = ['adolf hitler' , 'abraham Lincoln', 'rocky balboa' ]
print(famous_people[0].title())
print(famous_people[1].title())
print(famous_people[2].title())

print(f"\n\nAbraham lincoln sais you are to afraid to join us for dinner  {famous_people[0].title()}.")
print(f"adolf whants to show you he is the stronger rais and you wont show up {famous_people[1].title()}.")
print(f"abraham lincoln whants toe invite you to beat up adolf Hitlor {famous_people[2].title()}.")

#3-5

uninvited_guest1 = famous_people.pop(2)
print(f"\n\n{uninvited_guest1.title()} has been uninvited.")

famous_people.append ('bruce lee')
print(famous_people)

#3-6
famous_people.insert(0,'Ruben kritzinger')

famous_people.insert(2,'vusie bandi')

famous_people.append('chuck norris')
print(famous_people)

print(f"\n\nYou are invited to join our dinner party {famous_people[0].title()}.")
print(f"You are invited to join our dinner party {famous_people[1].title()}.")
print(f"You are invited to join our dinner party {famous_people[2].title()}.")
print(f"You are invited to join our dinner party {famous_people[3].title()}.")
print(f"You are invited to join our dinner party {famous_people[4].title()}.")
print(f"You are invited to join our dinner party {famous_people[5].title()}.")

#3-7

message = "\nYou are only allowed to invite two people for dinner.\n"
print(message)

print(f"sorry {famous_people[-1].title()}, you have been uninvited")
famous_people.pop()

print(f"sorry {famous_people[-1].title()}, you have been uninvited")
famous_people.pop()

print(f"sorry {famous_people[-1].title()}, you have been uninvited")
famous_people.pop()

print(f"sorry {famous_people[-1].title()}, you have been uninvited")
famous_people.pop()

print(f"\n{famous_people}")

famous_people.pop()
famous_people.pop()

print(f"\n{famous_people}")
