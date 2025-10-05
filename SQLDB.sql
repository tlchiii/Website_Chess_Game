CREATE DATABASE CoVuaDB;
GO
USE CoVuaDB;
GO

CREATE TABLE TaiKhoan (
    maTK INT IDENTITY(1,1) PRIMARY KEY,
    tenTK NVARCHAR(50) NOT NULL,
    matKhau NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL UNIQUE,
    diem INT DEFAULT 0,
    mauCo NVARCHAR(10),          -- trắng / đen
    trangThai NVARCHAR(20),
    phanQuyen NVARCHAR(20) DEFAULT N'nguoidung'
);
GO

CREATE TABLE BangXepHang (
    maBXH INT IDENTITY(1,1) PRIMARY KEY,
    maTK INT NOT NULL,
    diemMoi INT,
    FOREIGN KEY (maTK) REFERENCES TaiKhoan(maTK)
);
GO

CREATE TABLE BanCo (
    maBan INT IDENTITY(1,1) PRIMARY KEY,
    kichThuoc INT NOT NULL DEFAULT 8,
    isEndGame BIT DEFAULT 0
);
GO

CREATE TABLE OCo (
    maO INT IDENTITY(1,1) PRIMARY KEY,
    x INT NOT NULL,
    y INT NOT NULL,
    maBan INT NOT NULL,
    FOREIGN KEY (maBan) REFERENCES BanCo(maBan)
);
GO

CREATE TABLE QuanCo (
    maQuan INT IDENTITY(1,1) PRIMARY KEY,
    tenQuan NVARCHAR(20) NOT NULL,    -- Vua, Hậu, Xe, Tượng, Mã, Tốt
    mau NVARCHAR(10) NOT NULL,        -- trắng / đen
    viTriO INT NULL,
    FOREIGN KEY (viTriO) REFERENCES OCo(maO)
);
GO

CREATE TABLE TranDau (
    maTD INT IDENTITY(1,1) PRIMARY KEY,
    maTK1 INT NOT NULL,
    maTK2 INT NOT NULL,
    maBan INT NOT NULL,
    thoiGianNguoiChoi1 INT,
    thoiGianNguoiChoi2 INT,
    ketThucTran NVARCHAR(50),
    FOREIGN KEY (maBan) REFERENCES BanCo(maBan),
    FOREIGN KEY (maTK1) REFERENCES TaiKhoan(maTK),
    FOREIGN KEY (maTK2) REFERENCES TaiKhoan(maTK)
);
GO

CREATE TABLE NuocDi (
    maNuoc INT IDENTITY(1,1) PRIMARY KEY,
    maTD INT NOT NULL,
    quanCoDi INT NOT NULL,
    viTriBatDau INT NOT NULL,
    viTriKetThuc INT NOT NULL,
    FOREIGN KEY (maTD) REFERENCES TranDau(maTD),
    FOREIGN KEY (quanCoDi) REFERENCES QuanCo(maQuan),
    FOREIGN KEY (viTriBatDau) REFERENCES OCo(maO),
    FOREIGN KEY (viTriKetThuc) REFERENCES OCo(maO)
);
GO

CREATE TABLE BaiViet (
    maBV INT IDENTITY(1,1) PRIMARY KEY,
    tieuDe NVARCHAR(200) NOT NULL,
    noiDung NVARCHAR(MAX),
    ngayDang DATETIME DEFAULT GETDATE(),
    maTK INT NOT NULL,
    FOREIGN KEY (maTK) REFERENCES TaiKhoan(maTK)
);
GO

CREATE TABLE BinhLuan (
    maBL INT IDENTITY(1,1) PRIMARY KEY,
    noiDung NVARCHAR(MAX),
    ngayBinhLuan DATETIME DEFAULT GETDATE(),
    maBV INT NOT NULL,
    maTK INT NOT NULL,
    FOREIGN KEY (maBV) REFERENCES BaiViet(maBV),
    FOREIGN KEY (maTK) REFERENCES TaiKhoan(maTK)
);
GO


INSERT INTO TaiKhoan (tenTK, matKhau, email, diem, mauCo, trangThai, phanQuyen)
VALUES 
(N'admin', N'123456', N'admin@example.com', 1000, N'trắng', N'hoạt động', N'admin'),
(N'nguoidung1', N'123456', N'user1@example.com', 800, N'đen', N'hoạt động', N'nguoidung');

INSERT INTO BanCo (kichThuoc, isEndGame) VALUES (8, 0);
INSERT INTO OCo (x, y, maBan) VALUES (1,1,1), (1,2,1), (2,1,1);

INSERT INTO QuanCo (tenQuan, mau, viTriO) 
VALUES (N'Vua', N'trắng', 1), (N'Hậu', N'đen', 2);

INSERT INTO TranDau (maTK1, maTK2, maBan, ketThucTran)
VALUES (1,2,1,N'Đang diễn ra');

INSERT INTO NuocDi (maTD, quanCoDi, viTriBatDau, viTriKetThuc)
VALUES (1,1,1,2);

INSERT INTO BaiViet (tieuDe, noiDung, maTK)
VALUES (N'Kinh nghiệm chơi cờ vua', N'Hãy luôn kiểm soát trung tâm bàn cờ', 1);

INSERT INTO BinhLuan (noiDung, maBV, maTK)
VALUES (N'Bài viết rất hữu ích!', 1, 2);
GO