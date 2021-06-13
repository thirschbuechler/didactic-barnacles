
import matplotlib.pyplot as plt
plt.close("all")

a=plt.rcParams
print(a)
print(a["font.family"])
#font.family: ['sans-serif']


#plt.rcParams.update({'font.size': 22})#seems to work
#plt.rc('font', family='Helvetica')
plt.rcParams.update({'font.family': 'Helvetica'})
#findfont: Font family ['Helvetica'] not found. Falling back to DejaVu Sans.
#http://www.identifont.com/differences?first=Helvetica&second=DejaVu+Sans

plt.figure()
plt.title("Hello my Lady, Hello my Darling")
plt.show()

