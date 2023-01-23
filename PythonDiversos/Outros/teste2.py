import pyaudio as py#ouvir o microfone
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc


def NotasMusicais(valor,grafico):
    notas=[32.703196,
           34.647829,
           36.708096,
           38.890873,
           41.203445,
           43.653529,
           46.249303,
           48.999429,
           51.913087,
           55,
           58.27047,
           61.735413]
    oitavas=[0,1,2,3,4,5,6,7]
    
    if valor<notas[0] or valor>notas[11]*2**(oitavas[7]):
        grafico.set_title("Nota nenhuma")

    for y in range(0,len(oitavas)):
        nota=notas[0]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("C oitava",y+1)
            break

    for y in range(0,len(oitavas)):
        nota=notas[1]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("C# oitava",y+1)
            break

    for y in range(0,len(oitavas)):
        nota=notas[2]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("D oitava",y+1)
            break
    for y in range(0,len(oitavas)):
        nota=notas[3]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("D3 oitava",y+1)
            break
    for y in range(0,len(oitavas)):
        nota=notas[4]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("E oitava",y+1)
            break

    for y in range(0,len(oitavas)):
        nota=notas[5]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("F oitava",y+1)
            break

    for y in range(0,len(oitavas)):
        nota=notas[6]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("F# oitava",y+1)
            break

    for y in range(0,len(oitavas)):
        nota=notas[7]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("G oitava",y+1)
            break
    for y in range(0,len(oitavas)):
        nota=notas[8]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("G# oitava",y+1)
            break
    for y in range(0,len(oitavas)):
        nota=notas[9]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("A oitava",y+1)
            break
    for y in range(0,len(oitavas)):
        nota=notas[10]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("A# oitava",y+1)
            break
    for y in range(0,len(oitavas)):
        nota=notas[11]*2**(oitavas[y])
        if valor<=nota+nota*1.5 or valor>=nota-nota*1.5:
            grafico.set_title("B oitava",y+1)
            break

def Microfone():
    GRAFICO=True
    audio=py.PyAudio() #objeto audio
    microfone= audio.open(
        format=py.paFloat32,
        rate=44100,
        channels=1,
        frames_per_buffer=1024,
        input=True,
        output=True
        )


    fig,(ax1,ax2)=plt.subplots(2)
    dados_binarios=0
    dados_convertidos=0
    espectro_frequencia=0
    filtro=0
    fft_calculo=0
    modulo=0
    espectro_positivo=[]
    fig.show()

    
    while True:
        dados_binarios=microfone.read(1024)
        dados_convertidos=np.frombuffer(dados_binarios,np.float32)
    
        espectro_frequencia = np.fft.fftfreq(1024, 1 / 44100)
        for elemento in espectro_frequencia:
            if elemento>0:
                espectro_positivo.append(elemento)
        fft_calculo=np.fft.fft(dados_convertidos)
        modulo=abs(fft_calculo)[:int(1024//2)]
        
        
        if GRAFICO==True:
            grafico1, = ax1.plot(np.array(range(1024)),dados_convertidos)
            #graficos2, = ax2.plot(espectro_positivo, modulo)
            GRAFICO=False

            
        grafico1.set_ydata(dados_convertidos)
        #graficos2.set_ydata(modulo)
        
        fig.canvas.draw()
        fig.canvas.flush_events()
Microfone()
