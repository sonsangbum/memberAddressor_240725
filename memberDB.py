import pymysql

conn = pymysql.connect(host='localhost',user='root',password='12345', db='memberdb')
#python program과 mysql간의 connection 생성

while True :
    print("*********************회원관리 프로그램 ********************")
    print("(1)회원가입")
    print("(2)회원정보수정")
    print("(3)회원탈퇴")
    print("(4)회원전체목록조회")
    print("(5)프로그램 종료")
    print("*********************************************************")

    userNum=input("위 메뉴 중 한 가지를 선택하세요(1~5)  :")

    if userNum == "1" :
        print("가입하시려면 회원정보를 입력하세요")
        memberid=input("* 회원아이디를 입력하세요 :")
        membername=input("* 회원이름을 입력하세요 :")
        memberemail=input("* 이메일을 입력하세요 :")
        memberage=input("* 나이를 입력하세요 :")

        sql=F"INSERT INTO membertbl(memberid,membername,memberemail,memberage) VALUES('{memberid}','{membername}','{memberemail}','{memberage}')"

        cur=conn.cursor()  #cursor 생성
        success = cur.execute(sql)  #sql문 실행 -> 반환되는 값이 1이면 '성공'

        if success == 1:
            print("축하합니다! 회원가입 성공하셨습니다.")
        else:
            print("회원가입 실패입니다.")

        cur.close()
        conn.commit()

    elif userNum == "2" :
        memberid=input("* 회원정보를 수정할 아이디를 입력하세요 :")
        membername=input("* 수정할 회원이름을 입력하세요 :")
        memberemail=input("* 수정할 이메일을 입력하세요 :")
        memberage=input("* 수정할 나이를 입력하세요 :")

        sql=f"UPDATE membertbl set membername='{membername}',memberemail='{memberemail}',memberage='{memberage}' where memberid='{memberid}'"

        cur=conn.cursor()  #cursor 생성
        success = cur.execute(sql)  #sql문 실행 -> 반환되는 값이 1이면 '성공'

        if success == 1:
            print("회원정보수정 성공하셨습니다.")
        else:
            print("회원정보수정 실패입니다.")

        cur.close()
        conn.commit()


    elif userNum == "3" :
        memberid=input("* 탈퇴활 회원ID를 입력하세요  :")

        sql=f"DELETE FROM membertbl WHERE memberid='{memberid}'"

        cur=conn.cursor()  #cursor 생성
        success = cur.execute(sql)  #sql문 실행 -> 반환되는 값이 1이면 '성공'

        if success == 1:
            print("회원 탈퇴 성공하셨습니다.")
        else:
            print("회원 탈퇴 실패했습니다.")

        cur.close()
        conn.commit()

    elif userNum == "4" :  #회원목록보기
        sql=f"SELECT * FROM membertbl"

        cur=conn.cursor()  #cursor 생성
        success = cur.execute(sql)  #sql문 실행 -> 반환되는 값이 1이면 '성공'
        allMemberList=cur.fetchall()  # SELECT 문의 결과를 반환 > 튜플 # 튜플의 특징. 내용수정불가

        print("***************** 전체회원 리스트 *****************")
        for member in allMemberList:
            print(member[0], end=" / ")
            print(member[1], end=" / ")
            print(member[2], end=" / ")
            print(member[3], end=" / ")
            print(member[4])

        cur.close()
        conn.commit()

    elif userNum =="5":
        print("회원관리 프로그램을 종료합니다")
        conn.close()
        break

    else:
        print("존재하지 않는 메뉴번호입니다. 다시 입력해주세요!")