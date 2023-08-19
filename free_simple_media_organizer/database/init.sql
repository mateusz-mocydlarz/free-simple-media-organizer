CREATE TABLE app_informations (
    information         VARCHAR(50),
    value               VARCHAR(50)
);

CREATE TABLE paths (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    path                VARCHAR(400) NOT NULL,
    created_by          VARCHAR(50) NOT NULL,
    creation_date       DATETIME NOT NULL,
    modified_by         VARCHAR(50) NOT NULL,
    modification_date   DATETIME NOT NULL
);

CREATE TABLE mimes (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    mime                VARCHAR(50) NOT NULL,
    created_by          VARCHAR(50) NOT NULL,
    creation_date       DATETIME NOT NULL,
    modified_by         VARCHAR(50) NOT NULL,
    modification_date   DATETIME NOT NULL
);

CREATE TABLE files (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    name                VARCHAR(400) NOT NULL,
    size                INTEGER NOT NULL,
    mime_id             INTEGER NOT NULL,
    path_id             INTEGER NOT NULL,
    created_by          VARCHAR(50) NOT NULL,
    creation_date       DATETIME NOT NULL,
    modified_by         VARCHAR(50) NOT NULL,
    modification_date   DATETIME NOT NULL,
    FOREIGN KEY (mime_id) REFERENCES mimes (id),
    FOREIGN KEY (path_id) REFERENCES paths (id)
);

INSERT INTO app_informations VALUES (
    "app_version",
    "01.000.000.00"
);

INSERT INTO app_informations VALUES (
    "creation_db_date",
    datetime('now','localtime')
);