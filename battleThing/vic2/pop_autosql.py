import random
import pymysql

# 빅토에 등장하는 모든 계급.
vicpop = ['farmers', 'laborers', 'craftsmen', 'slaves', 'soldiers', 'artisans', 'breaucrats', 'clerks', 'clergymen',
          'officers', 'aristocrats', 'capitalists']
# 빅토에 등장하는 모든 사상과 관점.
ideology = ['conservative', 'reactionary', 'liberal', 'anarcho', 'socialist', 'communist', 'fascist']
trade = ['free', 'protect']
economy = ['laissez', 'interventionism', 'state', 'planned']
religion = ['atheism', 'secular', 'pluralism', 'moralism']
citizen = ['residency', 'limited', 'full']
military = ['jingo', 'pro', 'anti', 'pacifist']
'''
insert into party(party_name, ideology, trade, economy, religion, citizen, military)
values('anarcho-liberals', 'anarcho', 'free', 'laissez', 'pluralism', 'full', 'pro');

insert into party(party_name, ideology, trade, economy, religion, citizen, military)
values('reactionaries', 'reactionary', 'protect', 'interventionism', 'moralism', 'residency', 'jingo');

insert into party(party_name, ideology, trade, economy, religion, citizen, military)
values('communists', 'communist', 'free', 'laissez', 'pluralism', 'full', 'pro');

insert into party(party_name, ideology, trade, economy, religion, citizen, military)
values('socialists', 'socialist', 'protect', 'planned', 'secular', 'full', 'pro');

insert into party(party_name, ideology, trade, economy, religion, citizen, military)
values('fascists', 'fascist', 'protect', 'interventionism', 'moralism', 'residency', 'jingo');

insert into party(party_name, ideology, trade, economy, religion, citizen, military)
values('anarco-liberals', 'anarco-liberals', 'free', 'laissez', 'pluralism', 'full', 'pro');
'''

issues = trade + economy + religion + citizen + military  # 위 사상·관점을 하나로 묶은거. 사용할지 미지수
issuelist = [trade, economy, religion, citizen, military]  # issues와 마찬가지.

print(issuelist)

print(issues)

sql = pymysql.connect(
    host='localhost',
    user='root', password='123',
    db='vic', charset='utf8')
curs = sql.cursor(pymysql.cursors.DictCursor)

# pop = "insert into pop ('popclass', 'ideology', 'religion', 'population', 'primeissue', 'secissue') VALUES "

# 팝 무작위 생성. 미완성 상태.
for x in range(1):
    prime = random.choice(issuelist)
    # print('prime is: ', prime)
    secondList = []
    for issu in issuelist:
        if issu != prime:
            secondList.append(issu)
    # print('final: ', secondList)
    sec = random.choice(random.choice(secondList))
    prime = random.choice(prime)
    # print(sec, prime)
    execute = "insert into pop (popclass, ideology, religion, population, primeissue, secissue) " \
              "VALUES ('{0}','{1}','{2}',{3},'{4}','{5}');" \
        .format(random.choice(vicpop), random.choice(ideology), 'taoist', random.randint(100, 80000), prime, sec)
    print(execute)

partysql = "select * from party"
print('---popsupport---\n\n\n')

def loadparty():  # sql안에 있는 모든 정당을 불러온다.
    partylist = []  # 게임에 있는 모든 정당 목록.
    partycurs = sql.cursor()
    partycurs.execute(partysql)
    party_all = partycurs.fetchall()
    print(party_all)
    return party_all

# loadparty()

def popsupport():
    popsql = "select * from pop"    # 게임 내 모든 팝 불러오기
    # partycurs = sql.cursor()        # 모든 정당 불러오기
    party_list = loadparty()                     # 정당 불러오기.
    nonvoters = 0
    curs.execute(popsql)
    poplist = curs.fetchall()

    # 지지하는 정당 확인. 만약 지지하는 정당이 걸리면 일일히 당번을 바꾼다.
    # 비효율적일수도 있으나... 작업자의 파이선 사용법 문제로(..) sql에 있는 모든 팝 인구를 뽑아서 일일히 지지정당 지정을 함.
    # 지지정당의 선택방식은 크게 세가지로 나뉠 예정: 사상이 같은가, 관점이 같은가, 소속 지역의 정당 충성도는 얼마나 되는가.
    # 사상이 우선인가 관점이 우선인가는 정치인식도에 따라 갈리지만 현재는 시험중이니 고려없이 사상우선으로 한다.
    '''
    팝의 인원개념.
    팝의 기초개념은 빅1을 따른다. 팝 하나가 팝 전체의 의견을 대변한다. 투표에 한하여 일정 비율 쪼개지만 이는 제한적이다.
    장인계급은 현재로선 존재하지 않는다. 제작자가 잘 모름...
    관료는.... 이것도 좀 생각해봅시다.


    팝의 전반적인 지지정당 선택 알고리즘:
    1. 정당선택 이전에 팝의 이념과 관점 변동사항이 작동한다.
        현 이념은 뭔지, 정치관점은 뭔지 등을 현재 만족도, 정치인식, 투쟁성 등을 통해 계산한다.
        현 시점에서 이건 미구현상태다.
    2. 소속된 팝 지역의 정당 충성도를 확인한다. 충성도는 정확히는 정당이 아니라 이념별로 갈리게 된다.
        그 충성도 비중만큼의 %는 팝의 이념과 무관하게 무조건적으로 특정 이념의 정당을 지지하게 된다.
        만일 해당 이념의 정당이 없을 시 이 충성도는 무시되고 충성도는 매 턴 1%씩 자동 감소한다.
        역시 현 단계에서는 미구현 상태.
    3. 그 다음은 팝의 정치인식도를 확인한다.
        정치인식도에 따라 이념에 우선하여 투표할지, 관점에 우선하여 투표할지가 결정된다.
        이 결정은 확률이며, 인식도가 높을수록 이념을 우선한다.
	4.



    '''
    #

    for ppl in poplist:
        # partycurs.execute(partysql)
        print('-----')
        one_party = ppl['one_party']
        two_party = ppl['two_party']
        print(ppl['popclass'])
        if ppl['popclass'].lower() == 'slaves':
            nonvoters += int(ppl['population'])
            print('this is slave. pass')
            pass
        else:
            print('phase 2')
            for parti in party_list:
                party_issues = [parti[3], parti[4], parti[5], parti[6], parti[7]]
                party_ideology = parti[2]  # 당의 정치성향.
                print('partyname: ', parti[1], ' / people\'s idea:', ppl['ideology'])
                if ppl['ideology'] == party_ideology:  # 정당 사상이 맞으면 그다음 단계인 관점으로 간다.
                    if ppl["primeissue"] in party_issues:
                        two_party = one_party
                        one_party = parti[1]
                    elif ppl['secissue'] in party_issues:
                        two_party = one_party
                        one_party = parti[1]

            print('these', ppl['popclass'], 'supports', one_party)

popsupport()
