from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys






#Please write gecko drivers path down here
browser = webdriver.Firefox(executable_path=r'gecko drivers path here')

""" login part """
browser.get("https://www.instagram.com/")
time.sleep(2)
idm = browser.find_element_by_name("username")
passw = browser.find_element_by_name("password")


# write your user name and password to log and pas areas.
log = "un here"
pas = "pw here"
idm.send_keys(log)
passw.send_keys(pas)
buton = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
buton.click()
time.sleep(3)



browser.get("https://www.instagram.com/"+log)



def scroll():
    global browser
    footer = browser.find_element_by_tag_name('footer')
    last_height = browser.execute_script('return document.body.scrollHeight')
    while True:
        footer.location_once_scrolled_into_view
        time.sleep(2)
        new_height = browser.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        else :
            last_height = new_height
scroll()




classes = browser.find_elements_by_class_name("v1Nh3 ")

links = []
for eleman in classes:
    links.append(eleman.find_element_by_tag_name('a'))

time.sleep(3)

links= [elem.get_attribute('href') for elem in links
                         if '.com/p/' in elem.get_attribute('href')]

#keeps likers for posts in order to add them to wholelikerslist
likersList = []
wholeLikers = []

def clickLikers():
    
    time.sleep(2)
    likers = browser.find_element_by_css_selector("a.zV_Nj:nth-child(2)")
    time.sleep(1)
    likers.click()
    time.sleep(1)

def likerListCheck():
   
   
    global likersList
    
    likersList = list(set(likersList))
    time.sleep(1)
    for liker in likersList:
        wholeLikers.append(liker)
    likersList = []




def likeScroll():
    exceptioncount = 0
    namecount = 0
    likerTab = browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div")
    actions = ActionChains(browser)
    likerTab.click()
    time.sleep(0.5)
    actions.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    exect = """
    followers = document.querySelector(".i0EQd > div:nth-child(1)");
    var lenOfPage=followers.scrollHeight;
    return lenOfPage;"""
    lenOfPage = browser.execute_script(exect)
    match=False 
    while(match==False):
        likername = browser.find_elements_by_css_selector(".FPmhX.notranslate.MBL3Z")
        lastCount = lenOfPage
        time.sleep(1)
        
        try:
            for eleman in likername:
                user = eleman.get_attribute('title')
                namecount +=1 
                print(namecount, " " , user)
                likersList.append(user)
        except:
            exceptioncount +=1 
            print(exceptioncount, "    ***************An exception occurred*****")
        time.sleep(0.5)
        actions.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(2)
        
        
        lenOfPage = browser.execute_script(exect)
        if lastCount == lenOfPage:
            match=True


ct = 0

for post in links:
    browser.get(post)
    time.sleep(6)
    clickLikers()
    time.sleep(2)
    likeScroll()
    time.sleep(1)
    likerListCheck()
    time.sleep(1)
    print(likersList)
    ct +=1
    
    

# change the current path of Followers below with  path of text file that contain your whole followers
Followers = open(r"Followers text file's path here", "r")
followerLines = Followers.readlines()



comparedFollowers = []
for person in followerLines:
        isLiked = False
        for liker in wholeLikers:
            if(person.strip() == liker.strip()):
                newline = person.strip()+"-"+ str(wholeLikers.count(liker))
                comparedFollowers.append(newline)
                isLiked = True
                break
        if(isLiked == False):
            line = person.strip()+"-"+"0"
            comparedFollowers.append(line)



#we obtained the list but it is not sorted.

LastList = sorted(comparedFollowers, key = lambda x: x.split('-')[1],reverse=True)


with open("comparedFollowers6.txt","w",encoding = "UTF-8") as file:
    for line in LastList:
        file.write(line+"\n")












               





