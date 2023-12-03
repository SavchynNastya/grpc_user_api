# Instalations
- pip install -r requirements.txt


# Database
- Database settings:
- Download Ms SQL Server 2022, Ms SQL Server Management Studio
- Create database georesearch, table projects:
- CREATE DATABASE GEORESEARCH;
- USE GeoResearch 
- GO

- DROP TABLE IF EXISTS dbo.Users

- CREATE TABLE dbo.Users(
	Id			INT				IDENTITY(1, 1)		PRIMARY KEY,
	Name			VARCHAR(30)			NOT NULL,
	UserName		VARCHAR(50)			NOT NULL,
	FirstEmail		VARCHAR(50)			NOT NULL,
	SecondEmail		VARCHAR(50)			,
	[Key]			VARBINARY(16)			NOT NULL,
	Hash			VARBINARY(MAX)			NOT NULL,
	Salt			VARCHAR(100)			NOT NULL		DEFAULT 'sha256',
	Status			TINYINT				NOT NULL,		--0 - user, 1 - admin, 2 - analyst, 3 - developer/tester, 4 - user_admin
	Description		VARCHAR(200)			NOT NULL		DEFAULT 'No information',
	Timestamp		DATETIME			NOT NULL		DEFAULT GETDATE()
)

# Python connection settings
- in file .env change parametr SERVER to yours (shown in ms sql server management studio, in dialog box)
  
# Run
- Terminal 1: python server.py
- Terminal 2: python client.py
