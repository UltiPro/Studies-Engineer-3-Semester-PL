//PS7

//Zad1
SELECT nazwa
FROM produkt
WHERE typ = (SELECT typ
             FROM produkt
             WHERE nazwa = 'produkt_1');

//Zad2
SELECT PP.nazwisko
FROM pracownik_personalia PP, pracownik P
WHERE PP.id_pracownika = P.id_pracownika AND P.data_zatrudnienia < (SELECT data_zatrudnienia
                                                                    FROM pracownik
                                                                    WHERE stanowisko = 'prezes');                                                                
//Zad3
SELECT PP.nazwisko
FROM pracownik_personalia PP, pracownik P
WHERE PP.id_pracownika = P.id_pracownika AND P.pensja+ NVL(P.premia,0) > (SELECT AVG(pensja+NVL(premia,0))
                                                                          FROM pracownik);
SELECT PP.nazwisko
FROM pracownik_personalia PP, pracownik P
WHERE PP.id_pracownika = P.id_pracownika AND P.pensja > (SELECT AVG(pensja)
                                                         FROM pracownik);                                                                      
//Zad4
SELECT PP.nazwisko, P.data_zatrudnienia
FROM pracownik_personalia PP, pracownik P
WHERE PP.id_pracownika = P.id_pracownika AND P.data_zatrudnienia = (SELECT MIN(data_zatrudnienia)
                                                                    FROM pracownik);
//Zad5
SELECT stanowisko, AVG(pensja) srednia
FROM pracownik
GROUP BY stanowisko
HAVING AVG(pensja) > (SELECT AVG(pensja)
                      FROM pracownik)
ORDER BY srednia DESC;

//Zad6
SELECT D.nazwa, COUNT(P.id_pracownika) ile
FROM dzial D, pracownik P
WHERE D.id_dzialu = P.id_dzialu
GROUP BY D.nazwa;

SELECT D.nazwa, COUNT(*) ile
FROM dzial D, pracownik P
WHERE D.id_dzialu = P.id_dzialu
GROUP BY D.nazwa
HAVING COUNT(*) = (SELECT MAX(count(*))
                   FROM pracownik
                   GROUP BY id_dzialu);

//Zad7
SELECT Pp.nazwisko
FROM pracownik_personalia PP, pracownik P
WHERE PP.id_pracownika = P.id_pracownika AND P.pensja < (SELECT AVG(pensja)
                                                         FROM pracownik
                                                         WHERE P.stanowisko = stanowisko);
//Zad8
SELECT PP.nazwisko
FROM pracownik_personalia PP, pracownik P
WHERE PP.id_pracownika = P.id_pracownika AND data_zatrudnienia < (SELECT data_zatrudnienia
                                                                  FROM pracownik
                                                                  WHERE id_pracownika = P.id_przelozonego);
//Zad9
SELECT D.nazwa, PP.nazwisko, P.pensja
FROM dzial D, pracownik_personalia PP, pracownik P
WHERE D.id_dzialu = P.id_dzialu AND P.id_pracownika = PP.id_pracownika AND P.pensja = (SELECT MAX(pensja)
                                                                                       FROM pracownik
                                                                                       WHERE D.id_dzialu = id_dzialu);
                                                                                       
//Zad10
SELECT T.nazwa
FROM towar T, produkcja P
WHERE T.nr_towaru = P.nr_towaru AND T.cena > (SELECT budzet
                                              FROM produkcja
                                              WHERE T.nr_towaru = nr_towaru);
                                              
//PS9

//ZAD1
SELECT PP.nazwisko, P.pensja
FROM Pracownik_Personalia PP, Pracownik P
WHERE PP.id_pracownika = P.id_pracownika AND P.id_pracownika IN (SELECT id_przelozonego
                                                                 FROM Pracownik
                                                                 );
                                                                 
SELECT PP.nazwisko, P.pensja
FROM Pracownik_Personalia PP, Pracownik P
WHERE PP.id_pracownika = P.id_pracownika AND P.id_pracownika NOT IN (SELECT id_przelozonego
                                                                     FROM Pracownik
                                                                     WHERE id_przelozonego IS NOT NULL);
                                                                     
//ZAD2
SELECT P.stanowisko, AVG(P.pensja) srednia
FROM Pracownik P
GROUP BY stanowisko
HAVING AVG(P.pensja) NOT IN (SELECT AVG(pensja)
                             FROM Pracownik
                             WHERE stanowisko <> P.stanowisko
                             GROUP BY stanowisko);
                            
SELECT P.stanowisko, AVG(P.pensja) srednia
FROM Pracownik P
GROUP BY stanowisko
HAVING AVG(P.pensja) <> ALL (SELECT AVG(pensja)
                             FROM Pracownik
                             WHERE stanowisko <> P.stanowisko
                             GROUP BY stanowisko);
                        
//ZAD3
SELECT DISTINCT PP.nazwisko
FROM Pracownik_Personalia PP, Pracownik P, Dostawa D
WHERE PP.id_pracownika = P.id_pracownika AND D.id_pracownika = P.id_pracownika AND P.pensja NOT IN (SELECT MIN(pensja)
                                                                                                    FROM Pracownik) AND P.id_pracownika IN (SELECT id_pracownika
                                                                                                                                            FROM Pracownik_Produkcja
                                                                                                                                            GROUP BY id_pracownika
                                                                                                                                            HAVING COUNT(*) >= ALL (SELECT MAX(COUNT(*))
                                                                                                                                                                    FROM Pracownik_produkcja
                                                                                                                                                                    GROUP BY id_pracownika));
                                                                                                                                            
//ZAD4
//4.1
SELECT stanowisko, COUNT(*) "ile ludu"
FROM Pracownik P
WHERE id_pracownika IN (SELECT id_pracownika
                        FROM pracownik_produkcja)
GROUP BY stanowisko
HAVING COUNT(*) >=ALL (SELECT COUNT(*)
                       FROM Pracownik
                       WHERE id_pracownika IN (SELECT id_pracownika
                                               FROM pracownik_produkcja)
                       GROUP BY stanowisko);
//4.2
SELECT stanowisko, COUNT(*) "ile ludu"
FROM Pracownik P
WHERE stanowisko IN (SELECT DISTINCT stanowisko
                     FROM Pracownik P1, Pracownik_produkcja PP1
                     WHERE P1.id_pracownika = PP1.id_pracownika)
GROUP BY stanowisko
HAVING COUNT(*) >=ALL (SELECT COUNT(*)
                       FROM Pracownik
                       WHERE id_pracownika IN (SELECT id_pracownika
                                               FROM pracownik_produkcja)
                                               GROUP BY stanowisko);
//ZAD5
SELECT PP.nazwisko, D.nazwa, D.id_dzialu
FROM Pracownik_Personalia PP, Pracownik P, Dzial D
WHERE PP.id_pracownika = P.id_pracownika AND P.id_dzialu = D.id_dzialu AND P.pensja IN (SELECT MIN(pensja)
                                                                                        FROM Pracownik
                                                                                        WHERE id_dzialu=P.id_dzialu
                                                                                        GROUP BY id_dzialu
                                                                                        HAVING COUNT(*) <ANY (SELECT COUNT(*)
                                                                                                              FROM Pracownik
                                                                                                              GROUP BY id_dzialu));
//help
SELECT COUNT(*)
FROM Pracownik
GROUP BY id_dzialu;

//ZAD6
SELECT Z.data, K.adres.miejscowosc
FROM Klient K, Zamowienie Z
WHERE K.id_klienta = Z.id_klienta
GROUP BY Z.data, K.adres.miejscowosc
HAVING COUNT(*) NOT IN (SELECT MAX(COUNT(*))
                        FROM Klient K1, Zamowienie Z1
                        WHERE K1.id_klienta = Z1.id_klienta
                        GROUP BY Z1.data)
ORDER BY Z.data;
                   
//ZAD7
SELECT K.nazwisko, SUM((ZS.ilosc*T.cena)*(1-ZS.upust/100)) kwota
FROM Klient K, Zamowienie Z, Zamowienie_szczegoly ZS, Towar T
WHERE K.id_klienta = Z.id_klienta AND ZS.id_zamowienia = Z.id_zamowienia AND ZS.nr_towaru = T.nr_towaru
GROUP BY K.id_klienta, K.nazwisko
HAVING SUM(ZS.ilosc) IN (SELECT MAX(SUM(ZS1.ilosc))
                         FROM Klient K1, Zamowienie Z1, Zamowienie_szczegoly ZS1, Towar T1
                         WHERE K1.id_klienta = Z1.id_klienta AND ZS1.id_zamowienia = Z1.id_zamowienia AND ZS1.nr_towaru = T1.nr_towaru
                         GROUP BY K1.id_klienta);

//PS10
//ZAD1
SELECT P3.stanowisko, SUM(P3.pensja) "sumaryczna pensja"
FROM Pracownik P3
WHERE EXISTS(SELECT P1.id_pracownika
             FROM Pracownik P1, Pracownik P2
             WHERE P1.id_pracownika = P2.id_przelozonego AND P1.stanowisko = P3.stanowisko AND P2.stanowisko = P3.stanowisko)
GROUP BY P3.stanowisko;

//ZAD2
SELECT D.id_dzialu, PP.nazwisko
FROM Dzial D, Pracownik P, Pracownik_Personalia PP
WHERE D.id_dzialu = P.id_dzialu AND P.id_pracownika = PP.id_pracownika AND NOT EXISTS(SELECT P2.id_pracownika
                                                                                      FROM Pracownik P2
                                                                                      WHERE P2.id_dzialu = D.id_dzialu AND pensja>=P.pensja AND P2.id_pracownika <> P.id_pracownika);
                                                                                  
//ZAD3
SELECT P.stanowisko
FROM Pracownik P
WHERE NOT EXISTS(SELECT COUNT(*)
                 FROM Pracownik P2
                 WHERE P2.stanowisko = P.stanowisko
                 GROUP BY P2.pensja
                 HAVING COUNT(*) > 1)
GROUP BY P.stanowisko;

SELECT P.stanowisko
FROM Pracownik P
WHERE NOT EXISTS(SELECT P2.id_pracownika
                 FROM Pracownik P2
                 WHERE P2.stanowisko=P.stanowisko AND P2.pensja IN (SELECT P3.pensja
                                                                    FROM Pracownik P3
                                                                    WHERE P3.stanowisko=P2.stanowisko AND P2.id_pracownika <> P3.id_pracownika))
GROUP BY P.stanowisko;

//ZAD4
SELECT PP.nazwisko, P.stanowisko, P.pensja
FROM Pracownik P, Pracownik_Personalia PP
WHERE PP.id_pracownika = P.id_pracownika AND NOT EXISTS(SELECT P2.id_pracownika
                                                        FROM Pracownik P2
                                                        WHERE P2.stanowisko = P.stanowisko AND P2.pensja = P.pensja AND P2.id_pracownika <> P.id_pracownika)       
                                         AND NOT EXISTS (SELECT P3.stanowisko
                                                        FROM Pracownik P3
                                                        WHERE P3.stanowisko = P.stanowisko
                                                        GROUP BY P3.stanowisko
                                                        HAVING AVG(P3.pensja) IN (SELECT AVG(P4.pensja)
                                                                                  FROM Pracownik P4
                                                                                  WHERE P3.stanowisko <> P4.stanowisko
                                                                                  GROUP BY P4.stanowisko));
//ZAD5
SELECT K1.imie, K1.nazwisko
FROM Klient K1
WHERE NOT EXISTS(SELECT K.imie, K.nazwisko
                 FROM Klient K, Zamowienie Z, Zamowienie_Szczegoly ZS, Towar T
                 WHERE K.id_klienta = Z.id_klienta AND Z.id_zamowienia = ZS.id_zamowienia AND ZS.nr_towaru = T.nr_towaru AND (T.cena*ZS.ilosc)*(1-ZS.upust/100)<5000
                 GROUP BY K.imie,K.nazwisko);
    
//ZAD6
SELECT PP.nazwisko, PP.imie
FROM Pracownik P, Pracownik P1, Pracownik_Personalia PP
WHERE PP.id_pracownika = P.id_pracownika AND P.id_przelozonego = P1.id_przelozonego AND P.id_przelozonego <> P1.id_pracownika AND EXISTS(SELECT PP.nr_towaru
                                                                                                                                         FROM Pracownik P3, Pracownik_Produkcja PP, Produkcja Pd
                                                                                                                                         WHERE P3.id_pracownika = PP.id_pracownika AND PP.nr_towaru = Pd.nr_towaru
                                                                                                                                         GROUP BY PP.nr_towaru
                                                                                                                                         HAVING COUNT(PP.id_pracownika)>1)
GROUP BY P.id_przelozonego, PP.nazwisko, PP.imie
HAVING COUNT(P1.id_pracownika) >=ALL (SELECT COUNT(P4.id_pracownika)
                                      FROM Pracownik P4
                                      GROUP BY P4.id_przelozonego);