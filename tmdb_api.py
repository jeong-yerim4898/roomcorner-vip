#-*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt_back.settings')

import django
django.setup()

import requests

from naver_movie.models import Genre, Movie

import json
from decouple import config

apikey = config('TMDB_SECRET_KEY')
lang = 'ko-KR'
page = 1
region = 'KR'

genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={apikey}&language={lang}'
genre_response = requests.get(genre_url).json().get('genres')

# print(genre_response)

for name in genre_response:
    genre = Genre()
    genre.id = name['id']
    genre.name = name['name']
    genre.save()

for i in range(1,11):
    movie_url = f'https://api.themoviedb.org/3/movie/popular?api_key={apikey}&language=ko&page={i}'
    movie_response = requests.get(movie_url).json().get('results')
    
    # print(movie_response)
    for name in movie_response:
       
        movie = Movie()
        movie.title = name['title']
        movie.rank = name['vote_average']
        movie.movie_id = name['id']
        movie.audience = name['popularity']
        movie.poster_url = name['poster_path']
        movie.overview = name['overview']
        movie.original_lang =  name['original_language']
        movieData2 = '''
        [
        {"2067":"qKL_l-3p1xU"}, {"하드 킬": "D1yo-zswLw4"}, {"스폰지밥 무비: 핑핑이 구출 대작전": "iXmokylChTo"}, {"그린랜드": "LwkHfve3m7U"}, {"마녀를 잡아라": "LwkHfve3m7U"}, {"로그 시티": "w1Ww62eIwOI"}, {"뮬란": "UmRfA5N5BPM"}, {"뉴 뮤턴트": "NwJpyKI-F-0"}, {"웰컴 투 서든 데쓰": "SwB9l6Pg7qg"}, {"원스 어폰 어 스노우맨": "H35-mSD11Tk"}, {"커넥트": "NUUe6i8QNGU"}, {"에놀라 홈즈": "ahG89RwXIzs"}, {"반도": "StbRpbmRRNw"}, {"징글 쟁글: 저니의 크리스마스": "EON4CiUedT4"}, {"브이에프더블유": "EON4CiUedT4"}, {"배트맨: 데스 인 더 패밀리": "EON4CiUedT4"}, {"로그": "2OoQCTIYER4"}, {"플레인 하이스트": "DQQL1bPcvR0"}, {"런던 시계 탑 밑에서 사랑을 찾을 확률": "nnAc7jROgvY"}, {"에이바": "oTT119fGFBY"}, {"극장판 귀멸의 칼날: 무한열차편": "Gr06R3YNcGY"}, {"보랏 속편": "Gr06R3YNcGY"}, {"아르테미스 파울": "IkdYCbjOSAs"}, {"킹 아더 카멜롯의 기사": "TPFdj0J1ffE"}, {"아메리칸 파이: 여자의 규칙": "TPFdj0J1ffE"}, {"위 베어 베어스: 더 무비": "TPFdj0J1ffE"}, {"나쁜 녀석들: 포에버": "ZJvhVyh1VkM"}, {"헤븐퀘스트": "1447dDuESwA"}, {"바바 야가": "1447dDuESwA"}, {"산타나": "mGiKX8MvC5I"}, {"조커": "8BDlo5VMbvQ"}, {"버즈 오브 프레이: 할리 퀸의 황홀한 해방": "Zte3-EoqzMQ"}, {"어쌔신 프리스트 벡맨": "tIFPdv8DQ4c"}, {"트롤: 월드 투어": "rGDBFQjYegM"}, {"아카이브": "4LCPImjld4s"}, {"벡키": "4LCPImjld4s"}, {"루도 - 인생 게임": "4LCPImjld4s"}, {"해피 할로윈, 스쿠비 두!": "4LCPImjld4s"}, {"인베이젼 2020": "Dwf49-UzKM4"}, {"겨울왕국 2": "8LMUkZlSmAs"}, {"프로젝트 파워": "5SJFR8-ozb4"}, {"택스 콜렉터": "Mc9RtRD93yQ"}, {"피니와 퍼브: 캔디스 대 우주": "Mc9RtRD93yQ"}, {"스펠": "g_PSbYcPznQ"}, {"수퍼 소닉": "bVQ90k5nGtU"}, {"스푸트니크": "bVQ90k5nGtU"}, {"그레이하운드": "InRMkw-jQZA"}, {"어벤져스: 인피니티 워": "9oVkuHLpMjs"}, {"치크 파이트": "9oVkuHLpMjs"}, {"워 위드 그랜파": "DM0JNRvEIsE"}, {"영안실의 미스테리": "DM0JNRvEIsE"}, {"컷 스로트 시티": "ib6aWcPbL0g"}, {"온워드: 단 하루의 기적": "tE3mdsfBYjA"}, {"타겟 넘버 원": "oNobfCpjA8Y"}, {"아무도 없다": "916oToe8tfs"}, {"스쿠비!": "Sm3TqFIXODY"}, {"그 남자의 집": "Sm3TqFIXODY"}, {"모탈: 레전드 오브 토르": "CXDdIefYrZw"}, {"원 나이트 인 방콕": "CXDdIefYrZw"}, {"나의 히어로 아카데미아 더 무비: 히어로즈 라이징": "YSM4KbIL6rk"}, {"블러드샷": "7dXlX0WdBT4"}, {"시크릿 소사이어티 오브 세컨드 본 로얄": "Zq2OLayDn9k"}, {"쥬만지: 넥스트 레벨": "p9rnQiEfVkE"}, {"정도": "Y7LCYXhq8ko"}, {"베이비시터를 위한 몬스터 사냥 가이드": "fKL3sOXnaRk"}, {"분노의 질주: 홉스 & 쇼": "k3uszPh2efQ"}, {"그것: 두 번째 이야기": "MD3G6TSn1L4"}, {"홀리데이트": "MD3G6TSn1L4"}, {"데스 오브 미": "MD3G6TSn1L4"}, {"올드 가드": "qzFCNiyeq8k"}, {"러브 앤 몬스터즈": "EeBQPeAfvfY"}, {"신 에반게리온 극장판 :||": "EeBQPeAfvfY"}, {"캣츠 앤 독스 3: 퍼스 유나이트": "EeBQPeAfvfY"}, {"어벤져스: 엔드게임": "J-3ppZk1MbA"}, {"사일런싱": "J-3ppZk1MbA"}, {"그린치": "MmKlIGkxGyM"}, {"크리스마스에 날아갑니다": "MmKlIGkxGyM"}, {"익스트랙션": "dB5NOpzd0Jk"}, {"인퍼머스": "zm8DVHkrT7Y"}, {"베놈": "VVVVwgAvN78"}, {"헌팅 오브 더 메리 셀레스트": "VVVVwgAvN78"}, {"라이온 킹": "bn5al7Ypcqg"}, {"모탈 컴뱃 레전드: 스콜피온의 복수": "G6eGkQ1ebxc"}, {"스파이더맨: 뉴 유니버스": "Bgh4sPrRIY4"}, {"크리스마스 스위치 - 한 번 더 바꿔?": "pwkiLvXLTUo"}, {"포스 오브 네이쳐": "cDT_Mjry03U"}, {"1917": "pqy-XGbvNO4"}, {"존 윅 3: 파라벨룸": "6mdAfG581yM"}, {"클라우즈": "4br4SqKOoBk"}, {"3022: 지구 대폭발": "__6vP5mNbY4"}, {"스파이더맨: 파 프롬 홈": "Pod3zdF6scI"}, {"라이어트: 기계들의 역습": "Pod3zdF6scI"}, {"토이 스토리 4": "S_Shzegh6Cc"}, {"터미네이터: 다크 페이트": "WcR7Akq7yQE"}, {"레거시 오브 라이즈": "WcR7Akq7yQE"}, {"피노키오": "Y-8Mg4i1cjQ"}, {"아이를 부탁해": "Y-8Mg4i1cjQ"}, {"사이언티스트": "Y-8Mg4i1cjQ"}, {"스타워즈: 라이즈 오브 스카이워커": "SVdTrZhfYC0"}, {"더 레고 스타 워즈 홀리데이 스페셜": "SVdTrZhfYC0"}, {"레이디 드라이버": "HYc47oM2m94"}, {"말레피센트 2": "iCyWP0n7OuQ"}, {"백두산": "BN62ur59h0g"}, {"겟 아웃 얼라이브": "a_nVEi-a7bw"}, {"바비의 프린세스 어드벤처": "a_nVEi-a7bw"}, {"라이징 호크": "a_nVEi-a7bw"}, {"놈놈놈: 캔자스의 무법자": "FZcBwPoUpMg"}, {"포르노의 막이 내린 후에 2": "FZcBwPoUpMg"}, {"가족의 죄": "FZcBwPoUpMg"}, {"아파트 209": "FFiPZUp-UBg"}, {"다크 포스": "FFiPZUp-UBg"}, {"업사이드 다운 매직": "PaaIhJAunP8"}, {"엑설런트 어드벤쳐 3": "noUPnJAO6Iw"}, {"슈퍼 에이전트 메이키": "noUPnJAO6Iw"}, {"드래곤하트: 벤지언스": "noUPnJAO6Iw"}, {"코코": "2OS-_8N5t0Q"}, {"명탐정 피카츄": "atPBX4bTWhI"}, {"비포 더 파이어": "atPBX4bTWhI"}, {"이 멋진 세계에 축복을! 붉은 전설": "GXp6N7eHVWE"}, {"가질 수 없는": "y-LIakl8hl0"}, {"터지기전에": "y-LIakl8hl0"}, {"어쌔신 33 A.D.": "y-LIakl8hl0"}, {"아웃포스트": "96Iwt5l8am8"}, {"보루토 - 나루토 더 무비": "96Iwt5l8am8"}, {"알라딘": "wbWu9P16Rt8"}, {"쥬라기 월드: 폴른 킹덤": "WDRdAxKp-PQ"}, {"더 라스트 - 나루토 더 무비": "WymhBpIrtzY"}, {"Megan Is Missing": "-4BMH7vsEeM"}, {"세라 쿠퍼: 아주 좋아!": "-4BMH7vsEeM"}, {"데스스트록: 나이츠 앤 드래곤즈": "-4BMH7vsEeM"}, {"마이펫의 이중생활  2": "q83QVRj5ldQ"}, {"ABC 오브 데쓰": "q83QVRj5ldQ"}, {"Cuidado con lo que deseas": "nZDyLHmqWA8"}, {"좀비랜드: 더블 탭": "yQ_vN4pVs-w"}, {"콜 오브 와일드": "HG9-7jM944w"}, {"제미니 맨": "vc-rvMuCpQM"}, {"딥워터": "SPivebgcNB0"}, {"크루즈 패밀리: 뉴 에이지": "SPivebgcNB0"}, {"메가로돈": "JfdrGDdBQyI"}, {"날씨의 아이": "NbJK4tPycQ0"}, {"언더워터": "mI7WvoFshm0"}, {"플레이데이트 위드 데스티니": "mI7WvoFshm0"}, {"테리파이어": "mI7WvoFshm0"}, {"램프 라이프": "zROM8XueVbA"}, {"블랙 팬서": "eipXk13afQ4"}, {"애프터": "BWUn15b57cQ"}, {"앵그리 버드 2: 독수리 왕국의 침공": "AOoYuCKh2RE"}, {"살육 호텔": "AOoYuCKh2RE"}, {"센티그레이드": "AOoYuCKh2RE"}, {"람보: 라스트 워": "Yy7mfTlYXJ0"}, {"레베카": "PpNsdVupC48"}, {"사냥의 시간": "aFy4By4H0vY"}, {"닥터 두리틀": "PPx3nfhAo5k"}, {"나이트메어 서커스": "kDeuZfOaTSA"}, {"그 숲에선 누구도 잠들 수 없다": "kDeuZfOaTSA"}, {"포드 V 페라리": "eq40nsZM8mY"}, {"주먹왕 랄프 2: 인터넷 속으로": "BOWythdbcZs"}, {"6 언더그라운드": "zPPQmsyUSNQ"}, {"청춘 돼지는 꿈꾸는 소녀의 꿈을 꾸지 않는다": "AiPGoAAzZnY"}, {"고블린 슬레이어: 고블린 크라운": "mnXjoHJv040"}, {"쥬라기 월드": "cvfXhyAhNok"}, {"엔젤 해즈 폴른": "kkFbKCQFb_Q"}, {"캡틴 마블": "bTiLvaRMRtU"}, {"주온": "Zifik5PtYCg"}, {"레디 플레이어 원": "tMQWaEI7Loo"}, {"립타운": "tMQWaEI7Loo"}, {"아이언 마스크: 용패지미": "eWz1QcCab9Q"}, {"해리 포터와 마법사의 돌": "piY0Z-opP_E"}, {"더 킹 오브 스태튼 아일랜드": "piY0Z-opP_E"}, {"아빠를 찾습니다": "P8tb-vfAHr8"}, {"더 원 앤 온리 이반": "52sq3MR5Jfw"}, {"사탄의 사자: 망자의 저주": "52sq3MR5Jfw"}, {"도라와 잃어버린 황금의 도시": "NcgQMQky-v0"}, {"종이의 집": "xKS1FgZ94dw"}, {"U-235: 무적의 잠수함": "5JRhfSQza7I"}, {"부산행": "jr_cvTxIEb8"}, {"앨빈과 슈퍼밴드: 악동 어드벤처": "cALzBOSk0HU"}, {"스타걸": "cALzBOSk0HU"}, {"고질라: 킹 오브 몬스터": "CQTFqueVq9g"}, {"크리스마스 스위치": "h_y-GpZZEVk"}, {"모노스": "5uTKyZ9ERig"}, {"Tremors: Shrieker Island": "JXcJUgDaAIU"}, {"지오스톰": "sgKqtIBuu_Q"}, {"너의 이름은.": "f0YOHq-VwEc"}, {"샤잠!": "PsUTdwXtlsk"}, {"매직 캠프": "sftIJT_ek-U"}
        ]
        '''

        info = json.loads(movieData2)
        for ele in info:
            title = name['title']
            if title in ele:
                # print(title)
                movie.video_id = ele[title]
                break
        movie.save()
        for genre in name['genre_ids']:
            movie.genre.add(genre)
        
