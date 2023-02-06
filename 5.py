#participants_list = [
#  ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
  #  ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
   # ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
   # ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
   # ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
  #  ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
    #]
#print("daily_participants---------")
#daily_participants(participants_list) # ['Desmond', 'Krish', 'Sam']
#print("one_time_participants---------")
#one_time_participants(participants_list)# ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
#print("first_day_only_participants----------------")
#first_day_only_participants(participants_list) #  ['John', 'Joan']

from collections  import Counter
def daily_participants(participants_list):
    dic = {}
    l = []
    a = []
    for i in range(len(participants_list)):
        l.append(0)
    for i in range(len(participants_list)):
        for j in range(len(participants_list[i])):
            if participants_list[i][j] not in dic:
                dic[participants_list[i][j]] = 0

    for name in dic:
        flag = 0
        for i in range(len(participants_list)):
            if name not in participants_list[i]:
                flag = 1
        if flag == 0:
            a.append(name)

    return a
def one_time_participants(participants_list):
  all=participants_list[0:]
  b=[]
  c=[]
  for list in participants_list[0:]:
   for element in list:
      b.append(element)
  dictOfElems = dict(Counter(b))

  dictOfElems = { key:value for key, value in dictOfElems.items() if value== 1}
  for key, value in dictOfElems.items():
    final=[]
    final.append(key)
    print(final,end="")

def first_day_only_participants(participants_list):
    firstlist=participants_list[0]
    lastlist=participants_list[1:]
    all=participants_list[0:]


    b=[]
    c=[]

    for list in participants_list[:1]:


      for element in list:
        b.append(element)
    for list in participants_list[1:]:


      for element in list:
        c.append(element)    

    for i in range(0,len(b)):
      if b[i] not in c:
        
        an=[]
        an.append(b[i])
        print(an,end=" ")
        
        
participants_list = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
    ]
print("daily_participants---------")
daily_participants(participants_list) # ['Desmond', 'Krish', 'Sam']
print("\n")
print("one_time_participants---------") 
one_time_participants(participants_list)# ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
print("\n")
print("first_day_only_participants----------------")
first_day_only_participants(participants_list) #  ['John', 'Joan']

