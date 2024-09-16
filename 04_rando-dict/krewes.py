#Evan Chan
# The Flying Mice
# SoftDev
#K04 -- Python dictionairies and random selection
#2024-09-14
#time spent: .3 hours

import random as r
krewes = {
           4: [
'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
],
           5: [
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN'
              ]
           }

def randomDevo():
    period = r.randint(4,5)
    return r.choice(krewes[period])

print(randomDevo())


