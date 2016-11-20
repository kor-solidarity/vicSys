# this is about total voting sys.
# basically follows victoria 2 rule, but POPs' voting pattern is based on vic1(i guess)
# right now there's technically nothing done. and all is just for tests.
# 제대로 읽히는지 시험 겸 확인용.


# 각 정당의 기본설정. 만약 불러온 값에 이게 없을 시

import pymysql

conn = pymysql.connect(
            host='localhost',
            user='root', password='123',
            db='vic', charset='utf8')
curs = conn.cursor()  # pymysql.cursors.DictCursor)

sql = 'select * from party'
curs.execute(sql)
rows = curs.fetchall()

# rows.count()
for a in rows:
    print(a)



print('----------------------')



#     .connect(
#     database='vic',
#     user='root',
#     password='123',
#
# )





