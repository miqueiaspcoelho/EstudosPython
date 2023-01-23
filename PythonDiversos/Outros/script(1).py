import pyaudio
import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fftpk
from scipy.fft import fft, fftfreq
import control.matlab
import math
import warnings
import keyboard
from music21 import note, stream,metadata,meter,key,tempo

#para não exibir alguns avisos que estava aparecendo ao usar tf e lsim
warnings.filterwarnings('ignore', '.*return_x specified*', )
warnings.filterwarnings('ignore', '.*Non-zero initial condition given for*', )

def GravarAudio(tempo,nota):
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
    #time.sleep(1)
    print('Nota:',(nota+1))
    try:
        while abs(time.time()- start_time)<=seconds:
          data=stream.read(1024,exception_on_overflow = False)
          frames.append(data)
    except KeyboardInterrupt:
        pass

    #transformando para frames
    frames=b''.join(frames)
    data=np.frombuffer(frames,dtype=np.int16)
    stream.stop_stream()
    
    #fechando o audio
    stream.close()
    
    #finalizando o objeto de audio
    audio.terminate()
    return data


def TransformadaFourier(data):
    FFT=abs(fft(data))#transformada e modulo

    freqs=fftpk.fftfreq(len(FFT),(1.0/44100))#frequencia
    freqs=freqs[:(len(freqs)//2)]#parte positiva

    FFT=FFT[0:(len(FFT)//2)]#parte positiva
    return freqs,FFT

def FiltroPassaAlta(data):
    tam=len(data)
    #Condições iniciais
    fc=90
    C=1
    R=(1/(2*math.pi*C*fc))
    tau=R*C
    y0=[[0]] # ordem no código é: y'[0] e depois y[0] /  nesse exemplo  y'[0]=0 e y[0]=2
    
    tempo =np.linspace(0,(len(data)/44100),len(data))

    #Função de transferência, sRC/sRC+1
    num_ft=[tau,0]
    den_ft=[tau,1]
    func_trans=control.matlab.tf(num_ft, den_ft)
    #Simulação usando a função lsim
    yout, t, xout = control.matlab.lsim(func_trans, data, tempo, y0)
    return yout


def FiltroPassaBaixa(data):
    tam=len(data)
    #Condições iniciais
    w0=800
    y0=[[0]] # ordem no código é: y'[0] e depois y[0] /  nesse exemplo  y'[0]=0 e y[0]=2
    
    tempo =np.linspace(0,(len(data)/44100),len(data))

    #Função de transferência, w0/s+w0
    num_ft=[0,w0]
    den_ft=[1,w0]
    func_trans=control.matlab.tf(num_ft, den_ft)
    #Simulação usando a função lsim
    yout, t, xout = control.matlab.lsim(func_trans, data, tempo, y0)
    return yout

def OitavaP3(nota):
    p=[
        130,138,146,155,
        164,174,184,195,
        207,220,233,245 
        ]
    if nota>=p[0] and nota<p[1]:
        return('C')
        
    elif nota>=p[1] and nota<p[2]:
        return('C#')
    
    elif nota>=p[2] and nota<p[3]:
        return('D')
    
    elif nota>=p[3] and nota<p[4]:
        return('D#')
    
    elif nota>=p[4] and nota<p[5]:
        return('E')
    
    elif nota>=p[5] and nota<p[6]:
        return('F')
    
    elif nota>=p[6] and nota<p[7]:
        return('F#')        
    
    elif nota>=p[7] and nota<p[8]:
        return('G')
    
    elif nota>=p[8] and nota<p[9]:
        return('G#')
    
    elif nota>=p[9] and nota<p[10]:
        return('A')
    
    elif nota>=p[10] and nota<p[11]:
        return('A#')
    
    elif nota>=p[11]:
        return('B')
    
def OitavaP4(nota):
    p=[
        260,277,293,311,
        329,349,369,391,
        415,440,466,493
        ]        

    if nota>=p[0] and nota<p[1]:
        return('C')
        
    elif nota>=p[1] and nota<p[2]:
        return('C#')
    
    elif nota>=p[2] and nota<p[3]:
        return('D')
    
    elif nota>=p[3] and nota<p[4]:
        return('D#')
    
    elif nota>=p[4] and nota<p[5]:
        return('E')
    
    elif nota>=p[5] and nota<p[6]:
        return('F')
    
    elif nota>=p[6] and nota<p[7]:
        return('F#')        
    
    elif nota>=p[7] and nota<p[8]:
        return('G')
    
    elif nota>=p[8] and nota<p[9]:
        return('G#')
    
    elif nota>=p[9] and nota<p[10]:
        return('A')
    
    elif nota>=p[10] and nota<p[11]:
        return('A#')
    
    elif nota>=p[11]:
        return('B')
    
def Classificador(valor):
    if valor<130 or valor>523:
        pass   
    else:
        if valor>=130 and valor <260:
            return OitavaP3(valor)
        elif valor>=260 and valor<=523:
            return OitavaP4(valor)

def Tempo(n):
    return round(((n/60)**-1),1)

def Partitura(partitura,titulo):
    s=stream.Stream()
    s.insert(0,metadata.Metadata())
    s.metadata.title=titulo
    s.metadata.composer='Miquéias 2022'
    for elemento in partitura:
        s.append(note.Note(elemento))
    return s

def ClassificaEscala(escala):
    
    doM={'C','D','E','F','G','A','B'}
    solM={'G','A','B','C','D','E','F#'}
    reM={'D','E','F#','G','A','B','C#'}
    laM={'A','B','C#','D','E','F#','G#'}
    miM={'E','F#','G#','A','B','C#','D#'}
    siM={'B','C#','D#','E','F#','G#','A#'}
    faM={'F','G','A','A#','C','D','E'}

    doPenta={'C','D','E','G','A'}
    rePenta={'D','E','F#','A','B'}
    miPenta={'E','F#','G#','B','C#'}
    faPenta={'F','G','A','C','D'}
    solPenta={'G','A','B','D','E'}
    laPenta={'A','B','C#','E','F#'}
    siPenta={'B','C#','D#','F#','G#'}

    if doM == (set(escala)):
        return 'Escala de Dó maior'
    elif reM == (set(escala)):
        return 'Escala de Ré maior'
    elif miM == (set(escala)):
        return 'Escala de Mi maior'
    elif faM == (set(escala)):
        return 'Escala de Fá maior'
    elif solM == (set(escala)):
        return 'Escala de Sol maior'
    elif laM == (set(escala)):
        return 'Escala de Lá maior'
    elif siM == (set(escala)):
        return 'Escala de Si maior'
    
    elif doPenta == (set(escala)):
        return 'Escala Pentatônica de Dó Maior'
    elif rePenta == (set(escala)):
        return 'Escala Pentatônica de Ré Maior'
    elif miPenta == (set(escala)):
        return 'Escala Pentatônica de Mi Maior'
    elif faPenta == (set(escala)):
        return 'Escala Pentatônica de Fá Maior'
    elif solPenta == (set(escala)):
        return 'Escala Pentatônica de Sol Maior'
    elif laPenta == (set(escala)):
        return 'Escala Pentatônica de Lá Maior'
    elif siPenta == (set(escala)):
        return 'Escala Pentatônica de Si Maior'
    else:
        return 'Notas'
    
bpm=int(input('BMP da música:'))
bpm=int(bpm*2)
tempo=Tempo(bpm)
data=0
partitura=[]
faudio=0
tf2=0
freqs1=0
FFT1=0
notaCF=0
a=0
i=0
parada=False
time.sleep(3)
while True:
    if keyboard.is_pressed('p'):
        parada=True
        break
    else:
        tempo=Tempo(bpm)
        data=GravarAudio(tempo,i)
        faudio=FiltroPassaAlta(data) #aplicando filtro no audio original
        faudio=FiltroPassaBaixa(faudio) #aplicando filtro no audio original
        tf2=TransformadaFourier(faudio) #transformada sobre o audio com filtro
        freqs1=tf2[0] #frequências
        FFT1=tf2[1] #módulo da transformada
        notaCF=freqs1[np.argmax(FFT1)] #frequência de pico
        a=Classificador(notaCF) #classificando a nota
        if a!=None:
            partitura.append(a)
        i+=1

print(partitura)
titulo=ClassificaEscala(partitura)
s=Partitura(partitura,titulo)
plt.semilogx(freqs1,FFT1)
a=partitura[-1]
plt.title(a)
plt.show()
s.show()

'''
Instalar music21:
https://www.youtube.com/watch?v=vN11f0qGNHU

Documentação da mesma:
https://web.mit.edu/music21/doc/

Projeto de inspiração:
http://repositorio.unesc.net/bitstream/1/8858/1/Guilherme%20de%20Nez%20Silvano.pdf

https://stringfixer.com/pt/Lowpass_filter
'''
