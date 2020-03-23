-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 23 Mar 2020 pada 19.08
-- Versi server: 10.1.38-MariaDB
-- Versi PHP: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_elm`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `home_data`
--

CREATE TABLE `home_data` (
  `id` int(11) NOT NULL,
  `bulan` varchar(50) DEFAULT NULL,
  `harga` varchar(50) DEFAULT NULL,
  `produksi` varchar(50) DEFAULT NULL,
  `ketersediaan` varchar(50) DEFAULT NULL,
  `permintaan` varchar(50) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `tahun` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `home_data`
--

INSERT INTO `home_data` (`id`, `bulan`, `harga`, `produksi`, `ketersediaan`, `permintaan`, `created_at`, `tahun`) VALUES
(1, 'Januari', '16000', '1350', '202.59', '10.57', '2020-03-19 16:03:57.470130', '2020'),
(2, 'Februari', '15000', '1485', '223.74', '9.543086', '2020-03-19 16:20:27.766317', '2020'),
(3, 'Maret', '16000', '1150', '103.5', '10.5655595', '2020-03-21 02:04:14.653936', '2020'),
(4, 'April', '12000', '1215', '206.91', '10.224735', '2020-03-21 02:11:23.447146', '2020'),
(5, 'Mei', '15000', '1260', '194.58', '10.5655595', '2020-03-21 02:17:35.862692', '2020'),
(6, 'Juni', '20000', '1440', '201.69', '11.2472085', '2020-03-21 02:19:26.489072', '2020'),
(7, 'Juli', '12000', '1575', '232.02', '11.62211545', '2020-03-21 02:20:16.250233', '2020'),
(8, 'Agustus', '15000', '1530', '207.81', '10.5655595', '2020-03-21 02:20:51.445872', '2020'),
(9, 'September', '10000', '1665', '204.75', '10.224735', '2020-03-21 02:21:32.311856', '2020'),
(10, 'Oktober', '10000', '1170', '136.98', '10.5655595', '2020-03-21 02:22:18.430847', '2020'),
(11, 'November', '11000', '1935', '219.96', '10.224735', '2020-03-21 02:23:26.370135', '2020'),
(12, 'Desember', '15000', '2025', '68.04', '10.5655595', '2020-03-21 02:23:56.837415', '2020');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `home_data`
--
ALTER TABLE `home_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `home_data`
--
ALTER TABLE `home_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
