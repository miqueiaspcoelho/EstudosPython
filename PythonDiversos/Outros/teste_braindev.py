#ranqueando um array com posições de chegada e se empate considera mesma posição para quem empatou
def rank(arr):
    if len(arr) > 0:
        array_orderned_list  = sorted(arr,reverse = True)
        array_orderned_list_adjust = []
        array_final = []
        i = 0
        last_item = False
        for x in array_orderned_list:
            if x != last_item:
                last_item = x
                i+=1
                array_orderned_list_adjust.append([x,i])
        for i in range(0,len(arr)):
            for j in range(0,len(array_orderned_list_adjust)):
                if (arr[i] == array_orderned_list_adjust[j][0]):
                    array_final.append(array_orderned_list_adjust[j][1])
        return array_final
    pass
#b = [int(x) for x in input('Lista: ').strip().split(',')]
#a = rank(b)
#print(a)

#ordenada uma string em ordem afabética
def orderned_alpha(string):
    return "".join(sorted(string.lower()))
a = "ASDAEFVSDUBvnusrnvui"
# b = orderned_alpha(a)
# print(b)
#conta quantos ips existem dentro de uma faixa de ip qualquer
# \(N = (Primeiro \times 256^3) + (Segundo \times 256^2) + (Terceiro \times 256^1) + Quarto\)
def count_ip(init_ip, end_ip):
    def convert_ip(ip):
        ip_list_convert = [int(x) for x in ip.strip().split('.')]
        print(ip_list_convert)
        tam = len(ip_list_convert)
        s = sum((ip_list_convert[(tam - i - 1)]*256**i) for i in range(0,tam))
        print(s)
        return s
    init_ip_convert = convert_ip(init_ip)
    end_ip_convert = convert_ip(end_ip)
    ip_total = abs(end_ip_convert - init_ip_convert) + 1
    return ip_total


a = '192.168.0.1' #3232235521
b = '192.168.1.100'
c = count_ip(a,b)
print(c) 