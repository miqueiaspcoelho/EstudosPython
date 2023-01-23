from music21 import note, stream,metadata,meter,key,tempo

def Partitura(partitura,titulo,bpm):
    s=stream.Stream()
    s.insert(0,metadata.Metadata())
    s.metadata.title=titulo
    s.metadata.composer='Miquéias 2022'
    tm2 = tempo.MetronomeMark(number=bpm)
    s.insert(tm2)
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

    if doM.intersection(escala)==doM:
        return 'Escala de Dó maior'
    elif reM.intersection(escala)==reM:
        return 'Escala de Ré maior'
    elif miM.intersection(escala)==miM:
        return 'Escala de Mi maior'
    elif faM.intersection(escala)==faM:
        return 'Escala de Fá maior'
    elif solM.intersection(escala)==solM:
        return 'Escala de Sol maior'
    elif laM.intersection(escala)==laM:
        return 'Escala de Lá maior'
    elif siM.intersection(escala)==siM:
        return 'Escala de Si maior'
    
    elif doPenta.intersection(escala)==doPenta:
        return 'Escala de Pentatônica de Dó Maior'
    elif rePenta.intersection(escala)==rePenta:
        return 'Escala de Pentatônica de Ré Maior'
    elif miPenta.intersection(escala)==miPenta:
        return 'Escala de Pentatônica de Mi Maior'
    elif faPenta.intersection(escala)==faPenta:
        return 'Escala de Pentatônica de Fá Maior'
    elif solPenta.intersection(escala)==solPenta:
        return 'Escala de Pentatônica de Sol Maior'
    elif laPenta.intersection(escala)==laPenta:
        return 'Escala de Pentatônica de Lá Maior'
    elif siPenta.intersection(escala)==siPenta:
        return 'Escala de Pentatônica de Si Maior'
    else:
        return 'Sem classificaçao'
    
a=['C','D','E','G','A','C']
titulo=ClassificaEscala(a)
s=Partitura(a,titulo,60)
s.show()


