-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 09, 2021 at 02:59 PM
-- Server version: 5.7.19
-- PHP Version: 7.1.9
use parking_system;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- --------------------------------------------------------

--
-- Table structure for table `parking_space`
--

 DROP TABLE `parking_space`;
 CREATE TABLE  `parking_space` (
   `id` int NOT NULL AUTO_INCREMENT,
   `type_id` int DEFAULT NULL,
   `status` char(20) DEFAULT NULL,
   PRIMARY KEY (`id`)
 ) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

-- Dumping data for table `parking_space`
--

 INSERT INTO `parking_space` (`id`, `type_id`, `status`) VALUES
 (1, 1, 'open'),
 (2, 1, 'open'),
 (3, 1, 'open'),
 (4, 1, 'open'),
 (5, 1, 'open'),
 (6, 1, 'open'),
 (7, 1, 'open'),
 (8, 1, 'open'),
 (9, 1, 'open'),
 (10, 1, 'open'),
 (11, 1, 'open'),
 (12, 1, 'open'),
 (13, 1, 'open'),
 (14, 1, 'open'),
 (15, 2, 'open'),
 (16, 2, 'open'),
 (17, 2, 'open'),
 (18, 2, 'open'),
 (19, 2, 'open'),
 (20, 2, 'open'),
 (21, 2, 'open'),
 (22, 2, 'open'),
 (23, 2, 'open'),
 (24, 2, 'open'),
 (25, 2, 'open'),
 (26, 2, 'open'),
 (27, 2, 'open'),
 (28, 2, 'open'),
 (29, 2, 'open'),
 (30, 2, 'open');

-- --------------------------------------------------------

--
-- Table structure for table `parking_type`
--

 DROP TABLE `parking_type`;
 CREATE TABLE  `parking_type` (
   `id` int NOT NULL AUTO_INCREMENT,
   `name` char(20) DEFAULT NULL,
   `price` decimal(7,2) DEFAULT NULL,
   PRIMARY KEY (`id`)
 ) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `parking_type`
--

 INSERT INTO `parking_type` (`id`, `name`, `price`) VALUES
 (1, 'Two Wheelar', 30.00),
 (2, 'car', 50.00);

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

 DROP TABLE `transaction`;
 CREATE TABLE  `transaction` (
   `id` int NOT NULL AUTO_INCREMENT,
   `vehicle_id` char(20) DEFAULT NULL,
   `parking_id` int DEFAULT NULL,
  `entry_date` date DEFAULT NULL,
   `exit_date` date DEFAULT NULL,
   `amount` decimal(10,2) DEFAULT NULL,
   PRIMARY KEY (`id`)
 ) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;


COMMIT;
