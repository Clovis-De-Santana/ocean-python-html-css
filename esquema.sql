DROP TABLE IF EXISTS entrada;

CREATE TABLE entradas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo STRING NOT NULL,
    texto STRING NOT NULL
);