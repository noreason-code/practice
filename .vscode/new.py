filename = 'test.txt'
with open(filename,'a') as f_obj :
    f_obj.write("haha")
with open(filename,'r') as f_obj :
    mes = f_obj.read()
    print(mes)
