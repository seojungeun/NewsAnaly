
----------------------------------------------In Put 정보-----------------------------------------------
infile= 'C:/Users/seo/Desktop/wordcloud/'  -> 워드 클라우드 이미지가 저장된 화면 파라미터 정보입니다  
saveFile='C:/Users/seo/Desktop/wordCloudImage/' ->워드 클라우드가 저장될 경로 설정입니다
fileName='wordcloud' 저장 파일 명
pictureNm=0 -> 마스크가 저장된 파일 리스트 숫자입니다.
font = 'C:\Windows\Fonts\HYSUPM.ttf' -> 폰트 경로를 호출하는 변수 입니다.


----------------------------------------------Out Put 정보-----------------------------------------------
savePath -> 이미지 파일 저장 경로(파일명 포함)


---------------------------------------------마스크 매핑 정보-----------------------------------------------

0.png     defult 마스크입니다 
1.png     화살표 마스크 입니다
2.png	타원 마스크 입니다
3.png	새 마스크 입니다
4.png	다이아몬드 마스크 입니다
5.png	공룡 마스크 입니다
6.png	소녀 마스크 입니다
7.png	총 마스크 입니다
8.png	하트 마스크 입니다
9.png	마름모 마스크 입니다

공룡 마스크 사용 할 경우 pictureNm=5 
---------------------------------------------------------------------------------------------------------------
그림 번호


쿼리 조건 정보
    data_ty  => 논문 타입 정보
    dataClkwTtle => 대상선택 정보
    dataClorTtle => 키워드 정보
    colctDe=>날짜 정보


1. ecobankWordcloud.py 접근하여 tblAnalyQuery(data_ty,dataClkwTtle,dataClorTtle ,colctDe)  파리미터 정보에 맞게  쿼리 함수를 호출 합니다.
2. main(fileName,font,infile,saveFile,pictureNm) 파라미터 정보에 맞게 메인 함수를 호출합니다.