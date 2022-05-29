for page in range(1,3):
        Sise_url='https://finance.naver.com/sise/sise_market_sum.naver?&page=%d' %page
        #print(Sise_url)

        html=urllib.request.urlopen(Sise_url) #url 요청하여 응답받은 웹 페이지 저장
        soup=BeautifulSoup(html,'html.parser') #BeautifulSoup 객체 생성
        
        no=soup.select('tbody>tr>td:nth-child(2)>a')[0]['href'].split('=')
        cd=no[1]
        name=soup.select('tbody>tr>td:nth-child(2)>a')
        price=soup.select('tbody>tr>td:nth-child(3)')

for cd,name, price in zip(cd,name,price):
            print(cd,name.text,price.text) 
            data.append([cd,name.text, price.text])