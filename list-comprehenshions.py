def run():
 # squeres = []
 #  for i in range(1,101):
 #    if i % 3 != 0:
 #      squeres.append(i**2)
 # squeres = [i**2 for i in range(1,101) if i % 3 != 0]
 # print(squeres)

  challenge = [i for i in range(1,100000)if i % 9 == 0 and i % 6 == 0 and i % 4 == 0]
  print(challenge)

if __name__=='__main__':
    run()



    