import random
for n in range(1):
  number = random.randint(1, 10001)
demande = int(input())
def devinez(demande, number):
  if demande < number:
    print("Ecrivez un nombre plus grand")
  else:
    print("Ecrivez un nombre plus petit")
while demande!=number:
    devinez(demande, number)
    demande = int(input())
print("vous avez deviné le nombre!")