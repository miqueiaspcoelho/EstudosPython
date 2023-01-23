import pyaudio
import numpy as np
from scipy.fft import fft, fftfreq
import time
import matplotlib.pyplot as plt

chunk = 1024 # Número de pontos lido no tempo
rate = 44000
seconds = 5
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=rate,input=True,
              frames_per_buffer=chunk, output=False)

def setNota(frequencia):
    # Foi utilizado um intervalo para + 7 do informado da tabela
    # Para fins de simplificação, foi considerado que entre o intervalo anterior
    # Até o máximo do próximo correspondia a uma nota.
    # https://bit.ly/32eh4Mx
    if frequencia < 258 or frequencia > 497:
        # APESAR DO ELSE, melhor adicionar aqui por questão de evitar os elif
        return None
    elif frequencia >= 258 and frequencia <= 266:
        return "C"
    elif frequencia >= 273 and frequencia <= 281:
        return "C#"
    elif frequencia >= 289 and frequencia <= 297:
        return "D"
    elif frequencia >= 307 and frequencia <= 315:
        return "D#"
    elif frequencia >= 325 and frequencia <= 333:
        return "E"
    elif frequencia >= 345 and frequencia <= 353:
        return "F"
    elif frequencia >= 365 and frequencia <= 373:
        return "#F"
    elif frequencia >= 387 and frequencia <= 394:
        return "G"
    elif frequencia >= 411 and frequencia <= 419:
        return "G#"
    elif frequencia >= 436 and frequencia <= 444:
        return "A"
    elif frequencia >= 462 and frequencia <= 470:
        return "A#"
    elif frequencia >= 489 and frequencia <= 497:
        return "B"
    else:
        return None


def configurarGrafico():
    fig, (ax1,ax2) = plt.subplots(2, figsize=(10, 6), dpi=100)
    fig.tight_layout(pad=3.0) 
    fig.suptitle('Transformada de Fourier - ATV')
    ax1.set_xlabel('Tempo (t)')
    ax1.set_ylabel('Amplitude')
    ax2.set_xlabel('Frequência (Hz)')
    ax2.set_ylabel('Módulo')
    return fig, ax1, ax2


fig, ax1,ax2 = configurarGrafico()
config = True

frames = []

print("Gravando")
time.sleep(1)
for i in range(0, int(rate / chunk * seconds)):
    data = stream.read(chunk, exception_on_overflow = False)
    frames.append(data)

print("Parando Gravação")

frames = b''.join(frames)
data = np.frombuffer(frames,dtype=np.int16)

N = 1/rate
T = len(data)
x = np.linspace(0, int(T * N) + 1, T)

# Sugestão no fórum foi aumentar a amplitude para melhor visualização dos picos
# De fato funcionou para visualização.
y_f = abs(fft(data)) ** 2

# Pegando o escpectro de x
x_espectro = fftfreq(len(y_f), N)
x_espectro = x_espectro[:int(len(x_espectro)/2)] # parte positiva

y_f = y_f[:int(len(y_f)/2)] # Limitando que nem o x_espectro
# Pegando só uma faixa de frequência para melhor visualização
faixa_freq = x_espectro < 600
x_espectro = x_espectro[faixa_freq]
y_f = y_f[faixa_freq]

# Tirando alguns ruídos, como frequência abaixo de 256 e acima de 550
ruido_menor_256 = x_espectro <= 256
y_f[ruido_menor_256] = 0
ruido_maior_550 = x_espectro >= 550
y_f[ruido_maior_550] = 0

valor_frequencia = x_espectro[np.argmax(y_f)]
#setNota(valor_frequencia)

# PLOTANDO
if config:
        # SERVE SÓ PRA INICIALIZAÇÃO
        plot_1, = ax1.plot(x, data)
        plot_2, = ax2.plot(x_espectro, y_f)
        config = False

plot_1.set_ydata(data)
plot_2.set_ydata(y_f)

# Pegando as 10 maiores amplitudes maiores
amplitudes = np.sort(y_f)
amplitudes = amplitudes[::-1][:12]
arcodes = set()
for x in amplitudes:
    idx = np.argwhere(y_f == x)
    try:
        freq = x_espectro[idx][0][0]
        print(freq)
        nota = setNota(freq)
        if nota != None:
            arcodes.add(nota)
    except:
        pass

fig.suptitle(f"ARCODES: {arcodes}" )
fig.canvas.draw()
fig.canvas.flush_events()
plt.show()
