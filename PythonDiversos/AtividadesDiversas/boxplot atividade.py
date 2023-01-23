import matplotlib.pyplot as plt
frequencia=[
6,32,99,168,297,420,625,803,958,
1037,1129,1091,1005,764,617,459,
242,153,55,37,3]
plt.boxplot(frequencia)
plt.ylabel('Ocorrências de cada soma')
plt.title('Frequência de cada soma')
plt.show()
