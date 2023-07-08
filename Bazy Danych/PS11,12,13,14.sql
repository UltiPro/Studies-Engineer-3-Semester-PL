//PS11

//Zad1
SELECT PP.imie, Pp.nazwisko , P.stanowisko, (SELECT COUNT(*)
                                             FROM Pracownik P1
                                             WHERE P1.stanowisko = P.stanowisko) liczba
FROM Pracownik_Personalia PP, Pracownik P
WHERE PP.id_pracownika = P.id_pracownika AND (SELECT COUNT(*)
                                             FROM Pracownik P1
                                             WHERE P1.stanowisko = P.stanowisko) > 5
ORDER BY liczba;

-- 1 procent
SELECT Pp.imie, Pp.nazwisko, P.stanowisko, (SELECT COUNT(*)
                                            FROM pracownik P1
                                            WHERE P1.stanowisko = P.stanowisko)/
                                            (SELECT COUNT(*)
                                            FROM pracownik P1)*100 procent
FROM pracownik_personalia Pp, pracownik P
WHERE Pp.id_pracownika = P.id_pracownika;

//Zad2
SELECT D.nazwa, (SELECT COUNT(*)
                 FROM pracownik
                 WHERE id_dzialu = D.id_dzialu)/(SELECT COUNT(*)
                                                 FROM pracownik)*100 procent
FROM dzial D;

//Zad3
SELECT (SELECT SUM(stawka*liczba_godzin) FROM pracownik_produkcja)/(SELECT SUM(budzet) FROM produkcja)*100 PROCENT
FROM Dual;

//Zad4

SELECT DISTINCT nazwisko, (SELECT T.nazwa
                           FROM Towar T, Produkcja P, Pracownik_Produkcja PP, Pracownik PR
                           WHERE T.nr_towaru = P.nr_towaru AND P.nr_towaru = PP.nr_towaru AND PP.id_pracownika = PR.id_pracownika
                           GROUP BY PR.id_dzialu, T.nazwa
                           HAVING COUNT(*) >= ALL (SELECT COUNT(*)
                                                   FROM Towar T, Produkcja P, Pracownik_Produkcja PP, Pracownik PR
                                                   WHERE T.nr_towaru = P.nr_towaru AND P.nr_towaru = PP.nr_towaru AND PP.id_pracownika = PR.id_pracownika
                                                   GROUP BY PR.id_dzialu, T.nazwa)) towar
FROM Pracownik_Personalia PPE1, Towar T1, Produkcja P1, Pracownik_Produkcja PP1, Pracownik PR1
WHERE T1.nr_towaru = P1.nr_towaru AND P1.nr_towaru = PP1.nr_towaru AND PP1.id_pracownika = PR1.id_pracownika AND PPE1.id_pracownika = PR1.id_pracownika;

//Zad5
SELECT PP.nazwisko, P.pensja, P.stanowisko
FROM Pracownik_Personalia PP, pracownik P,(SELECT stanowisko, MAX(pensja) max_pensja
                                           FROM pracownik
                                           GROUP BY stanowisko) POM
WHERE PP.id_pracownika = P.id_pracownika AND POM.max_pensja = P.pensja AND P.stanowisko = POM.stanowisko;

//Zad6

SELECT Dost.nazwa
FROM (SELECT D.nazwa, D.id_dostawcy, COUNT(*)
      FROM Dostawca D, Dostawa DO, Pracownik P
      WHERE D.id_dostawcy = DO.id_dostawcy AND DO.id_pracownika = P.id_pracownika AND P.data_zatrudnienia <=ALL (SELECT data_Zatrudnienia
                                                                                                                 FROM Pracownik)
      GROUP BY D.nazwa, D.id_dostawcy
      HAVING COUNT(*) >= 5) Dost;

//Zad7
SELECT ROUND(koszt/budzet*100,4) PROCENT
FROM (SELECT SUM(stawka*liczba_godzin) koszt FROM pracownik_produkcja), 
     (SELECT SUM(budzet) budzet FROM produkcja);
          
//Zad8

SELECT PP.nazwisko, P.pensja, P.stanowisko
FROM Pracownik_Personalia PP, pracownik P,(SELECT P1.stanowisko, MAX(P1.pensja) max_pensja
                                           FROM pracownik P1
                                           GROUP BY P1.stanowisko
                                           HAVING MAX(P1.pensja) NOT IN (SELECT MAX(pensja)
                                                                         FROM pracownik
                                                                         WHERE stanowisko <> P1.stanowisko
                                                                         GROUP BY stanowisko)) POM
WHERE PP.id_pracownika = P.id_pracownika AND POM.max_pensja = P.pensja AND P.stanowisko = POM.stanowisko;

//PS12

//Zad1
CREATE VIEW pracownik_dane AS
SELECT PP.imie, PP.nazwisko, p.stanowisko, P.pensja
FROM Pracownik_Personalia PP, Pracownik P
WHERE PP.id_pracownika = P.id_pracownika;

DROP VIEW pracownik_dane;

SELECT imie, nazwisko, stanowisko, pensja
FROM Pracownik_Dane
WHERE pensja > (SELECT AVG(pensja)
                FROM Pracownik);
                 
//Zad2
CREATE VIEW Przelozony_Podwladny(przelozony_imie, przelozony_nazwisko, podwladny_imie, podwladny_nazwisko) AS
SELECT PP.imie, PP.nazwisko, PP2.imie, PP2.nazwisko
FROM Pracownik_Personalia PP, Pracownik_Personalia PP2, Pracownik P
WHERE PP.id_pracownika (+) = P.id_przelozonego AND PP2.id_pracownika = P.id_pracownika;

DROP VIEW Przelozony_Podwladny;

SELECT *
FROM Przelozony_Podwladny;

//Zad3
SELECT Przelozony_Imie, Przelozony_Nazwisko, COUNT(*) ile
FROM Przelozony_Podwladny
GROUP BY Przelozony_Imie, Przelozony_Nazwisko
HAVING COUNT(*) > 3;

//Zad4
CREATE VIEW Stanowisko_MAXPensja AS
SELECT stanowisko, Max(pensja) Max_pensja
FROM Pracownik
GROUP BY stanowisko;

DROP VIEW Stanowisko_MAXPensja;

SELECT *
FROM Stanowisko_MAXPensja;

//Zad5
SELECT stanowisko
FROM Stanowisko_MAXPensja
WHERE MAX_Pensja = (SELECT MAX(MAX_PENSJA)
                    FROM Stanowisko_MAXPensja);
                    
//Zad6
SELECT PD.stanowisko, PD.Nazwisko, PD.Pensja
FROM Pracownik_Dane PD, Stanowisko_MAXPensja SMP
WHERE SMP.stanowisko = PD.stanowisko AND SMP.max_pensja = PD.pensja AND PD.stanowisko IN (SELECT P.stanowisko
                                                                                          FROM Pracownik P, Stanowisko_MAXPensja SMP
                                                                                          WHERE SMP.stanowisko = P.stanowisko AND SMP.max_pensja = P.pensja
                                                                                          GROUP BY P.stanowisko
                                                                                          HAVING COUNT(P.stanowisko) = 1);
                                                                                                                              
//Zad7
CREATE VIEW Dochod AS
SELECT SUM(((T.ilosc*T.cena)*ZS.ilosc)*(1-(ZS.upust/100))) dochod_calkowity
FROM Zamowienie_Szczegoly ZS, Towar T
WHERE ZS.nr_towaru = T.nr_towaru;

DROP VIEW Dochod;

SELECT dochod_calkowity
FROM Dochod;

CREATE VIEW Klient_Wydatki AS
SELECT K.imie, K.nazwisko, SUM(((T.ilosc*T.cena)*ZS.ilosc)*(1-(ZS.upust/100))) wydatek_calkowity
FROM Klient K, Zamowienie Z, Zamowienie_Szczegoly ZS, Towar T
WHERE K.id_klienta = Z.id_klienta AND Z.id_zamowienia = ZS.id_zamowienia AND ZS.nr_towaru = T.nr_towaru
GROUP BY K.imie, K.nazwisko;

SELECT *
FROM Klient_Wydatki;

SELECT KW.imie, KW.nazwisko, ROUND((KW.Wydatek_Calkowity/D.Dochod_Calkowity)*100,4) "Procent Dochodu Firmy"
FROM Klient_Wydatki KW, Dochod D;

//ps13

//zad1
CREATE VIEW zad1 as
SELECT K.imie, K.nazwisko
FROM Klient K, Zamowienie Z, Zamowienie_szczegoly ZS, Towar T
WHERE K.id_klienta = Z.id_klienta AND Z.id_zamowienia = ZS.id_zamowienia AND ZS.nr_towaru = T.nr_towaru
GROUP BY K.imie, K.nazwisko, K.id_klienta, Z.id_zamowienia
HAVING SUM(ZS.ilosc*T.cena*(1-(ZS.upust/100))) > 100;

CREATE VIEW zad1a as
SELECT K.imie, K.nazwisko
FROM Klient K, Zamowienie Z, Zamowienie_szczegoly ZS
WHERE K.id_klienta = Z.id_klienta AND Z.id_zamowienia = ZS.id_zamowienia
GROUP BY K.imie, K.nazwisko, K.id_klienta, Z.id_zamowienia
HAVING COUNT(*) > 10;

SELECT * FROM zad1
UNION
SELECT * FROM zad1a;

SELECT * FROM zad1
INTERSECT
SELECT * FROM zad1a;

SELECT * FROM zad1
MINUS
SELECT * FROM zad1a;

//zad2

CREATE VIEW zad22 as
SELECT PP.imie, PP.nazwisko, '2' as typ
FROM Pracownik P, Pracownik_Personalia PP
WHERE P.id_pracownika = PP.id_pracownika AND P.id_przelozonego IS NULL;

CREATE VIEW zad21 as
SELECT DISTINCT PP.imie, PP.nazwisko, '1' as typ
FROM Pracownik P, Pracownik P2, Pracownik_Personalia PP 
WHERE P.id_pracownika = PP.id_pracownika AND P.id_pracownika IN (SELECT id_przelozonego
                                                                 FROM Pracownik);

CREATE VIEW zad20 as
SELECT PP.imie, PP.nazwisko, '0' as typ
FROM Pracownik P, Pracownik_Personalia PP
WHERE P.id_pracownika = PP.id_pracownika AND P.id_przelozonego IS NOT NULL;

CREATE VIEW zad2wynik as
SELECT * FROM zad22
UNION
SELECT * FROM zad21
UNION
SELECT * FROM zad20;

SELECT * 
FROM zad2wynik 
ORDER BY typ DESC;

//zad3

CREATE VIEW Zad31 as
SELECT DISTINCT Stanowisko
FROM Pracownik;

CREATE VIEW Zad32 as
SELECT DISTINCT Stanowisko
FROM Pracownik P, Dostawa D
WHERE P.id_pracownika = D.id_pracownika;

SELECT * FROM Zad31
MINUS
SELECT * FROM Zad32;

//zad4

CREATE VIEW Zad41 as
SELECT T.nazwa
FROM Towar T
WHERE (SELECT COUNT(*)
       FROM Zamowienie_Szczegoly ZS2
       WHERE ZS2.nr_towaru = T.nr_towaru) >= 5;

CREATE VIEW Zad42 as
SELECT T.nazwa
FROM Towar T
WHERE (SELECT COUNT(*)
       FROM Towar_Sklad TS
       WHERE T.nr_towaru = TS.nr_towaru) <= 3;
   
CREATE VIEW Zad43 as       
SELECT T.nazwa 
FROM Zamowienie Z, Zamowienie_Szczegoly ZS, Towar T
WHERE Z.id_zamowienia = ZS.id_zamowienia AND T.nr_towaru = ZS.nr_towaru
GROUP BY Z.id_klienta, ZS.nr_towaru, T.nazwa
HAVING COUNT(*) = 1;
         
SELECT * FROM Zad41
INTERSECT
SELECT * FROM Zad42
MINUS
SELECT * FROM Zad43;

//zad5

SELECT DISTINCT nazwa FROM Dzial;

CREATE VIEW Zad51 as
SELECT DISTINCT D.nazwa
FROM Dzial D, Pracownik P, Zamowienie Z
WHERE D.id_dzialu = P.id_dzialu AND P.id_pracownika = Z.id_pracownika;

CREATE VIEW Zad52 as
SELECT DISTINCT D.nazwa
FROM Pracownik P, Pracownik PP, Dzial D
WHERE P.id_przelozonego = PP.id_pracownika AND P.id_dzialu = PP.id_dzialu AND P.id_dzialu = D.id_dzialu;

SELECT nazwa FROM Dzial
MINUS
SELECT * FROM Zad51
INTERSECT
SELECT * FROM Zad52;

//ps14

//zad1
CREATE TABLE TABELAPOM_PW AS
SELECT P.id_pracownika, PP.imie, PP.nazwisko, P.pensja, P.stanowisko
FROM Pracownik_Personalia PP, Pracownik P
WHERE PP.id_pracownika = P.id_pracownika;

DROP TABLE TABELAPOM_PW;

//zad2
UPDATE TABELAPOM_PW p
SET pensja = pensja*1.05
WHERE pensja = (SELECT MIN(pensja)
                FROM Pracownik p2
                WHERE p2.stanowisko = p.stanowisko);
                
//zad3
UPDATE TABELAPOM_PW
SET pensja = pensja*1.1
WHERE id_pracownika IN (SELECT id_pracownika
                        FROM Pracownik_Produkcja
                        GROUP BY id_pracownika
                        HAVING COUNT(*) >= 10);
                        
//zad4
SELECT * FROM Przedzial_zarobkow;

ALTER TABLE TABELAPOM_PW ADD przedzial NUMBER(1);

SELECT * FROM TABELAPOM_PW;

UPDATE TABELAPOM_PW
SET przedzial = (SELECT id_przedzialu
                 FROM Przedzial_Zarobkow
                 WHERE pensja BETWEEN dolna_granica AND gorna_granica);
                 
SELECT * FROM TABELAPOM_PW;

//zad5
DELETE TABELAPOM_PW
WHERE id_pracownika IN (SELECT id_pracownika
                        FROM Pracownik
                        WHERE premia IS NOT NULL);
                        
ROLLBACK;

//zad6
DELETE TABELAPOM_PW
WHERE id_pracownika IN (SELECT id_pracownika
                        FROM Pracownik
                        WHERE id_przelozonego = (SELECT id_pracownika
                                                 FROM Pracownik_Personalia
                                                 WHERE INITCAP(imie) = INITCAP('&param') AND INITCAP(nazwisko) = INITCAP('&param2')));
                                                 
ROLLBACK;
//zad7
DELETE TABELAPOM_PW
WHERE id_pracownika = (SELECT id_pracownika FROM Pracownik WHERE stanowisko = 'robotnik'
                       MINUS
                       SELECT DISTINCT P.id_pracownika
                       FROM Pracownik P, Pracownik_Produkcja PP
                       WHERE P.id_pracownika = PP.id_pracownika AND P.stanowisko = 'robotnik'
                       UNION
                       SELECT DISTINCT id_pracownika
                       FROM Pracownik_Produkcja
                       WHERE koniec < '2010/05/10');

//zad8
DROP TABLE TABELAPOM_PW;