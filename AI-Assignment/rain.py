file_name = open('rainfall.csv','r')
List = []
for e in file_name:
    n_str = f.split() 
    num = [str(n) for n in n_str] 
    List.append(num) 
   
print(List)    