from django.http import HttpResponse


a=list(input('enter a word: '))
b=list(reversed(a))
if a==b:
    print('equal')
else:
    print('not equal')

   

