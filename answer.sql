
CREATE DATABASE LibraryManagement;

USE LibraryManagement;

CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE,
    UNIQUE (FirstName, LastName)
);

CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Genre VARCHAR(50),
    AuthorID INT, 
    PublishYear INT,
    AvailableCopies INT NOT NULL CHECK (AvailableCopies >= 0),
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE SET NULL
);

CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Phone VARCHAR(15),
    JoinDate DATE NOT NULL
);

CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Position VARCHAR(50),
    HireDate DATE NOT NULL
);

CREATE TABLE BorrowedBooks (
    BorrowID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT,
    BookID INT,
    BorrowDate DATE NOT NULL,
    ReturnDate DATE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE,
    CHECK (ReturnDate >= BorrowDate OR ReturnDate IS NULL)
);

INSERT INTO Authors (FirstName, LastName, DateOfBirth) VALUES ('George', 'Orwell', '1903-06-25');
INSERT INTO Authors (FirstName, LastName, DateOfBirth) VALUES ('J.K.', 'Rowling', '1965-07-31');

INSERT INTO Books (Title, Genre, AuthorID, PublishYear, AvailableCopies) VALUES ('1984', 'Dystopian', 1, 1949, 5);
INSERT INTO Books (Title, Genre, AuthorID, PublishYear, AvailableCopies) VALUES ('Harry Potter and the Sorcerer\'s Stone', 'Fantasy', 2, 1997, 10);

INSERT INTO Members (FirstName, LastName, DateOfBirth, Email, Phone, JoinDate) VALUES ('Alice', 'Johnson', '1990-05-15', 'alice.johnson@example.com', '123-456-7890', '2023-01-01');
INSERT INTO Members (FirstName, LastName, DateOfBirth, Email, Phone, JoinDate) VALUES ('Bob', 'Smith', '1985-11-23', 'bob.smith@example.com', '987-654-3210', '2022-03-15');

INSERT INTO Staff (FirstName, LastName, Position, HireDate) VALUES ('Samantha', 'Green', 'Librarian', '2020-05-20');
INSERT INTO Staff (FirstName, LastName, Position, HireDate) VALUES ('Tom', 'Davis', 'Assistant Librarian', '2021-08-01');

INSERT INTO BorrowedBooks (MemberID, BookID, BorrowDate, ReturnDate) VALUES (1, 1, '2023-02-01', '2023-02-15');
INSERT INTO BorrowedBooks (MemberID, BookID, BorrowDate, ReturnDate) VALUES (2, 2, '2023-03-05', NULL);
