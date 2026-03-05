CREATE DATABASE Vehicles;
USE Vehicles;

-- 1. Centers Table
CREATE TABLE Centers (
    CenterID INT PRIMARY KEY AUTO_INCREMENT,
    CenterName VARCHAR(100) NOT NULL
);

-- 2. Brands Table
CREATE TABLE Brands (
    BrandID INT PRIMARY KEY AUTO_INCREMENT,
    BrandName VARCHAR(100) NOT NULL
);

-- 3. Operating Status Table
CREATE TABLE OperatingStatus (
    StatusID INT PRIMARY KEY AUTO_INCREMENT,
    StatusName VARCHAR(50) NOT NULL -- (تعمل، لا تعمل، عاطل، تكهين)
);

-- 4. Vehicles Table
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT,
    PlateNumber VARCHAR(50),
    WorkLocation VARCHAR(200),
    ModelYear INT,
    CarType VARCHAR(100),
    ChassisNumber VARCHAR(100),
    EngineNumber VARCHAR(100),
    CenterID INT,
    BrandID INT,
    StatusID INT,
    AdditionalNotes TEXT,
    
    CONSTRAINT FK_Center FOREIGN KEY (CenterID) REFERENCES Centers(CenterID),
    CONSTRAINT FK_Brand FOREIGN KEY (BrandID) REFERENCES Brands(BrandID),
    CONSTRAINT FK_Status FOREIGN KEY (StatusID) REFERENCES OperatingStatus(StatusID)
);
