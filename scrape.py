from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

class AcademicScrape():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def get_page(self):
        self.driver.get('https://academic.oup.com/cid/article/75/4/657/6448919')
        time.sleep(5)
    def accept_cookies(self):
        self.driver.find_element(By.CLASS_NAME,'cookiepolicycontinue').click()
    def get_data_page(self):
        # self.driver.execute_script("arguments[0].scrollIntoView(true);",'class="fig-view-orig openInAnotherWindow btn js-view-large"')
        # self.driver.implicitly_wait(5)
        # time.sleep(5)
        # self.driver.find_element(By.CLASS_NAME,'fig-view-orig openInAnotherWindow btn js-view-large')
        # self.driver.execute_script("window.scrollTo({left: 0, top: document.body.scrollHeight, behavior : 'smooth'});")
        # time.sleep(2)
        # self.driver.find_element(By.CLASS_NAME,'fig-view-orig openInAnotherWindow btn js-view-large')
        x=0
        page = self.driver.find_element(by=By.TAG_NAME, value='body')
        while True:
            page.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.9)
            x+=1
            if x==10:
                break
        self.driver.get('https://academic.oup.com/view-large/372144023')     

    def data_frame(self):
        plwhiv_data={
            'category':['No. of participants','Site','Kayunga, Uganda','South Rift Valley, Kenya','Kisumu West, Kenya','Mbeya, Tanzania','Abuja and Lagos, Nigeria','Age at most recent visit','18-24','25-39','40-49','>=50','Sex','Male','Female','Marital status','Married','single','Divorced/Seperated','Widowed','Other','Religion','Catholic Christian','Non catholic Christian','Muslim','Traditionalist','Other','Highest level of school(n=2722)','No school','Primary','Secondary','University/Vocational','Other','Currently employed(n=2723)','No','Yes'],
            'Total N(%)':['2724','','503(18.5)','944(34.7)','500(18.4)','500(18.4)','277(10.2)','','119(4.4)','961(35.3)','940(34.5)','704(25.8)','','1134(41.6)','1590(58.4)','','317(11.6)','1549(57.0)','404(14.8)','437(16.1)','16(0.6)','','680(25.0)','1837(67.4)','184(6.8)','19(0.7)','4(0.1)','','108(4.0)','1469(54.0)','803(29.5)','340(12.5)','2(0.1)','','1653(60.7)','1070(39.3)'],
            'Dead n(%)':['118','','37(7.4)','33(3.5)','24(4.8)','14(2.8)','10(3.6)','','5(4.2)','40(4.2)','45(4.8)','28(4.0)','','58(5.1)','60(3.8)','','14(4.4)','60(3.9)','25(6.2)','18(4.1)','0(0.0)','','38(5.6)','66(3.6)','11(6.0)','3(15.8)','0(0.0)','','6(5.6)','64(4.4)','37(4.6)','10(2.9)','0(0.0)','','69(4.2)','48(4.5)'],
            'Alive n(%)':['2606','','466(92.6)','911(96.5)','476(95.2)','486(97.2)','267(96.4)','','114(95.8)','921(95.8)','895(95.2)','676(96.0)','','1076(94.9)','1530(96.2)','','303(95.6)','1489(96.1)','379(93.8)','419(95.9)','16(100.0)','','642(94.4)','1771(96.4)','173(94.0)','16(84.2)','4(100.0)','','102(94.4)','1405(95.6)','766(95.4)','330(97.1)','2(100)','','1584(95.8)','1022(95.5)'],
            'Mortality Unadjusted HR(95%CI)':['...','','1.00','0.47(.29-.75)','0.64(.38-1.07)','0.44(2.4-8.2)','0.53(.26-1.06)','','1.00','0.63(.25-1.61)','0.68(.27-1.72)','0.55(.21-1.42)','','1.00','0.72(.50-1.03)','','1.35(.76-2.42)','1.00','1.66(1.04-2.64)','1.04(.61-1.75)','...','','1.59(1.07-2.37)','1.00','1.70(.90-3.22)','4.83(1.52-15.40)','...','','1.00','0.80(.35-1.85)','0.84(.36-1.99)','0.56(.20-1.54)','...','','1.00','1.05(.73-1.52)'],
            'P value':['...','','','.002','.087','.009','.074','','','.339','.415','.213','','','.076','','.311','','.033','.890','...','','.023','','.104','.008','...','','','.603','.695','.260','','','','.797']

           }
        df=pd.DataFrame(plwhiv_data)
        df.to_csv('plwhiv_mortality.csv')
        #print(df)



def run():
    crawl=AcademicScrape()
    crawl.get_page()
    crawl.accept_cookies()
    crawl.get_data_page()
    crawl.data_frame()
if __name__=='__main__':
    run()