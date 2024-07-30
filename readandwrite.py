fr =open('simple.txt','r')
fr.read('hello world\n')
fr.read("shivrajbsdk")
fr.read('muthi man')
fr.close

fw=open('simple.txt','w')
text=fr.read()
print(text)
fr.close
