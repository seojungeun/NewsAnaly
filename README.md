python 데이터 수집 메뉴얼

python 버전: python 3.6.5

--------------중요 모듈 설치 명령어------------
python 설치 라이브러리 :

팬텀JS 설치: http://phantomjs.org/download.html

import urllib.parse

import psycopg2
	설치 방법 : pip install psycopg2

from bs4 import BeautifulSoup
	설치 방법 : pip install beautifulsoup4

from selenium import webdriver
	설치 방법 : pip install selenium

----------------------------------------------------
작동은 mainColct.py 을 실행 하시면 데이터 수집이 시작 됩니다.

아래의  파라미터 정보를 바꿔주셔야 합니다
browser_path='C:/Users/seo/Desktop/phantomjs-2.1.1-windows/bin/phantomjs.exe' 팬텀 JS 가 설치된 경로
									- 팬텀 JS 는 http://phantomjs.org/download.html 에서 설치 합니다

output='C:/Users/seo/Desktop/BioWebCollect/' 논문 파일 다운로드 경로
delay=2    페이지 로딩 시간
order_input=2 수집 시작 페이지
order=7	 수집 종료 페이지 



	
	
	



