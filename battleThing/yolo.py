import random

list = []
for i in range(20):
  insert = 'insert into rent(car_id, cus_id, rent_sdate, rent_edate, rent_ddate) values("'
  carId = random.randint(1, 50)
  cusId = ", 'dkdlel" + str(random.randint(1, 51)) + "', "
  list.append(carId)
  for j in range(len(list)-1):
    if len(list) == 1:
      break
    if list[j] == carId:
      continue
  sday = random.randint(1, 30)
  eday = random.randint(1, 30)
  dday = eday + random.randint(0, 2)
  smon = random.randint(1,1) + 8
  emon = random.randint(1,1) + 8
  dmon = random.randint(1,1) + 8
  if smon > emon or dmon > emon or smon > dmon:
    continue
  if sday >= dday:
    continue
  elif sday >= dday:
    continue
  sdate = "'2016-" + str(smon) + "-" + str(sday) + "', "
  edate = "'2016-" + str(emon) + "-" + str(eday) + "', "
  ddate = "'2016-" + str(dmon) + "-" + str(dday) + "');"
  print(insert + str(carId) + cusId + sdate + edate + ddate)
