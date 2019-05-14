# -*- coding: cp949 -*-

# %load ecobankWordcloud.py
import config
import numpy as np
import psycopg2

# 경로설정
from io import StringIO
from os.path import isfile ,join
from os import listdir
import os
import re
from PIL import Image

# 워드 클라우드 생성
from wordcloud import WordCloud

# 쿼리조건
# data_ty= 유형 쿼리, dataClkwTtle=대상,dataClorTtle= 주기


# 쿼리조건
# data_ty= 유형 쿼리, dataClkwTtle=대상,dataClorTtle= 주기

def tblAnalyQuery(data_ty,dataClkwTtle,dataClorTtle,colctDe):  
    keyword_query=[]
    comMa="'"
    #   Default port =1200
    conn_string = "host='121.160.17.80' dbname ='EcoBank' user='dev' password='nie12345' port='12000'"
    conn = psycopg2.connect(conn_string)
    curs = conn.cursor()

    query ="""
           SELECT         
        ere_wrd_ttle AS "ereWrdTtle"
        , sum(sum_count) AS "wrdEreCo"
        FROM   data_scraping_analysis.vw_data_anals_result
        WHERE 
        (data_ty is not null or data_ty="""+comMa+data_ty+comMa+""")
        AND (data_clkw_ttle is not null or data_clkw_ttle ="""+comMa+dataClkwTtle+comMa+""")
        AND (data_clor_ttle is not null or data_clor_ttle= """+comMa+dataClorTtle+comMa+""")
        AND(news_colct_de is not null or news_colct_de = """+comMa+colctDe+comMa+""")
        group by data_anals_no 
               , data_ty 
               , ere_wrd_ttle 
               , data_clkw_ttle 
               , data_clor_ttle 
               , news_colct_de 
               , sum_count

        ORDER BY
            data_anals_no ASC"""

    curs.execute(query)
    rows = curs.fetchall()
    for row in rows:
        keyword_query.append(row)
    conn.close()
    return keyword_query
    
	
def maskSelect(infile):
    os.chdir(infile)
    # 모든 파일정보
    files = [f for f in listdir(infile) if isfile(join(infile, f))]
    # 마스크 정보
    files = [x for x in files if x.find("png") != -1] 
    return files
    
def keywordTrim(tblAnalyQuery):
    minSize=0
    keyword=[]
    count=[]
    keyword_query=tblAnalyQuery(data_ty,dataClkwTtle,dataClorTtle,colctDe)
    maxSize=len(keyword_query)
    for minSize in range (minSize,maxSize):
        keyword.append(keyword_query[minSize][0])
        count.append(keyword_query[minSize][1])
    return keyword
	
def wordCloudGenerate(files,font,saveFile,fileName):
    alice_mask = np.array(Image.open(files))
    wc1 = WordCloud(font_path=font,background_color="white", max_words=2000, mask=alice_mask,max_font_size=30,
                   contour_width=2, contour_color='steelblue')
    wordcloud = WordCloud(font_path =font)
    wordcloud.generate(str(keywordTrim(tblAnalyQuery))).to_image()
    
    wc1.generate(str(keywordTrim(tblAnalyQuery))).to_image() 
    
    wordcloud.to_file(saveFile+fileName+'defult'+'.png')
    wc1.to_file(saveFile+fileName+'.png')
    savePath=saveFile+fileName+'.png'
    return savePath
	
def main(fileName,font,infile,saveFile,pictureNm):
    selectFile=[]
    pictureslist=['0.png','1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png', '9.png']
    maskSelect(infile)
    files =maskSelect(infile)
    
    for file in files:
        if file ==pictureslist[pictureNm]:
            selectFile.append(file)    
            
    wordCloudGenerate(selectFile[0],font,saveFile,fileName)
    savePath=saveFile+fileName+'.png'
    print(savePath)

if __name__ == "__main__":
    infile=config.infile
    saveFile=config.saveFile
    fileName=config.fileName
    pictureNm=config.pictureNm
    font=config.font 
    data_ty=config.data_ty
    dataClkwTtle=config.dataClkwTtle
    dataClorTtle=config.dataClorTtle
    data_ty=config.data_ty
    colctDe=config.colctDe
    tblAnalyQuery(data_ty,dataClkwTtle,dataClorTtle,colctDe)
    
    main(fileName,font,infile,saveFile,pictureNm)
    
    
