import pyaudio
import wave
import time
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpk
from scipy.fft import fft, fftfreq
import control.matlab
import math

'''1)Gravar audio (ok) - Transformada de Fourier (ok) - Classificar nota (ok) - Plotar Gráfico (ok)'''

'''2)Gravar audio (ok) - Passar pelo filtro passa alta - Transformada de Fourier - Classificar nota - Plotar Gráfico'''

#função gravar audio()
def GravarAudio(tempo):
    #Objeto de audio
    audio = pyaudio.PyAudio()

    #Configuraçoes da gravaçao
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        frames_per_buffer=1024,
        output=True
        )

    #gravando microfone
    data=0
    frames=[]
    seconds=tempo
    start_time=time.time()
    print('Inicio da gravação')
    try:
        while abs(time.time()- start_time)<=seconds:
          data=stream.read(1024)
          frames.append(data)
    except KeyboardInterrupt:
        pass
    print('Fim da gravação')

    #parando gravaçao
    stream.stop_stream()

    #fechando o audio
    stream.close()

    #finalizando o objeto de audio
    audio.terminate()

    #salvando audio em wav
    sound_file=wave.open("audio.wav", "wb")

    #salvando em mono
    sound_file.setnchannels(1)

    #largura de banda
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))

    #taxa de amostragem por segundo
    sound_file.setframerate(44100)

    #juntando os bytes pra fazer um só arquivo
    sound_file.writeframes(b''.join(frames))

    #open the wav file
    wave_file=wave.open("audio.wav", "r")

    #O -1 pega todos os frames
    raw_file=wave_file.readframes(-1)

    #convertendo para array para plotar
    raw_file=np.frombuffer(raw_file,np.int16)

    #eixo x em segundos
    sampleRate = wave_file.getframerate()
    x=np.linspace(0,(len(raw_file)/sampleRate),len(raw_file))
    print('Concluído com sucesso')
    return x,raw_file

#função plotar gráfico()
def DefineGrafico():
    fig, (plot1,plot2) = plt.subplots(2)

    #plot1.set_title('Sem o filtro')
    #plot1.set_xlabel('tempo')
    plot1.set_ylabel('amplitude')
    plot1.set_xlim(20,1000)

    #plot2.set_title('Com o filtro')
    #plot2.set_xlabel('frequência')
    plot2.set_ylabel('|amplitude|')
    plot2.set_xlim(20,1000)
    
    return fig,plot1,plot2

#função transformada de fourier()
def TransformadaFourier():
    #abre, lé e faz a transformada no sinal de audio
    s_rate, signal = wavfile.read("audio.wav")

    FFT=abs(fft(signal))#transformada e modulo

    freqs=fftpk.fftfreq(len(FFT),(1.0/s_rate))#frequencia
    freqs=freqs[:(len(freqs)//2)]#parte positiva

    
    FFT=FFT[0:(len(FFT)//2)]#parte positiva
    #FFT=FFT/max(FFT)#normalizando
    
    return freqs,FFT

#função classificando nota()
def Classificador(note,grafico):
    p=[
        int(261.625568),277.182632,293.664768,311.126984,
        329.62756,349.228232,369.994424,391.995432,
        415.304696,440,466.16376,523
        ]
    if note<p[0] or note>523:
        grafico.set_title('Fora do range')
        print('note:',note)
    elif note>=p[0] and note<p[1]:
        print('Dó')
        grafico.set_title('Dó')
        #return 1
    
    elif note>=p[1] and note<p[2]:
        print('Dó Sustenido/Ré bemol')
        grafico.set_title('Dó Sustenido/Ré bemol')
        #return 1.1
        
    elif note>=p[2] and note<p[3]:
        print('Ré')
        grafico.set_title('Ré')
        #return 2

    elif note>=p[3] and note<p[4]:
        print('Ré Sustenido/Mi bemol')
        grafico.set_title('Ré Sustenido/Mi bemol')
        #return 2.1
        
    elif note>=p[4] and note<p[5]:
        print('Mi')
        grafico.set_title('Mi')
        #return 3
    
    elif note>=p[5] and note<p[6]:
        print('Fá')
        grafico.set_title('Fá')
        #return 4
        
    elif note>=p[6] and note<p[7]:
        print('Fá Sustenido/Sol bemol')
        grafico.set_title('Fá Sustenido/Sol bemol')
        #return 4.1
    
    elif note>=p[7] and note<p[8]:
        print('Sol')
        grafico.set_title('Sol')

    elif note>=p[8] and note<p[9]:
        print('Sol Sustenido/Lá bemol')
        grafico.set_title('Sol Sustenido/Lá bemol')
        #return 5.1

    elif note>=p[9] and note<p[10]:
        print('Lá')
        grafico.set_title('Lá')
        #return 6
        
    elif note>=p[10] and note<p[11]:
        print('Lá Sustenido')
        grafico.set_title('Lá Sustenido')
        #return 6.1
    
    elif note>=p[11]:
        print('Si')
        grafico.set_title('Si')
        #return 7

#função filtro passa alta()
def Filtro(sinal,tamanhoSinal):
    #Condições iniciais
    fc=200
    C=1
    R=1/(2*math.pi*C*fc)
    tau=R*C
    y0=[[0]] # ordem no código é: y'[0] e depois y[0] /  nesse exemplo  y'[0]=0 e y[0]=2

    #Definições de tempo de simulação
    Tfinal=5; #Segundos
    DeltaT=Tfinal/tamanhoSinal #Passo
    Tfinal=Tfinal/DeltaT;
    tempo=list(range(0,int(Tfinal), 1))

    #Entrada, neste exemplo, sinal de audio
    #x=[]
    N=len(tempo)
    tempo = np.array(tempo)

    #Função de transferência, neste exemplo (massa-mola amortecedor): 1/(ms²+bs+k)
    num_ft=[tau,0]
    den_ft=[tau,1]
    func_trans=control.matlab.tf(num_ft, den_ft)
    #print(func_trans)
    #Simulação usando a função lsim
    yout, t, xout = control.matlab.lsim(func_trans, sinal, tempo, 0)
    return xout,yout

fig, plot1, plot2 = DefineGrafico()
audio=GravarAudio(5) #retorna x,raw_file
raw_file=audio[1]

transformadaAudioOriginal=TransformadaFourier() #retorna freqs,FFT

freqs=transformadaAudioOriginal[0]

FFT=transformadaAudioOriginal[1]
note1=freqs[np.argmax(FFT)]
print('Sem filtro, nota=',note1)
PLOT1, = plot1.plot(freqs,FFT) #gráfico da transformada do audio sem ser filtrado
Classificador(freqs[np.argmax(FFT)],plot1) #coloca o nome de acordo com a nota

s_rate, signal = wavfile.read("audio.wav")
tamanhoSinal=len(raw_file)
audioFiltrado=Filtro(signal,tamanhoSinal) # retorna xout e yout
xout=audioFiltrado[0]
yout=audioFiltrado[1]

FFT1=abs(fft(yout))#transformada e modulo

freqs1=fftpk.fftfreq(len(FFT1),(1.0/s_rate))#frequencia
freqs1=freqs1[:int(len(freqs1)/2)]#parte positiva    
FFT1=FFT1[0:int(len(FFT1)/2)]#parte positiva
FFT1=FFT1/max(FFT1)#normalizando

note2=freqs1[np.argmax(FFT1)]
print('Com filtro, nota=',note2)
PLOT2, = plot2.plot(freqs1,FFT1,'r') #gráfico da transformada do audio filtrado
Classificador(freqs1[np.argmax(FFT1)],plot2) #coloca o nome de acordo com a nota


plt.show()


