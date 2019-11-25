# -*- coding: utf-8 -*-
import multidict as multidict
import psycopg2
import sys
from io import StringIO
from os.path import isfile, join
from os import listdir
import os
import re
from PIL import Image
from wordcloud import WordCloud
import numpy as np



def tblAnalyQuery(data_ty, dataClkwTtle, dataClorTtle, dataClprEndDe,dataClprBeginDe):
    #   Default port =1200
    keyword_query = []
    comMa = "'"
    conn_string = "host='121.160.17.80' dbname ='EcoBank' user='dev' password='nie12345' port='12000'"
    conn = psycopg2.connect(conn_string)
    curs = conn.cursor()

    query = """
        SELECT         
        ere_wrd_ttle AS "ereWrdTtle"
        , sum(sum_count) AS "wrdEreCo"
        FROM   data_scraping_analysis.vw_data_anals_result
        WHERE 
            1=1
        """
    if not data_ty is None:
        if not data_ty is '':
            query =  query + """
            AND
            (data_ty=""" + comMa + data_ty + comMa + """)
        """   
    if not dataClkwTtle is None:
        if not dataClkwTtle is '':
            query =  query + """
            AND 
            (data_clkw_ttle =""" + comMa + dataClkwTtle + comMa + """)
         """ 
    if not dataClorTtle is None:
        if not dataClorTtle is '':
            query =  query + """
            AND 
            ( data_clor_ttle= """ + comMa + dataClorTtle + comMa + """)
        """ 
    if not dataClprEndDe is None: 
        if not dataClprEndDe is '':
            query =  query + """
            AND
            ( news_colct_de <= """ + comMa + dataClprEndDe + comMa + """)
             """ 
    if not dataClprBeginDe is None:
        if not dataClprBeginDe is '':
            query =  query + """
            AND
            (news_colct_de >= """ + comMa + dataClprBeginDe + comMa + """)
        """
    query =  query+"""
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
    # os.getcwd()
    os.chdir(infile)
    files = [f for f in listdir(infile) if isfile(join(infile, f))]
    files = [x for x in files if x.find("png") != -1]
    return files


def keywordTrim(tblAnalyQuery,stopWord):
    minSize = 0
    keyword = []
    count = []
    keyword_query = tblAnalyQuery(data_ty, dataClkwTtle, dataClorTtle, dataClprEndDe,dataClprBeginDe)
    maxSize = len(keyword_query)
    for minSize in range(minSize, maxSize):
        if keyword_query[minSize][0] not in stopWord:
                 keyword.append(keyword_query[minSize][0])
        
        count.append(keyword_query[minSize][1])
    return keyword




def getFrequencyDict(tblAnalyQuery):
    minSize = 0
    fullTermsDict = multidict.MultiDict()
    keyword_query = tblAnalyQuery(data_ty, dataClkwTtle, dataClorTtle, dataClprEndDe,dataClprBeginDe)
    maxSize = len(keyword_query)
    print(maxSize)
    for minSize in range(minSize, maxSize):
        fullTermsDict.add(keyword_query[minSize][0], float(keyword_query[minSize][1]))
    return fullTermsDict


def wordCloudGenerate(files, font, saveFile, fileName,stopWord):
    alice_mask = np.array(Image.open(files))
    # wc1 = WordCloud(font_path=font, background_color="white", max_words=1000, mask=alice_mask, max_font_size=100,
    #                 contour_width=2, contour_color='steelblue',width=400,height=400)
    wc1 = WordCloud(font_path=font, background_color="white", mask=alice_mask, width=1987, height=736,
                    contour_width=2, contour_color='steelblue')
    wordcloud = WordCloud(font_path=font)
    wordcloud.generate(str(keywordTrim(tblAnalyQuery,stopWord))).to_image()
    # wc1.generate(str(keywordTrim(tblAnalyQuery))).to_image()
    wc1.generate_from_frequencies(getFrequencyDict(tblAnalyQuery)).to_image()
    wordcloud.to_file(saveFile + fileName + 'defult' + '.png')
    wc1.to_file(saveFile + fileName + '.png')
    savePath = saveFile + fileName + '.png'
    return savePath


def main(fileName, font, infile, saveFile, pictureNm, stopWord):
    selectFile = []
    pictureslist = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png']
    maskSelect(infile)
    files = maskSelect(infile)

    for file in files:
        if file == pictureslist[pictureNm]:
            selectFile.append(file)

    #     file=files[pictureNm]
    wordCloudGenerate(selectFile[0], font, saveFile, fileName,stopWord)
    savePath = saveFile + fileName + '.png'
    print(savePath)


if __name__ == "__main__":
	runPath = os.path.dirname(os.path.abspath(__file__))
	print('runPath = ' + runPath)
	fileName = sys.argv[3]
	font = sys.argv[5]
	infile = runPath + '/' + sys.argv[1]
	saveFile  = sys.argv[2]
	pictureNm = int(sys.argv[4])
	stopWord=sys.argv[11]
	data_ty= sys.argv[6]
	dataClkwTtle= sys.argv[7]
	dataClorTtle=sys.argv[8]
	colctDe=''
	dataClprEndDe=sys.argv[9]
	dataClprBeginDe=sys.argv[10]
	print(fileName)

	tblAnalyQuery(data_ty, dataClkwTtle, dataClorTtle, dataClprEndDe,dataClprBeginDe)
	main(fileName, font, infile, saveFile, pictureNm,stopWord)
