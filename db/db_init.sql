CREATE TABLE Stations (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Code NVARCHAR(50),
    Name NVARCHAR(255),
    Latitude FLOAT,
    Longitude FLOAT
);

CREATE TABLE Measurements (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    StationId INT FOREIGN KEY REFERENCES Stations(Id),
    Timestamp DATETIME,
    PM10 FLOAT,
    PM25 FLOAT,
    AQI FLOAT
);
