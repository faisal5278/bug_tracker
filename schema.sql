
DROP TABLE IF EXISTS bugs;

CREATE TABLE bugs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    severity TEXT CHECK(severity IN ('Low', 'Medium', 'High')) NOT NULL,
    status TEXT CHECK(status IN ('Open', 'Closed')) NOT NULL,
    module TEXT,
    created_at TEXT
);
