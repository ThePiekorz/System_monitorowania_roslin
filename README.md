# System_monitorowania_roslin

## Cel Projektu

Projekt zdalnego, automatycznego systemu monitorowania roślin
(tj. Kaktusa), który ma za zadanie monitorować warunki rozwoju
rośliny w celu ich dalszej analizy.

## Opis projektu:

Układ został oparty na bazie Raspberry Pi 2 model B, oraz
nakładki Grove Base hat. Układ komunikuje się zdalnie z
użytkownikiem poprzez aplikacje PuTTy z użyciem połączenia
WiFi (w tym przypadku układ wykorzystuje do tego zewnętrzną
kartę sieciową podpięta pod port USB).

Do poboru danych zostały użyte 3 czujniki. Pierwszym z nich jest
czujnik temperatury i wilgotności grove DHT 11. 
Drugim jest czujnik wilgotności gleby/ sonda pomiaru gleby. 
Trzecim jest czujnik światła, który podaje wartości nasłonecznienia dla rośliny.

Wszystkie dane zebrane podczas działania aplikacji wyświetlają
się na wyświetlaczu LCD i zapisują się na karcie USB w pliku
dane.txt

Dodatkowo system jest wyposażony w kamerę, która umożliwia
monitorowanie tempa wzrostu rośliny poprzez szereg zdjęć.

