//ps4

zad1
SELECT imie, nazwisko
FROM pracownik_personalia
ORDER BY nazwisko ASC, imie DESC;

zad2
SELECT imie, nazwisko, nip
FROM pracownik_personalia
WHERE nip LIKE '15%' AND nazwisko LIKE '%ski';

zad3
SELECT id_pracownika, pensja+NVL(premia,0) Zarobki
FROM pracownik;

zad4
SELECT PP.imie, PP.nazwisko, P.stanowisko
FROM pracownik_personalia PP, pracownik P
WHERE PP.id_pracownika = P.id_pracownika AND P.premia IS NOT NULL;

zad5
SELECT id_pracownika, pensja
FROM pracownik P, przedzial_zarobkow PZ
WHERE (id_przedzialu = 1 OR id_przedzialu = 2) AND (P.pensja BETWEEN PZ.dolna_granica AND PZ.gorna_granica);

zad6
SELECT PP.imie , PP.nazwisko, P.pensja
FROM pracownik P, przedzial_zarobkow PZ, pracownik_personalia PP
WHERE PP.id_pracownika = P.id_pracownika AND (id_przedzialu = 1 OR id_przedzialu = 2) AND (P.pensja BETWEEN PZ.dolna_granica AND PZ.gorna_granica);

zad7
SELECT DISTINCT D.nazwa , P.stanowisko
FROM dzial D, pracownik P
WHERE D.id_dzialu = P.id_dzialu;

SELECT D.nazwa , P.stanowisko
FROM dzial D, pracownik P
WHERE D.id_dzialu = P.id_dzialu
GROUP BY D.nazwa, P.stanowisko;

zad8
SELECT PP.nazwisko
FROM pracownik P, pracownik_personalia PP, dzial D
WHERE D.id_dzialu = P.id_dzialu AND PP.id_pracownika = P.id_pracownika AND p.stanowisko LIKE 'informatyk' AND D.nazwa = 'Produkcja';

zad9
SELECT D.nazwa , SUM(P.pensja)
FROM dzial D, pracownik P
WHERE D.id_dzialu = P.id_dzialu
GROUP BY D.nazwa;

SELECT DISTINCT D.nazwa, NVL(P.pensja,0), NVL(P.id_pracownika,0)
FROM dzial D, pracownik P
WHERE D.id_dzialu = P.id_dzialu (+);

zad10
SELECT D.nazwa, Da.nazwa
FROM dzial D, pracownik P, dostawa Do, dostawca Da
WHERE D.id_dzialu = P.id_dzialu AND P.id_pracownika = Do.id_pracownika AND Da.id_dostawcy = Do.id_dostawcy
GROUP BY D.nazwa, Da.nazwa;

//ps5

zad1
SELECT 'Pracownik '||PP.imie||' '||PP.nazwisko||' jest zatrudniony na stanowisku '||P.stanowisko
FROM pracownik P, pracownik_personalia PP
WHERE P.id_pracownika=PP.id_pracownika;

zad2
SELECT 'Pracownik '||UPPER(PP.imie)||' '||UPPER(PP.nazwisko)||' jest zatrudniony na stanowisku '||INITCAP(P.stanowisko)
FROM pracownik P, pracownik_personalia PP
WHERE P.id_pracownika=PP.id_pracownika;

zad3
SELECT PP.imie, PP.nazwisko, REPLACE(UPPER(SUBSTR(D.nazwa,0 ,4)),'KSIE','KSIG') Skrot
FROM pracownik P, pracownik_personalia PP, dzial D
WHERE P.id_pracownika = PP.id_pracownika AND P.id_dzialu = D.id_dzialu;

zad4
SELECT imie, nazwisko
FROM pracownik_personalia 
ORDER BY LENGTH(nazwisko);

zad5
SELECT P.pensja, P.data_zatrudnienia, D.nazwa
FROM Pracownik P, Dzial D, Pracownik_personalia PP
WHERE P.id_pracownika = PP.id_pracownika AND P.id_dzialu = D.id_dzialu AND INITCAP(PP.nazwisko) = INITCAP('&parametr');

zad6
SELECT PP.imie, PP.nazwisko, TO_CHAR(P.data_zatrudnienia ,'DD MONTH YYYY HH24:MI:SS'), TO_CHAR(SYSDATE,'DD MONTH YYYY HH24:MI:SS')
FROM Pracownik_personalia PP, Pracownik P;

zad7
SELECT imie, nazwisko, nip
FROM Pracownik_personalia
WHERE SUBSTR(nip,0,2) = '15';

zad8
SELECT p1.id_przelozonego, p2.id_pracownika, ABS(p1.data_zatrudnienia-p2.data_zatrudnienia) DNI, FLOOR(ABS(MONTHS_BETWEEN(p1.data_zatrudnienia,p2.data_zatrudnienia))) MIESIONCE, FLOOR((ABS(MONTHS_BETWEEN(p1.data_zatrudnienia,p2.data_zatrudnienia)))/24) LATA
FROM Pracownik P1, Pracownik P2
WHERE P2.id_przelozonego = P1.id_pracownika (+);

zad9
SELECT p1.id_przelozonego, PP.nazwisko, ABS(p1.data_zatrudnienia-p2.data_zatrudnienia) DNI, FLOOR(ABS(MONTHS_BETWEEN(p1.data_zatrudnienia,p2.data_zatrudnienia))) MIESIONCE, FLOOR((ABS(MONTHS_BETWEEN(p1.data_zatrudnienia,p2.data_zatrudnienia)))/24) LATA
FROM Pracownik P1, Pracownik P2, Pracownik_personalia PP
WHERE P2.id_przelozonego = P1.id_pracownika (+) AND PP.id_pracownika = P2.id_pracownika;

zad10
SELECT id_pracownika,
    CASE
        WHEN pensja<2500 THEN pensja*1.2
        WHEN pensja<3500 THEN pensja*1.1
        ELSE pensja*1.05
    END Wyplata
FROM pracownik;

//ps6

zad1
SELECT COUNT(*) Liczba
FROM pracownik;

zad2
SELECT COUNT(id_pracownika) AS "Liczba pracownikow z premia"
FROM pracownik
WHERE premia IS NOT NULL;

zad3
SELECT stanowisko, ROUND(AVG(pensja)) "ŒREDNIA PENSJA"
FROM pracownik
GROUP BY stanowisko
ORDER BY "ŒREDNIA PENSJA" DESC;

zad4
SELECT k.adres.miejscowosc, COUNT(id_klienta) 
FROM klient k
GROUP BY k.adres.miejscowosc;

zad5
SELECT PP.nazwisko, COUNT(COLUMN_VALUE)
FROM pracownik_personalia PP, TABLE(PP.telefon)
GROUP BY PP.id_pracownika, PP.nazwisko;

zad6
SELECT D.nazwa ,MAX(P.pensja)-MIN(P.pensja) Roznica 
FROM Dzial D, Pracownik P
WHERE (D.id_dzialu = P.id_dzialu) AND D.nazwa = 'Sprzedaz'
GROUP BY D.nazwa;

zad7
SELECT D.nazwa, COUNT(id_pracownika) "Liczba Pracownikow"
FROM Dzial D, Pracownik P
WHERE (D.id_dzialu = P.id_dzialu)
GROUP BY D.nazwa, D.id_dzialu;

zad7 nie posiada przypisanych adresów wiêc nie wykonamy dobrze 
zadania 7 z poleceniem ni¿ej dowód, jest to spowodoweane tym,
¿e nie ma grupowania po adresie gdy¿ nie ma wartoœci i bêdy
SELECT d.adres
FROM dzial d;

zad8
SELECT D.nazwa, COUNT(DISTINCT P.stanowisko) Stanowiska
FROM dzial D, pracownik P
WHERE D.id_dzialu = P.id_dzialu
GROUP BY D.nazwa, D.id_dzialu;

zad9
SELECT D.nazwa, P.stanowisko Stanowiska, COUNT(P.id_pracownika) "Liczba Pracownikow"
FROM dzial D, pracownik P
WHERE D.id_dzialu = P.id_dzialu
GROUP BY D.nazwa, P.stanowisko;

zad10
SELECT T.nazwa, T.model, COUNT(*) ILE
FROM towar T, zamowienie_szczegoly ZS, Zamowienie Z
WHERE (T.nr_towaru = ZS.nr_towaru) AND (Z.id_zamowienia = ZS.id_zamowienia) AND TO_NUMBER(TO_CHAR(Z.data,'MM')) BETWEEN 0 AND 5
GROUP BY T.nazwa, T.model
HAVING COUNT(*) > 10;

zad11 
SELECT k.nazwisko
FROM klient k, zamowienie Z, zamowienie_szczegoly ZS, towar T
WHERE k.id_klienta = Z.id_klienta AND Z.id_zamowienia = ZS.id_zamowienia AND ZS.nr_towaru = T.nr_towaru AND ((T.ilosc*T.cena)*ZS.ilosc)*((100-ZS.upust)/100) > 1000
GROUP BY k.nazwisko;