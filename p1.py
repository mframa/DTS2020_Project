# nama file p1.py
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded
# Isikan juga priority file

# untuk resubmisi, grader hanya akan mengambil priority yang paling besar
# jadi kalau anda ingin merevisi kode anda:
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0

priority = 0


#netacad email cth: 'abcd@gmail.com'
email='fajar.rama20@gmail.com'

# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI
#Graded

# Manual, filter, list comprehension
def letter_catalog(items,letter='A'):
  result = []
  if len(items) > 0:
      for i in range(len(items)):
          if items[i][0:1].upper() == letter.upper():
              result.append(items[i])
          else:
              continue

  else:
      return result
  return result

#Graded

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

fruit_price = {}
for i in range(len(fruits)):
    fruit_price[fruits[i]] = prices[i]

def total_price(dcounter,fprice):
  total = 0
  for i in dcounter:
      total += dcounter[i] * fprice[i]
  return total

#Graded

def discounted_price(total,discount,minprice=100):
  if total >= minprice:
      result = total - (total * (discount / 100))
      return result
  else:
      return total

#Graded

def print_summary(items,fprice):
  charts = counter_item(items)
  total_prices = total_price(charts,fprice)
  disc_price = discounted_price(total_prices, 10, minprice=100)
  for i in charts:
      item_total = 0
      item_total = charts[i] * fprice[i]
      print("{} {} : {}".format(charts[i], i, item_total))
  print("total : {}".format(total_prices))
  print("discount price : {}".format(disc_price))

