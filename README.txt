Dokumentation Baustellenkamera --> created by Christio alias Ramba-Zamba
Hardware: Raspberry Pi Gen.1 mit 5MP Kamera
Betriebssystem: Raspian

Folgende Bedingungen müssen erfüllt sein, dass die Baustellenkamera funktioniert:
1) Kamera ist enstprechend angesschlossen
2) Am Desktop ist ein Ordner mit dem Namen "Baustelle" angelegt
3) Dieser Ordner muss das Python-Skript Baustelle.py, sowie einen weiteren mit dem Namen "pics" beinhalten
4) Das das Skript automatisch nach dem booten ausgeführt wird, muss dies in der .bashrc festgelegt sein
	--> Dieses File findest du wie folgt: Öffne die Shell und gib folgenden Command ein --> nano ~/.bashrc
	--> Scrolle ganz nach unten. Folgende Zeilen müssen dort zu finden sein:  
		echo Running on boot
		sudo python /home/pi/Desktop/Baustelle/Baustelle.py
	--> Sind diese nicht zu finden trag sie ein, speichere das File und führe einen Reboot durch 


Verändern der Fotofrequenz:
1) Öffne das Skript Baustelle.py
2) Verändere im Code die globale Variable "CONST_SLEEP_TIME" (Der Wert danach entspricht dem Fotointervall in Sekunden)


So fügst du die einzelnen Bilder in ein Video zusammen:
1) Die einzelnen Bilder werden in dem Ordner pics im Baustellenordern abgespeichert. 
2) Der Name der Bilder entpricht einem Zähler der iterativ inkrementiert wird.
3) Lösche Bilder die du nicht im Video haben willst aus dem Ordner
4) Dann öffne die Shell, navigiere vorher unbedingt zu den pics Ordner und gib folgenden Commands ein:
	--> erstelle eine liste aller Bilder mit dem Befehl: ls *.jpg > stills.txt
	--> schaue in das File ob die Reihenfolge der Bilder korrekt ist 
	--> mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o timelapse-Baustelle.avi -mf type=jpeg:fps24 mf://@stills.txt
	--> Du kannst die FPS (wie viel Bilder pro Sekunde verwendet werden sollen) mit dem Paramter im vorigen Command veränder (siehe fps24 --> z.B. ändere zu fps6 etc.) 
	--> Du kannst die Bilder natürlich auch auf einen anderen PC transferieren und dort mit einem anderen Programm zusammensetzen
	--> Ist mencoder nicht installiert wird dies in der Shell mit folgenden Command gemacht (Internet benötigt): sudo apt install mencoder 
5) Ist das Video einmal gemacht kannst du die Bilder wieder löschen.
