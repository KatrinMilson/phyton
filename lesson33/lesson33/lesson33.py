# coding=windows-1251


#f = open(r'C:\Users\satoa\OneDrive\������� ����\phyton\lesson33\File.txt', 'r')
#text = f.read(2)
#text2 = f.read(8)
#text = f.read()
#f.close()
#print(text)
#print(text2)

f = open(r'C:\Users\satoa\OneDrive\������� ����\phyton\lesson33\File.txt', 'a')

f.write('����� ������\n')
f.close()


lines = ['����� ������ 1', '����� ������ 2']
f = open(r'C:\Users\satoa\OneDrive\������� ����\phyton\lesson33\File.txt', 'a')
#for i in lines:
#     f.write(i + '\n')

# f.writelines(lines) #bez probelov
f.writelines(f'{i}\n' for i in lines) #s perenosom
f.close()

f = open(r'C:\Users\satoa\OneDrive\������� ����\phyton\lesson33\File.txt', 'r')

for line in f:
     print(line, end='')
f.close()
