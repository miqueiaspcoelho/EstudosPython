from typing_extensions import Required
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
import pyaudio

# PARAMETROS

# https://dsp.stackexchange.com/questions/13728/what-are-chunks-when-recording-a-voice-signal


def configurarGrafico():
    fig, (ax1,ax2) = plt.subplots(2)
    fig.tight_layout() 
    fig.canvas.set_window_title('Transformada de Fourier - ATV')
    ax1.set_ylim(-0.5, 0.5)
    ax1.set_xlabel('Tempo (t)')
    ax1.set_ylabel('Amplitude')
    ax2.set_ylim(0, 1)
    ax2.set_xlabel('Frequência (Hz)')
    ax2.set_ylabel('Módulo')
    return fig, ax1, ax2


def setNota(index, x_espectro, ax1):
    # Foi utilizado um intervalo para + 7 do informado da tabela
    # Para fins de simplificação, foi considerado que entre o intervalo anterior
    # Até o máximo do próximo correspondia a uma nota.
    # https://bit.ly/32eh4Mx
    frequencia = x_espectro[index]
    if frequencia < 256 or frequencia > 500:
        ax1.set_title("")
    elif frequencia >= 256 and frequencia <= 268:
        ax1.set_title("A nota tocada é : C")
    elif frequencia <= 284:
        ax1.set_title("A nota tocada é : C#")
    elif frequencia <= 300:
        ax1.set_title("A nota tocada é : D")
    elif frequencia <= 320:
        ax1.set_title("A nota tocada é : D#")
    elif frequencia <= 337:
        ax1.set_title("A nota tocada é : E")
    elif frequencia <= 376:
        ax1.set_title("A nota tocada é : F#")
    elif frequencia <= 398:
        ax1.set_title("A nota tocada é : G")
    elif frequencia <= 422:
        ax1.set_title("A nota tocada é : G#")
    elif frequencia <= 447:
        ax1.set_title("A nota tocada é : A")
    elif frequencia <= 473:
        ax1.set_title("A nota tocada é : A#")
    elif frequencia <= 500:
        ax1.set_title("A nota tocada é : B")


def audio(chunk, rate, canal, formato):
    py_audio = pyaudio.PyAudio()
    mic = py_audio.open(rate=rate, format=formato, channels=canal, 
                        frames_per_buffer=chunk, input=True, output=True)
    config = True
    fig, ax1,ax2 = configurarGrafico()

    while True:
        amostra_bytes = mic.read(chunk)
        amostra = np.frombuffer(amostra_bytes, np.float32)

        x_espectro = fftfreq(chunk, 1 / rate)[:chunk//2] # Pegando só o espectro positivo
        y_f =  fft(amostra) # Fazendo a transformada
        y_abs =  abs(y_f/(chunk//10))[:chunk//2] # Pegando os valores reais x imaginarios e tirando o módulo
        if config:
            # SERVE SÓ PRA INICIALIZAÇÃO
            plot_1, = ax1.plot(np.array(range(chunk)), amostra)
            plot_2, = ax2.plot(x_espectro, y_abs)
            config = False

        plot_1.set_ydata(amostra)
        plot_2.set_ydata(y_abs)

        # SETANDO INTERVALOS
        req_index=np.argmax(y_abs)
        setNota(req_index, x_espectro, ax1)
        
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.5)


chunk = 1024
rate = 44000 # é a "taxa de amostragem", ou seja, o número de quadros por segundo
canal = 1 # tipo a quantidade de amostras, nesse caso 1
formato = pyaudio.paFloat32 # Ficou a melhor configuração, ver mais sobre isso

audio(chunk, rate, canal, formato)




# links refer~encia
#https://www.delftstack.com/pt/api/numpy/python-numpy-argmax/#:~:text=Podemos%20tamb%C3%A9m%20encontrar%20o%20maior,que%20aparece%20primeiro%20no%20array.
# https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html
# TERIA QUE GRAVAR POR 5 SEGUNDOS, mas tive problemas
# https://realpython.com/playing-and-recording-sound-python/ 
# PLOTAR EM TEMPO REAL
# https://youtu.be/AShHJdSIxkY
