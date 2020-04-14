from bs4 import BeautifulSoup as bs
import requests

html = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250").text
soup = bs(html,'lxml')

class data:    
    def __init__(self,tittle,rating,directors,writers,stars,summary):
        self.directors=[]
        self.writers=[]
        self.stars=[]
        self.title=title
        self.rating=rating
        dire = directors.split(',')
        for i in dire:
            check=i.split(" ")
            if (len(check)>1 and check[1]=="more"):
                break
            if (i=="1 more credit" or i == "See full cast & crew"):
                break
            self.directors.append(i)
        writ = writers.split(',')
        for i in writ:
            check=i.split(" ")
            if (len(check)>1 and check[1]=="more"):
                break
            if (i=="1 more credit" or i == "See full cast & crew"):
                break
            self.writers.append(i)
        star= stars.split(',')
        for i in star:
            check=i.split(" ")
            if (len(check)>1 and check[1]=="more"):
                break
            if (i=="1 more credit" or i == "See full cast & crew"):
                break
            self.stars.append(i)
        self.summary=summary
       
    def fun(self):
        print(rating)
        print("Title : ",self.title,summary,"\ndirectors : ",end="")
        for i in self.directors:
            print(i,end=",")
        print("\nwriters : ",end="")
        for i in self.writers:
            print(i,end=", ")
        print("\nstars : ",end="")
        for i in self.stars:
            print(i,end=", ")
        print("\n----------------------------------------------------------------------------------------")
       
           
table=soup.find('tbody')
c=1
record=[]
for row in table.find_all('tr'):
    title = row.find('img')['alt']
    title = title.strip()
    rating = row.find('td',class_="ratingColumn imdbRating").strong.text
    link =row.find('a')['href']
    link=link.split('/')
    m_link="https://www.imdb.com/title/"+link[2]
    movie= requests.get(m_link).text
    movie_soup=bs(movie,'lxml')
    s1=""
    focus= movie_soup.find('div',class_="plot_summary_wrapper")
    summary= focus.find('div',class_="summary_text").text
    summary= summary.strip()
    for div in focus.find_all('div',class_="credit_summary_item"):
        for a in div.find_all('a'):
            s1+=a.text +","
        s1+="**"
    s1=s1.split("**")
    dire=s1[0]
    writ=s1[1]
    acto=s1[2]
    node= data(title,rating,dire,writ,acto,summary)
    record.append(node)
    node.fun()
    c+=1
    if(c==10):
        break