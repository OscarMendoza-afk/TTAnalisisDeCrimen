/* Completa */

CREATE TABLE crimenes_cdmx (
	idCarpeta INTEGER PRIMARY KEY,
	Dia INTEGER,
	Mes VARCHAR(50),
	Año YEAR,
	Fecha DATE,
	Hora TIME,
	Delito VARCHAR(250),
	CalidadJuridica VARCHAR(250),
	Categoria VARCHAR(250),
	Colonia VARCHAR(250),
	Alcalia VARCHAR(150),
	Sexo VARCHAR(50),
	Edad INTEGER,
	TipoPersona VARCHAR(100),
	longitud DOUBLE,
	latitud DOUBLE
);

/* ######################################################################*/

/* Delito */

CREATE TABLE Delito (
	idCarpeta INTEGER,
	Delito VARCHAR(250),
	CalidadJuridica VARCHAR(250),
	Categoria VARCHAR(250),
	PRIMARY KEY (idCarpeta)
	
)ENGINE=innodb;

/* Ubicacion */

CREATE TABLE Ubicacion (
	idUbicacion INTEGER,
	Colonia VARCHAR(250),
	Alcalia VARCHAR(150),
	longitud DOUBLE,
	latitud DOUBLE,
	FOREIGN KEY(idUbicacion) REFERENCES Delito(idCarpeta)
	ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=innodb;


/* Persona */

CREATE TABLE Persona (
	idPersona INTEGER,
	Sexo VARCHAR(50),
	Edad INTEGER,
	TipoPersona VARCHAR(100),
	FOREIGN KEY(idPersona) REFERENCES Delito(idCarpeta)
	ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=innodb;

/* Fecha */

CREATE TABLE Fecha (
	idFecha INTEGER,
	Dia INTEGER,
	Mes VARCHAR(50),
	Año YEAR,
	Fecha DATE,
	Hora TIME,
	FOREIGN KEY(idFecha) REFERENCES Delito(idCarpeta)
	ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=innodb;

/* ######################################################################*/
LOAD DATA LOCAL INFILE '/home/ozkr/Documentos/BaseCrimenes.csv' INTO TABLE crimenes_cdmx FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';	



