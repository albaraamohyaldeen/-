from turtle import Screen
from range import Range
from box import Box
from writ import Writ
import random
window = Screen()
window.bgcolor('black')
window.setup(711,1255)
window.tracer(0)


wr1 = Writ((-321,409))
wr2 = Writ((-321,355))
wr3 = Writ((-321,301))
wr4 = Writ((-321,247))

bx1 = Box((121,425))
bx2 = Box((121,371))
bx3 = Box((121,317))
bx4 = Box((121,263))



ran_t = Range((0,515))
ran_t.shapesize(1,33.3)

ran_d = Range((0,-611))
ran_d.shapesize(1,33.3)

ran_r = Range((341,-55))
ran_r.shapesize(57.1,1)

ran_l = Range((-341,-55))
ran_l.shapesize(57.1,1)

window.update()

wr1.write('first name:',font= ('courier',9,'normal'))
wr2.write('last name:',font =('courier',9,'normal'))
wr3.write('number:',font = ('courier',9,'normal'))
wr4.write('email:',font = ('courier',9,'normal'))

fr_n = window.textinput('first name','enter first name')

num = [0,1,2,3,4,5,6,7,8,9]
while True:
 
 if fr_n == f'':
   #wr1.goto(-55,405)
   #wr1.write('this is correct', font = ('courier',9,'normal'))
   while True:
      fr_n = window.textinput('first name','name is correct\n enter first name')
      if fr_n != f'':
         
         wr1.goto(-85,405)
         wr1.write(f'{fr_n}',font = ('courier',9,'normal'))
         
         break
 else:
   wr1.goto(-85,405)
   wr1.write(f'{fr_n}',font = ('courier',9,'normal'))
   la_n = window.textinput('last name','enter last name')
   
   if la_n == f'' :
      
      while True:
        la_n = window.textinput('last name','name is correct\n enter first name')
        if la_n != f'':
         
         wr2.goto(-85,349)
         wr2.write(f'{la_n}',font = ('courier',9,'normal'))
         
         
         break
   else:
      wr2.goto(-85,349)
      wr2.write(f'{la_n}',font = ('courier',9,'normal'))
        
      number = window.textinput('number','enter mobile number')
      numint = int(number)
      crachters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q',
      'u','w','r','t','y','u','i','o','p','s','v','c','x','z')
      if range(numint) != 12:
         wr3.goto(-85,295)
         wr3.write('range is high',font = ('courier',9,'normal'))
         break
      
      if number == '' or number in crachters:
         wr3.goto(-85,295)
         wr3.write('this is not number', font = ('courier',9,'normal'))
         break
      
      else:
         wr3.goto(-85,295)
         wr3.write(f'{number}',font = ('courier',9,'normal'))
         witch = window.textinput('email','enter email(by_self/by_ai)')
         
   
         if witch == 'by_self':
 
            en_em = window.textinput('email','enter email(@,fr_n,la_n)')
 
            if "@" in en_em and fr_n in en_em and la_n in en_em:
               wr4.goto(-85,239)
               wr4.write(f'{en_em}' ,font=('courier',9,'normal'))
               wr4.goto(-321,203)
               wr4.write('sucesfully',font = ('courier',9,'normal'))
               break
 
            else:
      
               wr4.goto(-21,255)
               wr4.write('there is correct',font=('courier',9,'normal'))
               break
         
         elif witch == 'by_ai':
   
            syn = ('#','&','=','+','_')
            num = (1,2,3,4,5,6,7,8,9,0)
            crachters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q',
            'u','w','r','t','y','u','i','o','p','s','v','c','x','z')
  
            ra_car = random.choice(crachters)+random.choice(crachters)+random.choice(crachters)
            ra_num = random.choice(num)+random.choice(num)+random.choice(num)
            ra_syn = random.choice(syn)+random.choice(syn)+random.choice(syn)
            emaill = (f'@{fr_n}{la_n}{ra_car}{ra_num}{ra_syn}')
  
            wr4.goto(-79,255)
            wr4.write(f'{emaill}' ,font = ('courier',7,'normal'))
            wr4.goto(-321,201)
            wr4.write('sucesfully' , font = ('courier',9,'normal'))
            break
      
         else:

            wr4.goto(-85,245)
            wr4.write('this is correct' ,font=('courier',9,'normal'))
            break
      
         
window.exitonclick()
