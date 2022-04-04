#hash
dic = {'a':"^#1!",'A':"^#2!",'e':"o3@",'E':"o4@",'ı':"6d6",'I':"7d6",'u':'S2>3x','U':'S3>3x','i':"/m+%",'İ':"/m+%1",'o':"7k+=",'O':"8k+=",'ç':"p*1?",'Ç':"p*2?",'ö':"f-+*!",'Ö':"f-+*!1",'b':",^^#fa",'B':",^^#fB",'d':"35qh",'D':"35qH",'q':"5s9%",'Q':"5S9%",'c':"*#6s",'C':"*#6S",'g':"o0*",'G':"O0*",'p':"£sfa/",'P':"£sfA/",'f':"#*9",'F':"#*0",'k':"#5o",'K':"#8o",'l':"fg3",'L':"fg4",'h':"3y2f",'H':"3Y2f",'t':"gh234",'T':"gh235",'v':"&6%2",'V':"&6%3",'z':"?=7",'Z':"?=8",'y':"fd243",'Y':"FD442",'w':"/&^+",'W':"/&U^+",'x':"/fsa",'X':"/fS3a",'m':"=*½",'M':"=*M½",'n':"^!&jg",'N':"^!&JG",'j':"k&42",'J':"K&42",'r':"1*=",'R':"1c*=",'s':"/&f3",'S':"/&gf3",'0':'K00O3','1':'A^Y^','2':'{½+}','3':'ı#2F','4':'N7g','5':'0V8','6':'21x&','7':'+/*6','8':'s-n','9':'31'}
dic2 = {}
for key,value in dic.items():
    dic2[value] = key
def hash_maker(password):
    lilPassword = password
  
    myHash = []
    finishedHash = ""
    for i in lilPassword:
        for j in dic:
            if i == j:
                myHash.append(dic[j])
            else:
                continue
    for i in range(len(myHash)):
        finishedHash += myHash[i]            
    return finishedHash   
 

def hash_solver(finishedHash):
    tempString = ""
    imgPassword = ""
    for i in finishedHash:
        tempString += i
        for j in dic2:
            if tempString == j:
                x = dic2.get(tempString)
                imgPassword += x
                tempString = ""
            else:
                continue
    return imgPassword                            

print(hash_maker('Merhaba58'))               
print(hash_solver(hash_maker('Merhaba58')))