import sqlite3

def register(username, password):
    con = sqlite3.connect('User.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM UserData WHERE username = ?;", (username,))
    if cursor.fetchone():
        print("이미 존재하는 ID입니다.")
        con.commit()
        con.close()
        return False
    cursor.execute("INSERT INTO UserData (username, password) VALUES (?, ?);", (username, password))
    print("가입이 완료되었습니다.")
    con.commit()
    con.close()
    return True

def authorization(username, password):
    con = sqlite3.connect('User.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM UserData WHERE username = ? AND password = ?;", (username, password))
    row = cursor.fetchone()
    if row:
        con.commit()
        con.close()
        print("로그인 성공")
        return (row[0], True)
    print("로그인 실패")
    con.commit()
    con.close()
    return False

def search_data(IndexID):
    con = sqlite3.connect('User.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM UserInfo WHERE "Index" = ?', (IndexID,))
    data = cursor.fetchall()
    return data

def UserInfoAdd(IndexID, DataName, Field):
    con = sqlite3.connect('User.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO UserInfo ("Index", DataName, Field) VALUES (?, ?, ?);', (IndexID, DataName, Field))
    con.commit()
    con.close()
    print("데이터 추가 완료")
    return True

Login = 0
IndexID = 0
while True:
    if Login:
        print("1. 데이터조회")
        print("2. 데이터추가")
        print("3. 종료")
        menu = int(input("메뉴를 선택하세요: "))

        if menu == 1:
            # 데이터 조회
            for turple_data in search_data(IndexID):
                _, DataName, Field = turple_data
                print(f"{DataName} : {Field}")
            continue
        if menu == 2:
            # 데이터 추가
            DataName = input("무슨 항목을 추가하실건가요? : ")
            Field = input("무슨 내용을 추가하실건가요? : ")
            UserInfoAdd(IndexID, DataName, Field)
            continue
        if menu == 3:
            break
    else:
        print("1. 로그인")
        print("2. 회원가입")
        print("3. 종료")
        menu = int(input("메뉴를 선택하세요: "))
    
        if menu == 1:
            username = input("username을 입력해주세요 : ")
            password = input("password를 입력해주세요 : ")
            IndexID, Login = authorization(username, password)
            continue
        if menu == 2:
            # 회원가입 정보를 SQL에 추가
            username = input("username을 입력해주세요 : ")
            password = input("password를 입력해주세요 : ")
            register(username, password)
            continue
        if menu == 3:
            break
