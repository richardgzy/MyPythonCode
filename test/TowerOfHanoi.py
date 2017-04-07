'''
Created on Feb 4, 2017

@author: Richard's Surface
'''
import time

def movePiece (pieceNumber, startNeedle, endNeedle, temp):
    if (pieceNumber == 1):
        return 1;
    else:
        return movePiece(pieceNumber - 1, "startNeedle", "temp", "endNeedle") + movePiece(pieceNumber - 1, "temp", "endNeedle", "startNeedle") + 1;

start = time.time()       
print(movePiece(3, "startNeedle", "temp", "endNeedle"))
end = time.time()
print("time: %.10f " % (end - start))