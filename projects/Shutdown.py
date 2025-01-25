def Shutdown():
    return('shuting down')
dtermine = (input('is chrome,system app , or any other app running (yes or no): '))
if dtermine == 'no':
    print('shutting down')
else:
    print('cant shut down unless apps closed')
Shutdown()     