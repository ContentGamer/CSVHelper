import main as cvs
import time

cvs.createNew("Rida", "Ialioune")
cvs.createNew("Abdlmjid", "Baco")
cvs.createNew("Alan", "Becker")
cvs.createNew("Hello", "Gay")
output = cvs.getCSVDataAsArray()
print(output)