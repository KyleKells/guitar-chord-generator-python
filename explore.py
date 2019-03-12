


def getNotes(rootNote):
    musicalAlphabet = ['An','A#','Bn','Cn','C#','Dn','D#','En','Fn','F#','Gn','G#']
    notesInChord = []
    notesInChord.append(rootNote)
    #Major 3rd
    if musicalAlphabet.index(rootNote) + 4 < 12:
        notesInChord.append(musicalAlphabet[(musicalAlphabet.index(rootNote) + 4)])
    else:
        notesInChord.append(musicalAlphabet[(musicalAlphabet.index(rootNote) - 8)])
    #Perfect 5th    
    if musicalAlphabet.index(rootNote) + 7 < 12:
        notesInChord.append(musicalAlphabet[(musicalAlphabet.index(rootNote) + 7)])
    else:
        notesInChord.append(musicalAlphabet[(musicalAlphabet.index(rootNote) - 5)])
    return notesInChord


def createDiagram(notesInChord):
    noteLocations = open("notelocations.txt")
    noteLocations = noteLocations.readlines()
    w, h = 6, 4;
    fretList = [['-' for x in range(w)] for y in range(h)]
    hitList = [0,0,0,0,0,0]
    i = 0
    j = 1
    k = 0
    while j <= 16:
        while i < 4:
            if noteLocations[i][j:j+2] in notesInChord and hitList[k]== 0:
                fretList[i][k] = 'x'
                hitList[k] = 1
            i+=1
        i = 0
        j+=3
        k+=1
    return fretList

def printDiagram(diagram):
    print(" Key:","\n","Open strings","\n","First Fret","\n","First Fret","\n","Second Fret","\n","Third Fret","\n")
    for i in range(4):
        for j in diagram[i]:
            print(j,end='')
        print()

userInput = input("Enter the root note of the chord you would like to see")

printDiagram(createDiagram(getNotes(userInput)))
