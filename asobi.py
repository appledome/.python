print('名前を入力してください')

your_name = input('>> ')

print('こんにちは！ {} さん！'.format(your_name))

print("大阪府の文字数は" + str(len("大阪府")))

str1 = "福田　将士"
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])

print(str1[1:3])

name = "福田"
old = 40
ad = "大東市"
print("名前は{:<5s}です。年齢は{:>8d}歳になりました。{:^8s}に住んでいます".format(name,old,ad))
print("もう一回、名前は{myname}です。年齢は{myold}才になりました".format(myname="福田",myold=40))
