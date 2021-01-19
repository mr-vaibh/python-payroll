CREATE DATABASE IF NOT EXISTS `mrv_payroll`;
USE `mrv_payroll`;

CREATE TABLE IF NOT EXISTS `employees` (
  `emp_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `department` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `basic` float DEFAULT NULL,
  `hra` float DEFAULT NULL,
  `conveyance` float DEFAULT NULL,
  `bonus` float DEFAULT NULL,
  PRIMARY KEY (`emp_id`),
)
