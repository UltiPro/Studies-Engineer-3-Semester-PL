CREATE TABLE Autor_7
(
  ID_autora NUMBER(3),
  Imie VARCHAR2(20),
  Nazwisko VARCHAR(25)
);
CREATE TABLE Ksiazka_7
(
  ID_ksiazki NUMBER(4),
  Tytul VARCHAR2(50),
  Cena NUMBER(4,2),
  Liczba NUMBER(2)
);
CREATE TABLE Ksiazka_szczegoly_7
(
  ID_ksiazki NUMBER(4),
  ISBN VARCHAR2(13),
  Data_wydania DATE,
  Oprawa NUMBER(1)
);
CREATE TABLE Autor_ksiazka_7
(
  ID_autora NUMBER(3),
  ID_ksiazki NUMBER(4)
);

DESC Autor_7;
DESC Ksiazka_7;
DESC Ksiazka_szczegoly_7;
DESC Autor_ksiazka_7; 

ALTER TABLE Autor_7 ADD CONSTRAINT ogr_7 PRIMARY KEY (ID_autora);
ALTER TABLE Ksiazka_7 ADD CONSTRAINT ogr_7_1 PRIMARY KEY (ID_ksiazki);
ALTER TABLE Ksiazka_szczegoly_7 ADD CONSTRAINT ogr_7_2 PRIMARY KEY (ID_ksiazki);
ALTER TABLE Autor_ksiazka_7 ADD CONSTRAINT ogr_7_3 PRIMARY KEY (ID_autora,ID_ksiazki);

ALTER TABLE Autor_ksiazka_7 ADD CONSTRAINT ogr_7_3_1 FOREIGN KEY (ID_autora) REFERENCES Autor_7 (ID_autora) ON DELETE CASCADE;
ALTER TABLE Ksiazka_szczegoly_7 ADD CONSTRAINT ogr_7_2_1 FOREIGN KEY (ID_ksiazki) REFERENCES  Ksiazka_7 (ID_ksiazki) ON DELETE CASCADE;

ALTER TABLE Autor_7 ADD CONSTRAINT coszmieniam CHECK (Imie > 10);
ALTER TABLE Autor_7 ADD CONSTRAINT jakaszmiana CHECK (Imie > 1 AND Nazwisko > 1);
ALTER TABLE Ksiazka_szczegoly_7 ADD CONSTRAINT costozmienia CHECK (oprawa = 'miekka' OR oprawa = 'twarda');

ALTER TABLE Autor_ksiazka_7 DROP CONSTRAINT ogr_7_3_1;

ALTER TABLE Ksiazka_szczegoly_7 MODIFY Data_wydania SET DEFAULT SYSDATE();

ALTER TABLE Autor_7 RENAME TO Autoor_7;
DESC Autoor_7;
ALTER TABLE Autoor_7 RENAME TO Autor_7;
DESC Autoor_7;

ALTER TABLE Autor_7 RENAME COLUMN Imie TO Immie;
DESC Autor_7;
ALTER TABLE Autor_7 RENAME COLUMN Immie TO Imie;

ALTER TABLE Autor_7 MODIFY Imie NUMBER(3);
DESC Autor_7;
ALTER TABLE Autor_7 MODIFY Imie VARCHAR2(20);

ALTER TABLE Autor_7 MODIFY Nazwisko VARCHAR(16);

ALTER TABLE Ksiazka_7 ADD CONSTRAINT cennik CHECK (cena>0);
ALTER TABLE Ksiazka_7 DROP CONSTRAINT cennik;
ALTER TABLE Ksiazka_7 ADD CONSTRAINT cennik CHECK (cena>1);

ALTER TABLE Autor_7 ADD komunista NUMBER(2);
DESC Autor_7;
ALTER TABLE Autor_7 DROP COLUMN komunista;

DROP TABLE Autor_7;
DROP TABLE Ksiazka_7 CASCADE CONSTRAINTS;
DROP TABLE Ksiazka_szczegoly_7;
DROP TABLE Autor_ksiazka_7;

/dalej

CREATE TABLE Autor_7
(
  ID_autora NUMBER(3),
  Imie VARCHAR2(20),
  Nazwisko VARCHAR2(25)
);
DROP TABLE Autor_7 CASCADE CONSTRAINTS;
CREATE TABLE Ksiazka_7
(
  ID_ksiazki NUMBER(4),
  Tytul VARCHAR2(50),
  Cena NUMBER(4,2),
  Liczba NUMBER(2)
);
DROP TABLE Ksiazka_7 CASCADE CONSTRAINTS;
CREATE TABLE Ksiazka_szczegoly_7
(
  ID_ksiazki NUMBER(4),
  ISBN VARCHAR2(13),
  Data_wydania DATE,
  Oprawa VARCHAR2(13)
);
DROP TABLE Ksiazka_opis_7 CASCADE CONSTRAINTS;
CREATE TABLE Autor_ksiazka_7
(
  ID_autora NUMBER(3),
  ID_ksiazki NUMBER(4)
);
DROP TABLE Autor_ksiazka_7;

ALTER TABLE Autor_7 ADD CONSTRAINT ogr_7_1 PRIMARY KEY (ID_autora);
ALTER TABLE Ksiazka_7 ADD CONSTRAINT ogr_7_2 PRIMARY KEY (ID_ksiazki);
ALTER TABLE Ksiazka_szczegoly_7 ADD CONSTRAINT ogr_7_3 PRIMARY KEY (ID_ksiazki);
ALTER TABLE Autor_ksiazka_7 ADD CONSTRAINT ogr_7_4 PRIMARY KEY (ID_autora,ID_ksiazki);

ALTER TABLE Autor_ksiazka_7 ADD CONSTRAINT ogr_7_4_1 FOREIGN KEY (ID_autora) REFERENCES Autor_7 (ID_autora) ON DELETE CASCADE;
ALTER TABLE Ksiazka_szczegoly_7 ADD CONSTRAINT ogr_7_3_1 FOREIGN KEY (ID_ksiazki) REFERENCES  Ksiazka_7 (ID_ksiazki) ON DELETE CASCADE;

ALTER TABLE Autor_7 ADD CONSTRAINT ogr_7_1_1 CHECK (LENGTH(Imie) > 1 AND LENGTH(Nazwisko) > 1);
ALTER TABLE Ksiazka_szczegoly_7 ADD CONSTRAINT ogr_7_3_2 CHECK (oprawa = 'miekka' OR oprawa = 'twarda');
ALTER TABLE Ksiazka_7 ADD CONSTRAINT ogr_7_2_1 CHECK (cena>1);

ALTER TABLE Ksiazka_szczegoly_7 RENAME TO Ksiazka_opis_7;

ALTER TABLE Autor_7 MODIFY Nazwisko VARCHAR2(16);

// nowe

INSERT INTO Autor_7 VALUES (1,'Adam','Mickiewicz');
INSERT INTO Autor_7(id_autora,imie,nazwisko) VALUES (2,'Henryk','Sienkiewicz');
INSERT INTO Autor_7 VALUES (3,'Patryk','Wójtowicz');
COMMIT;
ROLLBACK;

INSERT INTO Ksiazka_7 VALUES (1,'Potop',53.50,24);
INSERT INTO Ksiazka_7 VALUES (3,'Pan Tadeusz',NULL,10);
INSERT INTO Ksiazka_7 VALUES (4,'Trylogia',99.99,15);
INSERT INTO Ksiazka_7 VALUES (5,'Ballady i romanse',27.60,NULL);
INSERT INTO Ksiazka_7 VALUES (6,NULL,15.90,30);

INSERT INTO Ksiazka_opis_7 VALUES (1,'0123456789','10/05/23','twarda');
INSERT INTO Ksiazka_opis_7 VALUES (4,'0123456788','10/02/17','miekka');
INSERT INTO Ksiazka_opis_7 VALUES (3,'0123456787','09/01/12','miekka');

INSERT INTO Ksiazka_opis_7(id_ksiazki,data_wydania,isbn,oprawa) VALUES (5,'11/09/01',123456786,'twarda');
INSERT INTO Ksiazka_opis_7(id_ksiazki,oprawa,isbn,data_wydania) VALUES (6,'twarda',123456785,'01/05/10');

INSERT INTO Autor_ksiazka_7 VALUES (1,3);
INSERT INTO Autor_ksiazka_7 VALUES (1,5);
INSERT INTO Autor_ksiazka_7 VALUES (2,2);
INSERT INTO Autor_ksiazka_7 VALUES (2,4);
INSERT INTO Autor_ksiazka_7 VALUES (3,1);

Commit;

INSERT INTO Ksiazka_7 VALUES (20,'Za górami i lasami',99.99,12);
INSERT INTO Autor_Ksiazka_7 VALUES(1,20);
INSERT INTO Autor_Ksiazka_7 VALUES(2,20);

UPDATE Ksiazka_7 SET Cena = Cena * 1.1; 

UPDATE Ksiazka_7 SET Liczba = 20 WHERE (tytul='Ballady i romanse');

UPDATE Ksiazka_7 SET Cena = Cena * 0.95 WHERE Liczba > 20;

DELETE Ksiazka_opis;
Rollback;

DELETE Autor_7 WHERE Imie = 'Adam' AND Nazwisko = 'Mickiewicz';

DELETE Ksiazka_7 WHERE Tytul = 'Potop';

DELETE Autor_7;
DELETE Ksiazka_7;
DELETE Ksiazka_szczegoly_7;
DELETE Autor_Ksiazka_7;

DROP TABLE Autor_7;
DROP TABLE Ksiazka_7;
DROP TABLE Ksiazka_szczegoly_7;
DROP TABLE Autor_Ksiazka_7;