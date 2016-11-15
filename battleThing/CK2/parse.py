from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import wikipedia
import time

newlistmen = urlopen('https://en.wikipedia.org/wiki/Category:Korean_masculine_given_names')
newlistwomen = urlopen('https://en.wikipedia.org/wiki/Category:Korean_feminine_given_names')

listsoup = BeautifulSoup(newlistwomen, 'html.parser')
newlistsoup = [
    ul('li')[0].txt for table in listsoup.find_all('div', 'mw-category-group') for ul in table('ul')[0:]
]
print(newlistsoup)
print('[[[[[')

html = urlopen(
    'https://en.wikipedia.org/wiki/List_of_members_of_the_National_Assembly_(South_Korea),_2016%E2%80%93present')
# print(html.read())

# sample = '''
# background-color:#DDDDDD"></td>\n<td><a href="/wiki/Jongno_District" title="Jongno District">Jongno</a></td>\n<td><a href="/wiki/Chung_Sye-kyun" title="Chung Sye-kyun">Chung Sye-kyun</a></td>\n<td><a href="/wiki/Independent_politician" title="Independent politician">Independent</a></td>\n<td>Left MPK as being elected a speaker.</td>\n</tr>\n<tr>\n<td scope="row" style="background-color:#004EA2"></td>\n<td><a href="/wiki/Jung_District,_Seoul" title="Jung District, Seoul">Jung</a>\xe2\x80\x93<a href="/wiki/Seongdong_District" title="Seongdong District">Seongdong</a> A</td>\n<td><a href="/wiki/Hong_Ihk-pyo" title="Hong Ihk-pyo">Hong Ihk-pyo</a></td>\n<td>Minjoo</td>\n<td></td>\n</tr>\n<tr>\n<td scope="row" style="background-color:#C8161E"></td>\n<td><a href="/wiki/Jung_District,_Seoul" title="Jung District, Seoul">Jung</a>\xe2\x80\x93<a href="/wiki/Seongdong_District" title="Seongdong District">Seongdong</a> B</td>\n<td><a href="/wiki/Ji_Sang-wook" title="Ji Sang-wook">Ji Sang-wook</a></td>\n<td><a href="/wiki/Saenuri_Party" title="Saenuri Party">Saenuri</a></td>\n<td></td>\n</tr>\n<tr>\n<td scope="row" style="background-color:#004EA2"></td>\n<td><a href="/wiki/Yongsan_District" title="Yongsan District">Yongsan</a></td>\n<td><a href="/wiki/Chin_Young" title="Chin Young">Chin Young</a></td>\n<td>Minjoo</td>\n<td></td>\n</tr>\n<tr>\n<td sco
# '''



soup = BeautifulSoup(html, 'html.parser')
names = [tr('td')[2].text for table in soup.find_all('table', 'sortable') for tr in table('tr')[1:]]
# print(names)

print()
lastname = re.compile(r'[A-Z][a-z]+ ')
firstname = re.compile(r'\s\w+-?\w+')
yay = firstname.findall(str(names))
nay = lastname.findall(str(names))

print(yay)

c = []
for a in yay:
    b = a.replace(' ', '')
    c.append(b)
    # print(b)
    # if truth == 1:
    #     c.append(b)
    #     truth += 1
    # for ab in c:
    #     print('ab=', ab, '/ b=', b)
    #     if ab == b:
    #         break
    #     else:
    #         c.append(b)
ccc = set(c)
for i in ccc:
    print(i, end=' ')



# print(soup)
# print(type(soup))
# print(type(str(soup)))
# sen = soup.find_all("table", {"class": "wikitable sortable jquery-tablesorter"})
# sen = soup.find_all("table", class_='wikitable sortable jquery-tablesorter')
# senate = re.compile(r'\w+ \w+</a></td>\n<td>')
# print(senate.findall(str('Chin Young')))
# print(senate.findall(str(soup)))
# print(str(html.read()).encode('ascii'))
# print('---------')
# print(str(soup))

# print(sen)

alist = '''
Constituency	Member	Party	Notes
Jongno	Chung Sye-kyun	Independent	Left MPK as being elected a speaker.
Jung–Seongdong A	Hong Ihk-pyo	Minjoo
Jung–Seongdong B	Ji Sang-wook	Saenuri
Yongsan	Chin Young	Minjoo
Gwangjin A	Jeon Hye-sook	Minjoo
Gwangjin B	Choo Mi-ae	Minjoo
Dongdaemun A	Ahn Gyu-baek	Minjoo
Dongdaemun B	Min Byung-doo	Minjoo
Jungnang A	Seo Young-kyo	Minjoo
Jungnang B	Park Hong-keun	Minjoo
Seongbuk A	You Seung-hee	Minjoo
Seongbuk B	Ki Dong-min	Minjoo
Gangbuk A	Cheong Yang-seog	Saenuri
Gangbuk B	Park Yong-jin	Minjoo
Dobong A	In Jae-keun	Minjoo
Dobong B	Kim Seon-dong	Saenuri
Nowon A	Koh Yong-jin	Minjoo
Nowon B	Woo Won-shik	Minjoo
Nowon C	Ahn Cheol-soo	People's	Co-chairman of the People's Party (2016–present)
Eunpyeong A	Park Joo-min	Minjoo
Eunpyeong B	Kang Byeong-won	Minjoo
Seodaemun A	Woo Sang-ho	Minjoo
Seodaemun B	Kim Yeong-ho	Minjoo
Mapo A	Noh Woong-rae	Minjoo
Mapo B	Sohn Hye-won	Minjoo
Yangcheon A	Hwang Hee	Minjoo
Yangcheon B	Kim Yong-tae	Saenuri
Gangseo A	Geum Tae-seop	Minjoo
Gangseo B	Kim Sung-tae	Saenuri
Gangseo C	Han Jeoung-ae	Minjoo
Guro A	Lee In-young	Minjoo
Guro B	Park Young-sun	Minjoo
Geumcheon	Lee Hoon	Minjoo
Yeongdeungpo A	Kim Young-joo	Minjoo
Yeongdeungpo B	Shin Kyoung-min	Minjoo
Dongjak A	Kim Byeong-gi	Minjoo
Dongjak B	Na Kyung-won	Saenuri
Gwanak A	Kim Sung-shik	People's
Gwanak B	Oh Shin-hwan	Saenuri
Seocho A	Lee Hye-hoon	Saenuri
Seocho B	Park Seong-joong	Saenuri
Gangnam A	Lee Jong-gu	Saenuri
Gangnam B	Jun Hyeon-hee	Minjoo
Gangnam C	Lee Eun-jae	Saenuri
Songpa A	Park In-sook	Saenuri
Songpa B	Choi Myeong-gil	Minjoo
Songpa C	Nam In-soon	Minjoo
Gangdong A	Jin Sun-mee	Minjoo
Gangdong B	Shim Jae-kwon	Minjoo
Busan[edit]
Constituency	Member	Party	Notes
Jung–Yeongdo	Kim Moo-sung	Saenuri
Seo–Dong	Yoo Ki-june	Saenuri
Busanjin A	Kim Young-choon	Minjoo
Busanjin B	Lee Hun-seung	Saenuri
Dongnae	Lee Jin-bok	Saenuri
Nam A	Kim Jung-hoon	Saenuri
Nam B	Park Jae-ho	Minjoo
Buk–Gangseo A	Chun Jae-soo	Minjoo
Buk–Gangseo B	Kim Do-eup	Saenuri
Haeundae A	Ha Tae-keung	Saenuri
Haeundae B	Bae Duk-kwang	Saenuri
Saha A	Choi In-ho	Minjoo
Saha B	Cho Kyoung-tae	Saenuri
Geumjeong	Kim Se-yeon	Saenuri
Yeonje	Kim Hae-young	Minjoo
Suyeong	Yoo Jae-jung	Saenuri
Sasang	Chang Jae-won	Independent Saenuri	Rejoined the Saenuri Party.
Gijang	Yoon Sang-jik	Saenuri
Daegu[edit]
Constituency	Member	Party	Notes
Jung–Nam	Kwak Sang-do	Saenuri
Dong A	Chong Jong-sup	Saenuri
Dong B	Yoo Seong-min	Independent Saenuri	Rejoined Saenuri Party.
Seo	Kim Sang-hoon	Saenuri
Buk A	Jeong Tae-ok	Saenuri
Buk B	Hong Eui-rak	Independent
Suseong A	Kim Boo-kyum	Minjoo
Suseong B	Joo Ho-young	Independent Saenuri	Rejoined Saenuri Party.
Dalseo A	Kwak Dae-hoon	Saenuri
Dalseo B	Yoon Jae-ok	Saenuri
Dalseo C	Cho Won-jin	Saenuri
Dalseong	Choo Kyung-ho	Saenuri
Incheon[edit]
Constituency	Member	Party	Notes
Jung–Dong–Ganghwa–Ongjin	Ahn Sang-soo	Independent Saenuri	Rejoined Saenuri Party.
Nam A	Hong Il-pyo	Saenuri
Nam B	Yoon Sang-hyun	Independent Saenuri	Rejoined Saenuri Party.
Yeonsu A	Park Chan-dae	Minjoo
Yeonsu B	Min Kyung-wook	Saenuri
Namdong A	Park Nam-choon	Minjoo
Namdong B	Youn Kwan-suk	Minjoo
Bupyeong A	Jung Yu-seok	Saenuri
Bupyeong B	Hong Young-pyo	Minjoo
Gyeyang A	Yu Dong-su	Minjoo
Gyeyang B	Song Young-gil	Minjoo
Seo A	Lee Hag-jae	Saenuri
Seo B	Shin Dong-keun	Minjoo
Gwangju[edit]
Constituency	Member	Party	Notes
Dong–Nam A	Chang Byoung-wan	People's
Dong–Nam B	Park Joo-sun	People's
Seo A	Song Gi-seok	People's
Seo B	Chun Jung-bae	People's	Co-chairman of the People's Party (2016–present)
Buk A	Kim Gyeong-jin	People's
Buk B	Choi Gyeong-hwan	People's
Gwangsan A	Kim Dong-cheol	People's
Gwangsan B	Kwon Eun-hee	People's
Daejeon[edit]
Constituency	Member	Party	Notes
Dong	Lee Jang-woo	Saenuri
Jung	Lee Eun-gwon	Saenuri
Seo A	Park Byeong-seog	Minjoo
Seo B	Park Beom-kye	Minjoo
Yuseong A	Jo Seung-rae	Minjoo
Yuseong B	Lee Sang-min	Minjoo
Daedeok	Jeong Yong-ki	Saenuri
Ulsan[edit]
Constituency	Member	Party	Notes
Jung	Jeong Kab-yoon	Saenuri
Nam A	Lee Chae-ik	Saenuri
Nam B	Bak Maeng-woo	Saenuri
Dong	Kim Jong-hoon	Independent
Buk	Yoon Jong-oh	Independent
Ulju	Kang Ghil-boo	Independent Saenuri	Rejoined Saenuri Party.
Sejong[edit]
Constituency	Member	Party	Notes
Sejong	Lee Hae-chan	Independent
Gyeonggi[edit]
Constituency	Member	Party	Notes
Suwon A	Lee Chan-yeol	Minjoo
Suwon B	Baek Hye-ryun	Minjoo
Suwon C	Kim Yeong-jin	Minjoo
Suwon D	Park Kwang-on	Minjoo
Suwon E	Kim Jin-pyo	Minjoo
Seongnam Sujeong-gu	Kim Tae-nyeon	Minjoo
Seongnam Jungwon-gu	Shin Sang-jin	Saenuri
Seongnam Bundang-gu A	Kim Byung-gwan	Minjoo
Seongnam Bundang-gu B	Kim Byung-uk	Minjoo
Uijeongbu A	Moon Hee-sang	Minjoo
Uijeongbu B	Hong Mun-jong	Saenuri
Anyang Manan-gu	Lee Jong-kul	Minjoo
Anyang Dongan-gu A	Lee Suk-hyun	Minjoo
Anyang Dongan-gu B	Shim Jae-chul	Saenuri
Bucheon Wonmi-gu A	Kim Gyeong-hyeop	Minjoo
Bucheon Wonmi-gu B	Sul Hoon	Minjoo
Bucheon Sosa-gu	Kim Sang-hee	Minjoo
Bucheon Ojeong-gu	Won Hye-young	Minjoo
Gwangmyeong A	Baek Jae-hyun	Minjoo
Gwangmyeong B	Lee Un-ju	Minjoo
Pyeongtaek A	Won Yoo-chul	Saenuri	Saenuri interim chairman (2016–present)
Pyeongtaek B	Yoo Ui-dong	Saenuri
Ansan Sangnok-gu A	Jeon Hae-cheol	Minjoo
Ansan Sangnok-gu B	Kim Cheol-min	Minjoo
Ansan Danwon-gu A	Kim Myung-yeon	Saenuri
Ansan Danwon-gu B	Park Sun-ja	Saenuri
Goyang A	Sim Sang-jung	Justice	Justice Party chairwoman (2015–present)
Goyang B	Jung Jae-ho	Minjoo
Goyang C	Yoo Eun-hae	Minjoo
Goyang D	Kim Hyun-mee	Minjoo
Namyangju A	Cho Eung-chun	Minjoo
Namyangju B	Kim Han-jeong	Minjoo
Namyangju C	Joo Kwang-deok	Saenuri
Siheung A	Ham Jin-kyu	Saenuri
Siheung B	Cho Jeong-sik	Minjoo
Gunpo A	Kim Jeong-woo	Minjoo
Gunpo B	Lee Hak-yeong	Minjoo
Yongin A	Lee Woo-hyun	Saenuri
Yongin B	Kim Min-gi	Minjoo
Yongin C	Han Sun-kyo	Saenuri
Yongin D	Pyo Chang-won	Minjoo
Paju A	Yoon Hu-duk	Minjoo
Paju B	Park Jeong	Minjoo
Gimpo A	Kim Doo-kwan	Minjoo
Gimpo B	Hong Chul-ho	Saenuri
Hwaseong A	Seo Chung-won	Saenuri
Hwaseong B	Lee Won-uk	Minjoo
Hwaseong C	Kwon Chil-seung	Minjoo
Gwangju A	So Byeong-hun	Minjoo
Gwangju B	Im Jong-seong	Minjoo
Guri	Yun Ho-jung	Minjoo
Osan	An Min-suk	Minjoo
Hanam	Lee Hyun-jae	Saenuri
Icheon	Song Seok-jun	Saenuri
Anseong	Kim Hak-yong	Saenuri
Yangju	Chung Seong-ho	Minjoo
Uiwang–Gwacheon	Sim Chang-hyeon	Minjoo
Dongducheon–Yeoncheon	Kim Seong-won	Saenuri
Pocheon–Gapyeong	Kim Young-woo	Saenuri
Yeoju–Yangpyeong	Choung Byoung-gug	Saenuri
Gangwon[edit]
Constituency	Member	Party	Notes
Chuncheon	Kim Jin-tae	Saenuri
Wonju A	Kim Ki-sun	Saenuri
Wonju B	Song Ki-hun	Minjoo
Gangneung	Kweon Seong-dong	Saenuri
Donghae–Samcheok	Lee Chul-gyu	Independent Saenuri	Rejoined Saenuri Party.
Taebaek–Hoengseong–Yeongwol–Pyeongchang–Jeongseon	Yeom Dong-yeol	Saenuri
Sokcho–Goseong–Yangyang	Lee Yang-su	Saenuri
Hongcheon–Cheorwon–Hwacheon–Yanggu–Inje	Hwang Young-cheul	Saenuri
North Chungcheong[edit]
Constituency	Member	Party	Notes
Cheongju Sangdang-gu	Chung Woo-taik	Saenuri
Cheongju Seowon-gu	Oh Jae-sae	Minjoo
Cheongju Heungdeok-gu	Do Jong-hwan	Minjoo
Cheongju Cheongwon-gu	Byun Jae-ill	Minjoo
Chungju	Lee Jong-bae	Saenuri
Jecheon–Danyang	Gwon Seok-chang	Saenuri
Boeun–Okcheon–Yeongdong–Goesan	Park Deok-heum	Saenuri
Jeungpyeong–Jincheon–Eumseong	Kyung Dae-soo	Saenuri
South Chungcheong[edit]
Constituency	Member	Party	Notes
Cheonan A	Park Chan-woo	Saenuri
Cheonan B	Park Wan-ju	Minjoo
Cheonan C	Yang Seoung-jo	Minjoo
Gongju–Buyeo–Cheongyang	Chung Jin-suk	Saenuri
Boryeong–Seocheon	Kim Tae-heum	Saenuri
Asan A	Lee Myoung-soo	Saenuri
Asan B	Kang Hun-sik	Minjoo
Seosan–Taean	Sung Il-jong	Saenuri
Nonsan–Gyeryong–Geumsan	Kim Jong-min	Minjoo
Dangjin	Eo Ki-kyu	Minjoo
Hongseong–Yesan	Hong Moon-pyo	Saenuri
North Jeolla[edit]
Constituency	Member	Party	Notes
Jeonju A	Kim Gwang-su	People's
Jeonju B	Chung Woon-chun	Saenuri
Jeonju C	Chung Dong-young	People's
Gunsan	Kim Kwan-young	People's
Iksan A	Lee Choon-suak	Minjoo
Iksan B	Cho Bae-sook	People's
Jeongeup–Gochang	You Sung-yop	People's
Namwon–Imsil–Sunchang	Lee Yong-ho	People's
Gimje–Buan	Kim Jong-hee	People's
Wanju–Jinan–Muju–Jangsu	An Ho-young	Minjoo
South Jeolla[edit]
Constituency	Member	Party	Notes
Mokpo	Park Jie-won	People's
Yeosu A	Lee Yong-ju	People's
Yeosu B	Joo Seung-yong	People's
Suncheon	Lee Jung-hyun	Saenuri
Naju–Hwasun	Son Kum-ju	People's
Gwangyang–Gokseong–Gurye	Jeong In-hwa	People's
Damyang–Hampyeong–Yeonggwang–Jangseong	Lee Kai-ho	Minjoo
Goheung–Boseong–Jangheung–Gangjin	Hwang Ju-hong	People's
Haenam–Wando–Jindo	Yoon Young-il	People's
Yeongam–Muan–Sinan	Park Jun-yeong	People's
North Gyeongsang[edit]
Constituency	Member	Party	Notes
Pohang Buk-gu	Kim Jeong-jae	Saenuri
Pohang Nam-gu–Ulleung	Park Myung-jae	Saenuri
Gyeongju	Kim Seok-ki	Saenuri
Gimcheon	Lee Cheol-uoo	Saenuri
Andong	Kim Kwang-lim	Saenuri
Gyeongsan	Choi Kyoung-hwan	Saenuri
Gumi A	Baek Seung-joo	Saenuri
Gumi B	Chang Seok-chun	Saenuri
Yeongju–Mungyeong–Yecheon	Choi Gyo-il	Saenuri
Yeongcheon–Cheongdo	Lee Man-hee	Saenuri
Sangju–Gunwi–Uiseong–Cheongsong	Kim Jong-tae	Saenuri
Yeongyang–Yeongdeok–Bonghwa–Uljin	Kang Seok-ho	Saenuri
Goryeong–Seongju–Chilgok	Yi Wan-young	Saenuri
South Gyeongsang[edit]
Constituency	Member	Party	Notes
Changwon Uichang-gu	Park Wan-su	Saenuri
Changwon Seongsan-gu	Roh Hoe-chan	Justice
Changwon Masanhappo-gu	Lee Ju-young	Saenuri
Changwon Masanhoewon-gu	Yoon Han-hong	Saenuri
Changwon Jinhae-gu	Kim Sung-chan	Saenuri
Jinju A	Park Dae-chul	Saenuri
Jinju B	Kim Jae-kyung	Saenuri
Tongyeong–Goseong	Lee Gun-hyeon	Saenuri
Sacheon–Namhae–Hadong	Yeo Sang-gyu	Saenuri
Gimhae A	Min Hong-chul	Minjoo
Gimhae B	Kim Kyung-soo	Minjoo
Miryang–Uiryeong–Haman–Changnyeong	Um Yong-su	Saenuri
Geoje	Kim Han-pyo	Saenuri
Yangsan A	Yoon Young-suk	Saenuri
Yangsan B	Seo Hyung-soo	Minjoo
Sancheong–Hamyang–Geochang–Hapcheon	Kang Seok-jin	Saenuri
Jeju[edit]
Constituency	Member	Party	Notes
Jeju A	Kang Chang-il	Minjoo
Jeju B	Oh Yeong-hoon	Minjoo
Seogwipo	Wi Seong-gon	Minjoo
'''
sample = """
Jeju[edit]
Yangcheon A	Hwang Hee	Minjoo
Constituency	Member	Party	Notes
Jeju A	Kang Chang-il	Minjoo
Jeju B	Oh Yeong-hoon   Minjoo
Seogwipo	Wi Seong-gon	Minjoo
"""

senate = re.compile(r'\w+-\w+\s+Minjoo|Saenuri|People|Justice')

# print(senate.findall(sample))
# names = [ tr('td')[2].text for table in soup.find_all('table', 'sortable') for tr in table('tr')[1:] ]
# print(senate.findall(alist))
# print(senate.findall("Jeju B	Oh Yeong-hoon   Minjoo"))
# lines = ' My_NUMBER                 =dd'
# print('==')
# num = lines.split('=')[0].strip()
# print("55")
# print(num)
