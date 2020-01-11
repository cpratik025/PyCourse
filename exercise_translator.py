from translate import Translator

trns = Translator(to_lang='ja')
with open('app/test.txt') as myfile:
    txt = myfile.readline()
    translated =trns.translate(txt)
    print(translated)
    with open('app/test-ja.txt',mode='w', encoding='utf-8') as myfile2:
        myfile2.write(translated)

