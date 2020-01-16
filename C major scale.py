#Running this program plays a C major scale, with only a single note frequency(A4) as a reference.

import winsound

#Sets the standard tuning frequency
A4=440

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

#Sets self[x].pitch to the correct frequency relative to A4
class Notes():
    def __init__(self,steps):
        self.pitch=round(A4 * (2**(1/12))**(steps))

#Creates 8 octaves and assigns attribute 'pitch'
def Note(note,steps):
    for i in range(9):
        note.append(i)
        note[i]=Notes((steps+((i-5)*12)))
    return note

#Plays a note in any octave at a specific pitch
def play(note,octave):
    winsound.Beep(note[octave].pitch,200)

#Creates the following pitches based on their distance from A4
A=Note(A,0)
B=Note(B,2)
C=Note(C,3)
D=Note(D,5)
E=Note(E,7)
F=Note(F,8)
G=Note(G,10)

#Plays a C major scale
def cmaj():
    play(C,4)
    play(D,4)
    play(E,4)
    play(F,4)
    play(G,4)
    play(A,5)
    play(B,5)
    play(C,5)

#Runs code that plays C major scale
cmaj()
