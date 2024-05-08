# CS-SCH
CS-SCH SQL해석
```SQL
SELECT * FROM UserData WHERE username = ? AND password = ?
```
SELECT *은 전체를 선택하는데
UserData 테이블에서
WHERE(조건에 맞는)
Username이 ?이면서, password가 ?인 것.

---
```SQL
SELECT * FROM UserInfo WHERE "Index" = ?
```
Index는 SQL에 예약어이기 떄문에 ""를 붙여야 함.

---
```SQL
INSERT INTO UserInfo ("Index", DataName, Field) VALUES (?, ?, ?)
```
INSERT 삽입하는데 INTO어디에? UserInfo에
(row 명칭) Values => 값을 (각각)으로 저장.

ex) INSERT INTO UserInfo ("Index", DataName, Field) VALUES (2, "이름", "난어디여긴누구?")
![image](https://github.com/hsx0306/CS-SCH/assets/70040924/a041629e-ad21-4456-aa55-5734b04da8b4)

---
# 추가사항
DELETE SQL 코드에서는 제공하지 않지만,
```SQL
DELETE FROM UserInfo WHERE "Index" = 1
```
이럴 경우 Index가 1인 조건이 사라지는데 이런식의 조건을 다중하여
```SQL
DELETE FROM UserInfo WHERE "INDEX" = 1 AND "Dataname" = "이름"
```
이런식으로 할 수 있다.

---
# 추가사항2
SQL을 정렬하여 끄집어 오고 싶을 떄 => 무엇을 하라고 시키는 것 ORDER BY
```SQL
SELECT * FROM UserData ORDER BY "Index", ASC;
```
이런식으로 UserData테이블을 선택하고 Index로 정렬해달라고 하면 된다.
ASC 와 내림차순(큰 값에서 작은 값으로) DESC 가 있음.

"Index"대신 조건이 오면 조건을 비교해서 정렬을 함.


