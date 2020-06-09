def counter_item(items):
  result = {}
  list_ = sorted(list(dict.fromkeys(items)))
  for j in range(len(list_)):
      counter = 0
      for i in range(len(items)):
          if list_[j] == items[i]:
              counter += 1
          else:
              continue
          result[list_[j]] = counter
  return result

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = {}
for i in range(len(fruits)):
    fruit_price[fruits[i]] = prices[i]

def total_price(dcounter,fprice):
  total = 0
  for i in dcounter:
      total += dcounter[i] * fprice[i]
  print(total)

total_price(counter_item(chart),fruit_price)