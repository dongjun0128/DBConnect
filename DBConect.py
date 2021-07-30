import re
import CUBRIDdb

#DB연결 
conn = CUBRIDdb.connect('CUBRID:13.124.197.219:30000:IROSDB:::','soa','soa')

#cursor는 fetch동작 관리, cur은 객체
cur = conn.cursor()

#query문 실행
cur.execute("select rdnmadr from tn_pubr_public_prhsmk_zn_api where rdnmadr  like '%''%' limit 10;")

#한개의 row만 가져오기
row = cur.fetchone()

#수정된 문자열을 저장할 객체 생성
modifyList=[]

while row:
    modifyList.append(re.sub("\'","","".join(row)))
    row = cur.fetchone()

#한 줄 씩 출력
for list in modifyList:
    print(list)


#conn.commit()