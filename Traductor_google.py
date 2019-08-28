import requests
from bs4 import BeautifulSoup


class TranslatorGoogle():

    def __init__(self,proxies=False):

        self.proxies=None
        self.url_trad='https://www.google.com/async/translate?vet=12ahUKEwibsYqynPniAhUSKa0KHXdwBFMQqDgwAHoECAkQGA..i&ei=zhcMXZuSHpLStAX34JGYBQ&client=firefox-b-d&yv=3&gsawvi=1'


    def translate(self,object):
        if type(object)==str:
            object = object.replace('.','').replace(',','').replace(';','').replace('\xa0','').replace(':','').replace('*','')
            object=[object]
        traducciones=[]
        for texto in object:
            texto = texto.replace('.','').replace(',','').replace(';','').replace('\xa0','').replace(':','').replace('*','')
            data = {
                'async': 'translate,sl:en,tl:es,st:' + texto + ',id:1561074010834,qc:true,ac:true,_id:tw-async-translate,_pms:s,_fmt:pc'}
            response = requests.post(self.url_trad,data=data,proxies=self.proxies)
            source = response.text
            self.soup = BeautifulSoup(source, 'lxml')
            #print(self.soup)
            try:
                traduccion=self.soup.find('span',id='tw-answ-target-text').text
            except:
                try:
                    url='https://www.google.com/async/translate?vet=12ahUKEwjM7dyyo_niAhUnjK0KHcq5BlgQqDgwAHoECAsQFw..i&ei=Jh8MXczCNqeYtgXK85rABQ&client=firefox-b-d&yv=3&gsawvi=1'
                    data={'async':'translate,sl:en,tl:es,st:'+texto+',id:1561075524442,qc:true,ac:true,_id:tw-async-translate,_pms:s,_fmt:pc'}
                    response = requests.post(url, data=data, proxies=self.proxies)
                    source = response.text
                    self.soup = BeautifulSoup(source, 'lxml')
                    traduccion = self.soup.find('span', id='tw-answ-target-text').text
                except:
                    traduccion='No se pudo traducir'
            traducciones.append(traduccion)

        return traducciones

if __name__=='__main__':
    original = ["Excuse us dear", "If not you, then who? If not now, then when?","At the end of the day, if I can say I had fun, it was a good day."]
    frases = TranslatorGoogle().translate(original)
    for i,traduc in enumerate(frases):
        print(original[i] + " ------> "+ traduc)
