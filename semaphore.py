# Inside of a Semaphore
import time
from multiprocessing import Process

prod_cons = False
count = 0
item = 1
times = 0


def factory(raw_item):

  global item

  time.sleep(1)
  item = raw_item * 2
  print(f"\nProducer Item: {item} & Time: {time.ctime()}")




def on_producer(prod_cons):

  global item

  if prod_cons == True:
    factory(item)





def off_producer(prod_cons, count):

  global times

  if times == 4:
    exit

  else:
    if prod_cons == False:
      count = count + 1
      print(f"Producer Count: {count} & Time: {time.ctime()}")
      consumer(count)



def relax():
  time.sleep(1)
  print(f"\nConsumer Item: {item} & Time: {time.ctime()}")




def consumer(count):

  global item
  global times

  prod_cons = True
  p1 = Process(target=relax)
  p1.start()

  p2 = Process(target=on_producer(prod_cons))
  p2.start()

  p1.join()
  p2.join()

  # time.sleep(2)

  count = count - 1
  print(f"Consumer Count: {count} & Time: {time.ctime()}\n")
  times = times + 1

  prod_cons = False
  off_producer(prod_cons, count)



def main():
  print(f"Producer Item: {item} & Time: {time.ctime()}\n")
  off_producer(prod_cons, count)
  print(f"Producer Item: {item} & Time: {time.ctime()}\n")


main()
