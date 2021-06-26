-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2021 at 08:58 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crazydev`
--

-- --------------------------------------------------------

--
-- Table structure for table `blogs`
--

CREATE TABLE `blogs` (
  `id` int(100) NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(22) NOT NULL,
  `content` text NOT NULL,
  `img` varchar(22) NOT NULL,
  `date_time` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(120) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(100) NOT NULL,
  `img` varchar(22) DEFAULT NULL,
  `date_time` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `img`, `date_time`) VALUES
(100, 'Shivam Raj Dubey', 'admn', 'shivam', '', '0000-00-00 00:00:00.000000'),
(101, 'Shivam Raj Dubey', 'dubeyshivam1911@gmail.com', '12', NULL, '2021-05-19 11:43:59.955536'),
(102, 'Shivam Raj Dubey', 'dubeyshivasdafm1911@gmail.com', '985ad59e9618544df993a7ff9430e7bc501d013ff666e63b8653d26f0c85340f', NULL, '2021-05-19 12:54:19.976325'),
(103, 'Shivam Raj Dubey', 'dubeyshivam191221@gmail.com', '985ad59e9618544df993a7ff9430e7bc501d013ff666e63b8653d26f0c85340f', NULL, '2021-05-19 12:54:51.758325'),
(105, 'Shivam Raj Dubey', 'dubeyshiva226m1911@gmail.com', '985ad59e9618544df993a7ff9430e7bc501d013ff666e63b8653d26f0c85340f', NULL, '2021-05-19 13:19:42.440994'),
(106, 'Shivam Raj Dubey', 'dubeyshivxxsam1911@gmail.com', '3a094e59dba0e0afe65f8f9f0a50a42ded791c30b15d0b087cd5d5e95d126977', NULL, '2021-05-19 13:29:38.463685'),
(107, 'Shivam Raj Dubey', 'dubeyshivam123321@gmail.com', '6a051db87a7fc8f87a59dc9ff80e60dc6a296cdca72a49ae50f96b828709d9b9', NULL, '2021-05-19 13:31:52.907481'),
(108, 'Shivam Raj Dubey', 'dubeyshivamraj@gmail.com', '6a051db87a7fc8f87a59dc9ff80e60dc6a296cdca72a49ae50f96b828709d9b9', NULL, '2021-05-19 19:55:02.600854'),
(109, 'Shivam Raj Dubey', 'dubeyshivamraj1@gmail.com', '6a051db87a7fc8f87a59dc9ff80e60dc6a296cdca72a49ae50f96b828709d9b9', NULL, '2021-05-19 21:05:56.527325');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blogs`
--
ALTER TABLE `blogs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blogs`
--
ALTER TABLE `blogs`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(120) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=110;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
