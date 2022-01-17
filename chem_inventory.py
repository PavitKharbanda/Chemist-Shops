import math
from datetime import datetime
import pickle


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
cor=current_time[:2]
corr=int(cor)
#D={1:(-1,2),2:(0,1),3:(0,2),4:(0,3),5:(0,4),6:(0,5),12:(1,0),11:(1,1),10:(1,2),9:(1,3),8:(1,4),7:(1,5),26:(1,6),14:(2,0),15:(2,1),16:(2,2),17:(2,3),18:(2,4),19:(2,5),27:(2,6),28:(2,7),25:(3,0),24:(3,1),23:(3,2),22:(3,3),21:(3,4),20:(3,5),30:(3,6),29:(3,7),38:(4,0),37:(4,1),36:(4,2),35:(4,3),34:(4,4),33:(4,5),32:(4,6),31:(4,7),39:(5,0),40:(5,1),41:(5,2),42:(5,3),43:(5,4),44:(5,5),45:(5,6),46:(5,7),47:(5,8),56:(6,0),55:(6,1),54:(6,2),53:(6,3),52:(6,4),51:(6,5),50:(6,6),49:(6,7),48:(6,8),61:(7,4),63:(7,6)}

def makefile():
    
    
    filout=open('data.dat','wb')
    L=[['chem1',  (43.7611716,-79.4767811),(10,23) ,{'med1': 127, 'med2': 457, 'med3': 700, 'med4': 146, 'med5': 209},1234],
    ['chem2',  (43.6677445,-79.7422621),(12,24) ,{'med1': 15, 'med2': 542, 'med3': 406, 'med4': 43, 'med5': 56},5678],
    ['chem3',  (43.7548651,-79.497116),(9,16) ,{'med1': 7, 'med2': 227, 'med3': 262, 'med4': 319, 'med5': 402},1111],
    ['chem4',  (43.6783178,-79.7363944),(7,24) ,{'med1': 312, 'med2': 168, 'med3': 503, 'med4': 240, 'med5': 378},2222],
    ['chem5',  (43.7542684,-79.5357925),(9,18) ,{'med1': 49, 'med2': 371, 'med3': 546, 'med4': 172, 'med5': 348},3333],
    ['chem6', (43.6652578,-79.4826807),(9,20) ,{'med1': 176, 'med2': 175, 'med3': 735, 'med4': 14, 'med5': 344},4444],
    ['chem7', (60.668583,-79.4047437),(8,23) ,{'med1': 469, 'med2': 362, 'med3': 516, 'med4': 92, 'med5': 135},5555],
    ['chem8',  (43.722151,-79.7074587),(9,24) ,{'med1': 191, 'med2': 418, 'med3': 180, 'med4': 45, 'med5': 102},6666],
    ['chem9', (43.7347996,-79.4283606),(9,17) ,{'med1': 83, 'med2': 552, 'med3': 656, 'med4': 242, 'med5': 315},7777],
    ['chem10', (43.6825061,-79.4294203),(9,15),{'med1': 200, 'med2': 289, 'med3': 182, 'med4': 32, 'med5': 317},8888],
    ['chem11', (43.678317,-79.7363937),(4,11),{'med1': 281, 'med2': 269, 'med3': 630, 'med4': 182, 'med5': 327},9999],
    ['chem12', (43.678317,-79.7363937),(11,22),{'med1': 390, 'med2': 235, 'med3': 913, 'med4': 193, 'med5': 379},1999]]
    pickle.dump(L,filout)
    filout.close()
    
  

def search(L):  
    
    
      L1=[]
      M=input("Enter the name of the medicine that you want: ")
      while M not in ["med1", "med2", "med3", "med4", "med5"]:
          print("invalid name")
          M=input("Enter the name of the medicine that you want: ")
         
          
      Q=int(input("Enter the quantity of the medicine that you want : "))
    
      for i in L:
        
        if i[3][M.lower()]>=Q:
            
            if corr>=i[2][0] and corr<i[2][1]:   
                
                L1.append(i)                      
      s=eval(input("Enter current latitude and Longitude (in degrees, (lat,lon)) : "))
      fl=dcomp(L1,s)
      
      return fl
  
def verify(L,N,count=1):
 
  pas=int(input('Enter your password : '))
  
  for i in L:
      
      if i[0]==N.lower():
          
          if i[4]==pas:
              update(L,N)
              
          elif count<3:
              
              count+=1
              print('''\033[0;31;40mIncorrect password!! Try again,Number of tries
                    left : ''',4-count,'''\033[0m''')
              verify(L,N,count)
              
          else:
              
              print('\033[0;31;40mToo many incorrect passwords,Login attempt failed\033[0m')
              break
          
            
def dcomp(lstofalchem,su):
   
    for x in lstofalchem:
        R = 6373.0
        s=x[1]
        dlat=math.radians(s[0])-math.radians(su[0])
        dlon=math.radians(s[1])-math.radians(su[1])
        
        a = math.sin(dlat / 2)**2 + math.cos(math.radians(su[0])) * math.cos(math.radians(s[0])) * math.sin(dlon / 2)**2
    
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c       
        x.append(distance)
        
    lstofalchem=dsort(lstofalchem)  
    
    return(lstofalchem)
   
def dsort(lstofallchem):
    
    for a in range(0,len(lstofallchem)):       
        for x in range(1,len(lstofallchem)):
            
         if lstofallchem[x-1][5]>lstofallchem[x][5]:
                
          lstofallchem[x-1],lstofallchem[x]=lstofallchem[x],lstofallchem[x-1]
              
    return lstofallchem

def update(L,N):
  
    change="S"
    print("\n\033[36mHere are the details of your account : ")
    print()
    for y in L:
        
        if y[0]==N.lower():
            
            print(y[3],'\033[0m')
            lis=y
                
    while change.upper() in "SB":
                 
        change=input('''If you want to make a change: Enter 'S' if you have sold
                     an item; 'B' if you have got some new stock; Else press any 
                     key : ''')
    
        if change=="S" or change=='s':
    
            M=input("Enter the name of the medecine you have sold : ")
            Q=int(input("Enter the quantity of the medicine sold : "))   
            lis[3][M]-=Q
                          
        elif change=="B" or change=='b':
    
            M=input("Enter the name of the medecine that has been restocked : ")
            Q=int(input("Enter the quantity of the medicine that has been restocked : "))   
            lis[3][M]+=Q
                 
        else :
            
             print("\n\033[36mUpdated record : \n\n", lis[3],'\033[0m')
             print("\nUpdation Completed!!")
                       
    binary(L)

def binary(L):
    
    filout=open('data.dat','wb')
    pickle.dump(L,filout)
    filout.close()

def dtmak():
    
    filout=open('data.dat','rb')
    
    try:      
        
        while True:           
            L=pickle.load(filout)

    except EOFError:      
        filout.close()

    return L
                 
#main
    
print("\t\t\t CHEMIST FINDER")
m=input("Create file(M)/Use file(U) : ")
if m.upper()=="M":
    
    makefile()
    print("File successfully created")
    
elif m.upper()=="U":    
   
    choose=input('''If you are a customer (press a)
If you are a chemist (press b) : ''')
    print()
    L=dtmak()
    
    if choose.upper()=='B':
        
        N=input("Enter the Name of your chemist shop : ")
        verify(L,N.lower())
        
    elif choose.upper()=='A':
        
        print("Available medicines are : med1, med2, med3, med4, med5")    
        lis=search(L)
        print("\n\033[36mName of chemists with available medicines from nearest to farthest : \033[0m")
        for x in lis:     
                                   
            print("\n\033[36mChemist name : ",x[0])
            print("Latitudes and longitudes of the chemist shop : ",x[1])
            print("Chemist opening and closing time is : ",x[2],'\n\033[0m')
                
    else:
        
       print("Invalid choice!!")    
            
else:
    
    print("Invalid choice!!")

