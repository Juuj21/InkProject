CREATE TABLE IF NOT EXISTS user (
    "id" INTEGER,
    "username" VARCHAR(200),
    "hash" TEXT,
    "pfpName" TEXT,
    "pfp" BLOB,
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS profiles (
    "id" INTEGER,
    "name" TEXT,
    "description" TEXT,
    "skills" TEXT,
    "email" TEXT,
    "phone" TEXT,
    "profession" TEXT,
    "experience" TEXT,
    "hourlyRate" INTEGER,
    "totalProjects" INTEGER,
    "englishLevel" INTEGER,
    "availabilityNum" INTEGER,
    "availabilityTime" TEXT
)

