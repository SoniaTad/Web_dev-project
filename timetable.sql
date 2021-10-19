-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 12, 2021 at 02:32 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `skytravel`
--

-- --------------------------------------------------------

--
-- Table structure for table `timetable`
--

CREATE TABLE `timetable` (
  `ID` int(11) NOT NULL,
  `Dep_ID` int(11) NOT NULL,
  `Des_ID` int(11) NOT NULL,
  `Dep_Time` varchar(10) NOT NULL,
  `Arr_Time` varchar(10) NOT NULL,
  `Cost_£` int(11) NOT NULL,
  `T_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `timetable`
--

INSERT INTO `timetable` (`ID`, `Dep_ID`, `Des_ID`, `Dep_Time`, `Arr_Time`, `Cost_£`, `T_ID`) VALUES
(1, 1, 2, '09:00:00', '12:00:00', 10, 1),
(2, 2, 1, '13:00:00', '16:00:00', 10, 1),
(3, 2, 3, '06:00:00', '08:00:00', 5, 1),
(4, 3, 6, '12:00:00', '15:00:00', 7, 1),
(5, 6, 5, '16:00:00', '20:00:00', 8, 1),
(6, 5, 6, '21:00:00', '01:00:00', 8, 1),
(7, 3, 5, '09:00:00', '10:00:00', 4, 1),
(8, 3, 2, '10:00:00', '12:00:00', 5, 1),
(9, 2, 4, '13:00:00', '18:00:00', 20, 1),
(10, 1, 3, '12:00:00', '12:30:00', 20, 2),
(11, 2, 4, '12:00:00', '13:00:00', 30, 2),
(12, 3, 2, '13:00:00', '13:30:00', 15, 2),
(13, 4, 5, '13:30:00', '14:30:00', 35, 2),
(14, 3, 1, '13:00:00', '13:30:00', 20, 2),
(15, 4, 2, '14:30:00', '15:30:00', 30, 2),
(16, 2, 3, '13:00:00', '13:30:00', 15, 2),
(17, 5, 4, '15:00:00', '16:00:00', 35, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `timetable`
--
ALTER TABLE `timetable`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Dep_ID` (`Dep_ID`),
  ADD KEY `Des_ID` (`Des_ID`),
  ADD KEY `T_ID` (`T_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `timetable`
--
ALTER TABLE `timetable`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `timetable`
--
ALTER TABLE `timetable`
  ADD CONSTRAINT `timetable_ibfk_1` FOREIGN KEY (`Dep_ID`) REFERENCES `cities` (`City_ID`),
  ADD CONSTRAINT `timetable_ibfk_2` FOREIGN KEY (`Des_ID`) REFERENCES `cities` (`City_ID`),
  ADD CONSTRAINT `timetable_ibfk_3` FOREIGN KEY (`T_ID`) REFERENCES `travelmode` (`Transport_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
