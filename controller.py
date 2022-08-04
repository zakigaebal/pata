class Controller:

    hp = 30
    exp = 0
    lv = 1

    def 밥먹기():

        global hp    #hp는 전역변수

        print('피카츄가 밥먹는다')  # hp 5증가
        hp += 5
        return hp


def 잠자기():
    global hp

    print('피카츄가 잠잔다')  # hp 10증가
    hp += 10
    return hp


def 놀기():
    global hp, exp, lv

    print('피카츄가 논다')  # hp 5감소, exp 7증가. hp감소(죽었나?). exp증가(레벨업체크)
    hp -= 5
    flag = hp>0  #살았나 죽었나
    if flag:
        exp +=7
        레벨체크()
    return flag


def 운동하기():
    global hp, exp, lv

    print('피카츄가 운동한다')  # hp 5감소, exp 7증가. hp감소(죽었나?). exp증가(레벨업체크)
    hp -= 15
    flag = hp > 0  # 살았나 죽었나
    if flag:
        exp += 15
        레벨체크()
    return flag

def 상태체크(): #그냥 읽어올때는 전역변수를 알아서 찾아가기 때문에, 따로 변수 지정 안해도 됌.
    print('Lv:', lv, 'HP:', hp, 'EXP:', exp)

def 레벨체크():
    global exp, lv
    if exp>=20:
        lv+=1
        exp -=20
        print('레벨업!!')