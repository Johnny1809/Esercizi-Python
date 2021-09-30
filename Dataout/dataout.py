import sys #sys contiene le funzioni per accedere agli argomenti passati da linea di comando
import os #contiene le funzioni per fare le operazioni su file e cartelle
import statistics

nome_cartella_destinazione = sys.argv[1] if sys.argv[1:] else 'out' #usa sys.argv[1] se non è vuota, 'out altrimenti'
#print(nome_cartella_destinazione)

#controllo sul tipo assunto da nome_cartella_destinazione
if(isinstance(nome_cartella_destinazione,list)):
    print('nome_cartella_destinazione è una lista')
elif(isinstance(nome_cartella_destinazione, str)):
    print('nome_cartella_destinazione è una stringa')

#creazione della cartella
try:
    os.mkdir(nome_cartella_destinazione)
    print('Creata la cartella ', nome_cartella_destinazione, ', in cui verranno scritti i file')
except FileExistsError:
    print('La cartella ', nome_cartella_destinazione, ',in cui verranno scritti i file, già esiste')

#scansione su tutti i file nella directory corrente (nome_file in os.listdir()) che finiscono con .data
for nome_file in os.listdir():
    if (nome_file.endswith('.data')):
        print('---------------\nTrovato il file ', nome_file)
        #nome_file_destinazione = nome_cartella_destinazione + "/" + nome_file + 'out'
            #versione valida, ma che funzionerebbe solo su windows poiché il separatore l'ho scritto esplicitamente come stringa
        nome_file_destinazione = os.path.join(nome_cartella_destinazione, nome_file + 'out')
        print('Il suo nome in uscita sarà', nome_file_destinazione)
        file_destinazione = open(nome_file_destinazione, 'w');
        contatore_righe = 1;
        for riga in open(nome_file): #open restituisce una lista di stringhe corrispondenti alle varie linee del file
            dati_riga = [float(dato) for dato in riga.split()] #abbiamo una lista di float ottenuta separando i dati contenuti nella linea di file
            file_destinazione.write('Risultati elaborazione riga %d \n' %contatore_righe)
            file_destinazione.write('%.2f %2f %2f\n' %(min(dati_riga), max(dati_riga), statistics.mean(dati_riga)))
            contatore_righe+=1
        print('...fine elaborazione\n---------------')
