-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 18, 2020 at 04:10 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `book_my_meal`
--

-- --------------------------------------------------------

--
-- Table structure for table `catagory`
--

CREATE TABLE IF NOT EXISTS `catagory` (
  `catid` varchar(20) NOT NULL,
  `catnm` varchar(20) NOT NULL,
  `caticon` varchar(1000) NOT NULL,
  PRIMARY KEY (`catid`),
  UNIQUE KEY `cnm` (`catnm`),
  UNIQUE KEY `catnm` (`catnm`),
  UNIQUE KEY `catnm_2` (`catnm`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `catagory`
--

INSERT INTO `catagory` (`catid`, `catnm`, `caticon`) VALUES
('Amenac800', 'American', 'American.jpg'),
('Bakyre606', 'Bakery', 'Bakery.jpg'),
('Chiese703', 'Chinese', 'Chinese.jpg'),
('Indnai595', 'Indian', 'Indian.jpg'),
('Itanai706', 'Italian', 'Italian.jpg'),
('Maxnac705', 'Maxican', 'Mexican.jpg'),
('Rajina137', 'Rajeshthani', 'Rajesthani.jpg'),
('Sounai158', 'South Indian', 'South_indian.png'),
('Sweste635', 'Sweets', 'Meethai.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `currentdpstatus`
--

CREATE TABLE IF NOT EXISTS `currentdpstatus` (
  `dpId` varchar(10) NOT NULL,
  `userId` varchar(20) NOT NULL,
  `orderId` bigint(20) NOT NULL,
  `status` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `currentdpstatus`
--


-- --------------------------------------------------------

--
-- Table structure for table `currentorder`
--

CREATE TABLE IF NOT EXISTS `currentorder` (
  `userId` varchar(20) NOT NULL,
  `orderId` bigint(20) NOT NULL,
  `status` int(11) NOT NULL DEFAULT '1',
  `statusMsg` varchar(25) NOT NULL DEFAULT 'CONFIRMED IT',
  `arrivalTime` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `currentorder`
--


-- --------------------------------------------------------

--
-- Table structure for table `deliverypartner`
--

CREATE TABLE IF NOT EXISTS `deliverypartner` (
  `dpId` varchar(10) NOT NULL,
  `dpName` varchar(25) NOT NULL,
  `dpEmail` varchar(25) NOT NULL,
  `dpPassword` varchar(15) NOT NULL,
  `dpMobile` varchar(13) NOT NULL,
  `dpgender` varchar(10) NOT NULL DEFAULT 'male',
  `dpAddress` varchar(60) NOT NULL,
  `dpRegTime` varchar(30) NOT NULL,
  `status` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`dpId`),
  UNIQUE KEY `dpId` (`dpId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `deliverypartner`
--

INSERT INTO `deliverypartner` (`dpId`, `dpName`, `dpEmail`, `dpPassword`, `dpMobile`, `dpgender`, `dpAddress`, `dpRegTime`, `status`) VALUES
('DP109jains', 'Sahil Jain', 'jainsahil9442@gmail.com', 'dpbmm@1234', '9665488235', 'male', '26,Gumasta nagar Indore (452001)', 'Wed May  6 12:24:02 2020', 0),
('DP326gupta', 'Piyush Gupta', 'guptapiyush552@gmail.com', 'dpbmm@1234', '8892054654', 'male', '73 Suvidhi nagar NearChota bangarada Indore', 'Wed May  6 12:21:17 2020', 0),
('DP356vrahu', 'Rahul Verma', 'vrahulrahul0609@gmail.com', 'dpbmm@1234', '9034995716', 'male', '53 shanti colony Airport Road Indore', 'Wed May  6 12:22:33 2020', 0),
('DP53akashu', 'Aakash Shukla', 'akashukla522@gmail.com', 'dpbmm@1234', '9032659456', 'male', '54/5 jawahar colony,  Dewas', 'Wed May  6 12:16:54 2020', 1),
('DP852bunty', 'Bunty', 'buntyy3986@gmail.com', 'dpbmm@1234', '9236520481', 'male', '53,Rajwada, Ring road Indore', 'Wed May  6 12:13:43 2020', 0),
('DP863ravik', 'Ravi Kushwah', 'raviksh521@gmail.com', 'dpbmm@1234', '9380464604', 'male', '43/1 Palhar nagar,60 Feet Road Indore', 'Wed May  6 12:18:29 2020', 0);

-- --------------------------------------------------------

--
-- Table structure for table `food`
--

CREATE TABLE IF NOT EXISTS `food` (
  `food_id` int(11) NOT NULL AUTO_INCREMENT,
  `catagory` varchar(20) NOT NULL,
  `subcatagory` varchar(20) NOT NULL,
  `dish` varchar(30) NOT NULL,
  `price` float NOT NULL,
  `dish_disc` varchar(100) NOT NULL,
  PRIMARY KEY (`food_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=258 ;

--
-- Dumping data for table `food`
--

INSERT INTO `food` (`food_id`, `catagory`, `subcatagory`, `dish`, `price`, `dish_disc`) VALUES
(1, 'Indian', 'Indian Veg', 'Mattar Paneer', 140, ''),
(2, 'Indian', 'Indian Veg', 'Palak Paneer', 140, ''),
(3, 'Indian', 'Indian Veg', 'Paneer Bhurji', 140, ''),
(4, 'Indian', 'Indian Veg', 'Kadhai Paneer', 160, ''),
(5, 'Indian', 'Indian Veg', 'Paneer Chatpata', 160, ''),
(6, 'Indian', 'Indian Veg', 'Shahi Paneer', 160, ''),
(7, 'Indian', 'Indian Veg', 'Kaju Paneer', 160, ''),
(8, 'Indian', 'Indian Veg', 'Veg Korma', 140, ''),
(9, 'Indian', 'Indian Veg', 'Aloo Gobhi', 120, ''),
(10, 'Indian', 'Indian Veg', 'Butter Kofta', 120, ''),
(11, 'Indian', 'Indian Veg', 'Bhindi Masala', 120, ''),
(12, 'Indian', 'Indian Veg', 'Sev Tamater', 120, ''),
(13, 'Indian', 'Indian Veg', 'Tomato Masala', 100, ''),
(14, 'Indian', 'Indian Veg', 'Stuffed Capsicum', 120, ''),
(15, 'Indian', 'Indian Veg', 'Malai Kofta', 140, ''),
(16, 'Indian', 'Rice', 'Jeera Rice', 80, ''),
(17, 'Indian', 'Rice', 'Plain Rice', 60, ''),
(18, 'Indian', 'Rice', 'Fried Rice', 110, ''),
(19, 'Indian', 'Rice', 'Kashmiri Pulao', 120, ''),
(20, 'Indian', 'Rice', 'Shahi Pulao', 120, ''),
(21, 'Indian', 'Rice', 'Butter Khichdi', 120, ''),
(22, 'Indian', 'Dal', 'Dal Fry', 110, ''),
(23, 'Indian', 'Dal', 'Dal Hari Mirch', 110, ''),
(24, 'Indian', 'Dal', 'Dal Makhani', 125, ''),
(25, 'Indian', 'Dal', 'Mix Dal', 125, ''),
(26, 'Indian', 'Dal', 'Dal Punjabi', 120, ''),
(27, 'Indian', 'Indian Bread', 'Tandoori Roti', 10, ''),
(28, 'Indian', 'Indian Bread', 'Butter Tandoori Roti', 12, ''),
(29, 'Indian', 'Indian Bread', 'Missi Roti', 15, ''),
(30, 'Indian', 'Indian Bread', 'Plain Naan', 25, ''),
(31, 'Indian', 'Indian Bread', 'Butter Naan', 30, ''),
(32, 'Indian', 'Indian Bread', 'Garlic Naan', 40, ''),
(33, 'Indian', 'Indian Bread', 'Butter Tandoori Paratha', 30, ''),
(34, 'Indian', 'Indian Bread', 'Stuffed Paratha', 20, ''),
(35, 'Indian', 'Indian Bread', 'Butter Kulcha', 30, ''),
(36, 'Indian', 'Indian Bread', 'Stuffed Kulcha', 25, ''),
(37, 'Indian', 'Indian Bread', 'Aloo Paratha', 30, ''),
(38, 'Indian', 'Indian Bread', 'Namkeen Paratha', 20, ''),
(39, 'Indian', 'Indian Bread', 'Gobhi Paratha', 30, ''),
(40, 'Indian', 'Indian Bread', 'Methi Paratha', 25, ''),
(41, 'Indian', 'Indian Bread', 'Paneer Paratha ', 45, ''),
(42, 'Indian', 'Indian Bread', 'Mixed Paratha', 30, ''),
(43, 'Indian', 'Indian Bread', 'Kashmiri Naan', 35, ''),
(44, 'Indian', 'Accomplishment', 'Onion Salad', 20, ''),
(45, 'Indian', 'Accomplishment', 'Green Salad', 40, ''),
(46, 'Indian', 'Accomplishment', 'Special Salad', 50, ''),
(47, 'Indian', 'Accomplishment', 'Fried Papad', 25, ''),
(48, 'Indian', 'Accomplishment', 'Dry Papad', 25, ''),
(49, 'Indian', 'Accomplishment', 'Fried Masala Papad', 30, ''),
(50, 'Indian', 'Accomplishment', 'Dry Masala Papad', 25, ''),
(51, 'Indian', 'Accomplishment', 'Dry Masala Papad', 25, ''),
(52, 'Indian', 'Accomplishment', 'Boondi Raita', 85, ''),
(53, 'Indian', 'Accomplishment', 'Onion Raita', 80, ''),
(54, 'Indian', 'Accomplishment', 'Veg Raita', 80, ''),
(55, 'Indian', 'Accomplishment', 'Fruit Raita', 100, ''),
(56, 'Indian', 'Accomplishment', 'Fruit Salad', 50, ''),
(57, 'Indian', 'Accomplishment', 'Green Fry Chilli', 30, ''),
(58, 'Indian', 'Accomplishment', 'Plain Curd', 40, ''),
(59, 'Indian', 'Rice', 'Veg Biryani', 120, ''),
(60, 'Indian', 'Thalies', 'Student Thali', 80, '1 seasonal veg + 4 tava Roti + Dal + Rice + Salad'),
(61, 'Indian', 'Thalies', 'Paneer Paratha Thali', 140, 'Paneer sabji + 4 Lachha Paratha + Salad + 2 Butter Tawa roti'),
(62, 'Indian', 'Thalies', 'Punjabi Thali', 160, '6 Butter Roti + Punjabi Paneer + Punjabi Dal + Rice + Mix Veg + Raita +Papad + Salad'),
(63, 'Indian', 'Thalies', 'Regular Thali', 140, '4 Butter Roti + 2 Veg + Papad + Salad + Sweet'),
(64, 'Indian', 'Thalies', 'Delux Thali', 160, 'Butter Panner + Dal Tadka + Seasonal Veg  + 4 Tawa Roti + Jeera Rice +  Gulab Jamun + Salad'),
(65, 'Indian', 'Thalies', 'Mini Thali', 90, '1 Dal  + 1 Veg + 4 Butter Roti + Achhar Salad'),
(66, 'Indian', 'Desserts', 'Lassi', 30, ''),
(67, 'Indian', 'Desserts', 'Mango Lassi', 40, ''),
(68, 'Indian', 'Desserts', 'Lassi With Ice Cream', 40, ''),
(69, 'Indian', 'Desserts', 'Shikanji', 60, ''),
(70, 'Indian', 'Desserts', 'Butter Milk', 20, ''),
(71, 'Indian', 'Desserts', 'Rasgulla', 15, ''),
(72, 'Indian', 'Desserts', 'Gulab Jamun', 10, ''),
(73, 'Indian', 'Desserts', 'Shrikhand', 50, ''),
(74, 'Indian', 'Desserts', 'Fruit Custurd', 50, ''),
(75, 'Indian', 'Desserts', 'Gajar Halwa', 60, ''),
(76, 'Indian', 'Desserts', 'Mung Halwa', 80, ''),
(77, 'Indian', 'Desserts', 'Mawa Bati', 15, ''),
(78, 'Indian', 'Beverages', 'Mineral Water', 20, ''),
(79, 'Indian', 'Beverages', 'Coke', 30, ''),
(80, 'Indian', 'Beverages', 'Sprite', 30, ''),
(81, 'Indian', 'Beverages', 'Fanta', 30, ''),
(82, 'Indian', 'Beverages', 'Appy Fizz', 35, ''),
(83, 'Indian', 'Beverages', 'Frooti', 35, ''),
(84, 'Indian', 'Beverages', 'Soda', 20, ''),
(85, 'Indian', 'Beverages', 'Monster Energy Drink', 149, ''),
(86, 'Indian', 'Beverages', 'Red Bull', 181, ''),
(87, 'Indian', 'Beverages', 'Special Thandai', 60, ''),
(88, 'Indian', 'Beverages', 'Special Thandai', 60, ''),
(89, 'Indian', 'Indian Veg', 'Paneer Kolhapuri', 160, ''),
(90, 'Indian', 'Indian Veg', 'Paneer Tikka Masala', 180, ''),
(91, 'Indian', 'Indian Veg', 'Paneer Handi', 150, ''),
(92, 'Indian', 'Indian Veg', 'Paneer Kofta', 160, ''),
(93, 'Indian', 'Indian Veg', 'Paneer Lababdar', 160, ''),
(94, 'Indian', 'Indian Veg', 'Paneer Peshwai', 160, ''),
(95, 'Indian', 'Indian Veg', 'Sev Paneer', 140, ''),
(96, 'Indian', 'Indian Veg', 'Paneer Punjabi', 160, ''),
(97, 'Indian', 'Indian Veg', 'Kaju Curry', 160, ''),
(98, 'Indian', 'Indian Veg', 'Kaju Makhana', 140, ''),
(99, 'Indian', 'Indian Veg', 'Paneer Korma', 150, ''),
(100, 'Indian', 'Indian Veg', 'Navratan Korma', 150, ''),
(101, 'Indian', 'Indian Veg', 'Mashroom Matar', 140, ''),
(102, 'Indian', 'Indian Veg', 'Methi Matar  Malai', 120, ''),
(103, 'Indian', 'Indian Veg', 'Dum Aloo', 120, ''),
(104, 'Indian', 'Indian Veg', 'Aloo Do Pyaaza', 120, ''),
(105, 'Indian', 'Indian Veg', 'Jeera Aloo', 100, ''),
(106, 'Indian', 'Indian Veg', 'Aloo Matar', 120, ''),
(107, 'Indian', 'Indian Veg', 'Lahsuni Palak', 100, ''),
(108, 'Indian', 'Indian Veg', 'Dudh Sev', 130, ''),
(109, 'Indian', 'Indian Veg', 'Baingan Bharta', 100, ''),
(110, 'Rajeshthani', 'Rajeshthani', 'Dal Baati Churma', 150, ''),
(111, 'Rajeshthani', 'Rajeshthani', 'Bafla ', 40, '1 Piece'),
(112, 'Rajeshthani', 'Rajeshthani', 'Dal', 120, ''),
(113, 'Rajeshthani', 'Rajeshthani', 'Gatte Sabji', 120, ''),
(114, 'Rajeshthani', 'Rajeshthani', 'Kadhi', 120, ''),
(115, 'Rajeshthani', 'Rajeshthani', 'Special  Plate', 50, '2 Bazra Roti with Lahsun Chatni'),
(116, 'Rajeshthani', 'Rajeshthani', 'Ker Sangari', 120, ''),
(117, 'Rajeshthani', 'Rajeshthani', 'Methi Bazra Puri', 20, ''),
(118, 'Rajeshthani', 'Rajeshthani', 'Butter Milk ', 20, ''),
(119, 'Rajeshthani', 'Rajeshthani', 'Bajre ka khichda', 120, ''),
(120, 'Rajeshthani', 'Rajeshthani', 'Mohan Thal', 40, '1 Piece'),
(121, 'Rajeshthani', 'Rajeshthani', 'Mirchi Bada', 30, ''),
(122, 'Rajeshthani', 'Rajeshthani', 'Kalakand', 60, ''),
(123, 'Rajeshthani', 'Rajeshthani', 'Ghevar', 80, ''),
(124, 'Rajeshthani', 'Rajeshthani', 'Moong Halwa', 80, ''),
(125, 'Rajeshthani', 'Rajeshthani', 'Malpua', 40, ''),
(126, 'Rajeshthani', 'Rajeshthani', 'Churma Laddo', 20, ''),
(127, 'Rajeshthani', 'Rajeshthani', 'Balushahi', 20, ''),
(128, 'Rajeshthani', 'Rajeshthani', 'Boondi Raita', 80, ''),
(129, 'Rajeshthani', 'Rajeshthani', 'Aam Ki Launji', 40, ''),
(130, 'Rajeshthani', 'Rajeshthani', 'Kalmi Vada', 25, ''),
(131, 'Rajeshthani', 'Rajeshthani', 'Makka Roti', 15, ''),
(132, 'Rajeshthani', 'Rajeshthani', 'Bajra Roti', 15, ''),
(133, 'Rajeshthani', 'Rajeshthani', 'Bikaneri Khichdi', 100, ''),
(134, 'South Indian', 'South Indian', 'Sada Dosa', 60, ''),
(135, 'South Indian', 'South Indian', 'Masala Dosa', 80, ''),
(136, 'South Indian', 'South Indian', 'Mysore Dosa', 80, ''),
(137, 'South Indian', 'South Indian', 'Mysore Masala Dosa', 90, ''),
(138, 'South Indian', 'South Indian', 'Paneer Sada Dosa', 90, ''),
(139, 'South Indian', 'South Indian', 'Paneer Masala Dosa', 100, ''),
(140, 'South Indian', 'South Indian', 'Cheese  Plain Dosa ', 100, ''),
(141, 'South Indian', 'South Indian', 'Cheese Masala Dosa', 120, ''),
(142, 'South Indian', 'South Indian', 'Paper Dosa', 60, ''),
(143, 'South Indian', 'South Indian', 'Rava Plain Dosa', 60, ''),
(144, 'South Indian', 'South Indian', 'Rava Masala Dosa', 80, ''),
(145, 'South Indian', 'South Indian', 'Onion Plain dosa', 60, ''),
(146, 'South Indian', 'South Indian', 'Onion Masala Dosa', 80, ''),
(147, 'South Indian', 'South Indian', 'Idli Sambhar', 40, '2 piece Idli'),
(148, 'South Indian', 'South Indian', 'Idli Fry', 40, ''),
(149, 'South Indian', 'South Indian', 'Vada Sambhar', 40, '2 Piece Vada'),
(150, 'South Indian', 'South Indian', 'Sada Uttapam', 60, ''),
(151, 'South Indian', 'South Indian', 'Mix Uttapam', 70, ''),
(152, 'South Indian', 'South Indian', 'Onion Uttapam', 80, ''),
(153, 'South Indian', 'South Indian', 'Tomato Uttapam', 80, ''),
(154, 'South Indian', 'South Indian', 'PAnner Uttapam', 100, ''),
(155, 'South Indian', 'South Indian', 'South  Indian Platter', 120, 'Mini Uttapam , Mini Dosa , 1 pc Vada , 1pc Idli , Sambhar'),
(156, 'Bakery', 'Cakes', 'Pineapple Cake', 200, '1 pound'),
(157, 'Bakery', 'Cakes', 'ButterScotch Cake', 200, '1 Pound'),
(158, 'Bakery', 'Cakes', 'Strawberry Cake', 200, '1 Pound'),
(159, 'Bakery', 'Cakes', 'Blueberry Cake', 200, '1 Pound'),
(160, 'Bakery', 'Cakes', 'Cassata Cake', 200, '1 Pound'),
(161, 'Bakery', 'Cakes', 'Mix Fruit Cake', 250, '1 Pound'),
(162, 'Bakery', 'Cakes', 'Choco Truffle Cake', 250, '1 Pound'),
(163, 'Bakery', 'Cakes', 'Black Forest Cake', 250, '1 Pound'),
(164, 'Bakery', 'Cakes', 'Choco Crunch Cake', 250, '1 Pound'),
(165, 'Bakery', 'Cakes', 'Choco Nuts Cake', 250, '1 Pound'),
(166, 'Bakery', 'Cakes', 'Choco Chips Cake', 250, '1 Pound'),
(167, 'Bakery', 'Cakes', 'Kit Ket Cake', 250, ''),
(168, 'Bakery', 'Cakes', 'Oreo Cake', 250, '1 Pound'),
(169, 'Bakery', 'Pastry', 'Black Forest Pastry', 50, ''),
(170, 'Bakery', 'Pastry', 'Pineapple Pastry', 40, ''),
(171, 'Bakery', 'Pastry', 'Chocolate Pastry', 50, ''),
(172, 'Bakery', 'Pastry', 'Butter Scotch Pastry', 40, ''),
(173, 'Bakery', 'Pastry', 'Strawberry Pastry', 40, ''),
(174, 'Bakery', 'Pastry', 'Blueberry Pastry', 40, ''),
(175, 'Bakery', 'Pastry', 'Red Valvet Pastry', 60, ''),
(176, 'Bakery', 'Cake', 'Red Valvet', 300, '1 pound'),
(177, 'Bakery', 'Cookies', 'Plain Cookie', 65, '300 gm'),
(178, 'Bakery', 'Cookies', 'Ajwain Cookies', 70, '300 gm'),
(179, 'Bakery', 'Cookies', 'Jeera Cookies', 75, '300 gm'),
(180, 'Bakery', 'Cookies', 'Almond Cookies', 100, '300 gm'),
(181, 'Bakery', 'Cookies', 'Kaju Cookies', 100, '300 gm'),
(182, 'Bakery', 'Cookies', 'American Cookies', 120, '300 gm'),
(183, 'Bakery', 'Cookies', 'Chocolate Cookies', 80, '300 gm'),
(184, 'Bakery', 'Cookies', 'Coconut Cookies', 75, '300 gm'),
(185, 'Bakery', 'Cookies', 'Nan Khatai', 70, '300 gm'),
(186, 'Bakery', 'Cookies', 'Cake Rusk', 80, '300 gm'),
(187, 'Bakery', 'Cookies', 'Jam Cookies', 90, '300 gm'),
(188, 'Bakery', 'Quick Bites', 'Veg Puff', 15, ''),
(189, 'Bakery', 'Quick Bites', 'Paneer Puff', 25, ''),
(190, 'Bakery', 'Quick Bites', 'Cheese Patty', 25, ''),
(191, 'Bakery', 'Quick Bites', 'Rajeshthani  Patty', 25, ''),
(192, 'Bakery', 'Quick Bites', 'Chinese Patty', 20, ''),
(193, 'Bakery', 'Quick Bites', 'Corn Patty', 20, ''),
(194, 'Bakery', 'Quick Bites', 'Baked Samosa', 20, ''),
(195, 'Bakery', 'Quick Bites', 'Butter Samosa', 25, ''),
(196, 'Bakery', 'Quick Bites', 'Baked Kachori', 20, ''),
(197, 'Bakery', 'Quick Bites', 'Hotdog', 30, ''),
(198, 'Bakery', 'Quick Bites', 'Cheese Hotdog', 40, ''),
(199, 'Bakery', 'Others', 'Cream Roll', 15, ''),
(200, 'Bakery', 'Others', 'Choco Muffin', 30, ''),
(201, 'Bakery', 'Others', 'Strawberry Muffin', 25, ''),
(202, 'Bakery', 'Others', 'Brownie', 40, ''),
(203, 'Bakery', 'Others', 'Plain Khari', 40, ''),
(204, 'Bakery', 'Others', 'Ajwain Khari', 50, ''),
(205, 'Bakery', 'Others', 'Sandwich Bread', 35, ''),
(206, 'Bakery', 'Others', 'Hod dog bun', 20, '6 Pieces'),
(207, 'Chinese', 'Chinese', 'Veg Noodles', 70, ''),
(208, 'Chinese', 'Chinese', 'Hakka Noodles', 70, ''),
(209, 'Chinese', 'Chinese', 'Plain Noodle', 60, ''),
(210, 'Chinese', 'Chinese', 'Schezwan Noodles', 80, ''),
(211, 'Chinese', 'Chinese', 'Garlic Noodles', 80, ''),
(212, 'Chinese', 'Chinese', 'Noodles with Manchurian', 80, ''),
(213, 'Chinese', 'Chinese', 'Noodle with Paneer', 100, ''),
(214, 'Chinese', 'Chinese', 'Noodle With Rice', 80, ''),
(215, 'Chinese', 'Chinese', 'Manchurian Dry', 70, ''),
(216, 'Chinese', 'Chinese', 'Manchurian Gravy', 70, ''),
(217, 'Chinese', 'Chinese', 'Schezwan Manchurian', 80, ''),
(218, 'Chinese', 'Chinese', 'Garlic Manchurian', 80, ''),
(219, 'Chinese', 'Chinese', 'Chilli Manchurian', 80, ''),
(220, 'Chinese', 'Chinese', 'Manchurian With Paneer', 100, ''),
(221, 'Chinese', 'Chinese', 'Chilli Paneer', 100, ''),
(222, 'Chinese', 'Chinese', 'Schezwan Paneer', 110, ''),
(223, 'Chinese', 'Chinese', 'Garlic Paneer', 110, ''),
(224, 'Chinese', 'Chinese', 'Plain Rice', 60, ''),
(225, 'Chinese', 'Chinese', 'Schezwan Rice', 60, ''),
(226, 'Chinese', 'Chinese', 'Fried Rice', 70, ''),
(227, 'Chinese', 'Chinese', 'Chinese Bhel', 110, ''),
(228, 'Chinese', 'Chinese', 'Veg Lollipop', 70, '3 Pcs'),
(229, 'Chinese', 'Chinese', 'Veg Lollipop ', 110, '6 Pcs'),
(230, 'Chinese', 'Chinese', 'Veg Steamed Momos', 40, ''),
(231, 'Chinese', 'Chinese', 'Veg Fried Momos', 40, ''),
(232, 'Chinese', 'Chinese', 'Paneer Steamed Momos', 50, ''),
(233, 'Chinese', 'Chinese', 'Paneer Fried Momos', 50, ''),
(234, 'Chinese', 'Chinese', 'Cheese Fried Momos', 60, ''),
(235, 'Chinese', 'Chinese', 'Veg Tandoori Momos', 60, ''),
(236, 'Chinese', 'Chinese', 'Paneer Tandoori Momos', 70, ''),
(237, 'Chinese', 'Chinese', 'Soya Momos', 50, ''),
(238, 'Chinese', 'Chinese', 'Soya Tandoori Momos', 60, ''),
(239, 'Sweets', 'Sweets', 'Kaju Katli', 220, '250 gm'),
(240, 'Sweets', 'Sweets', 'Dudh Katli', 100, '250 gm'),
(241, 'Sweets', 'Sweets', 'Motichur Laddu', 100, '250 gm'),
(242, 'Sweets', 'Sweets', 'Kesariya Peda', 100, '250 gm'),
(243, 'Sweets', 'Sweets', 'Mathura Peda', 100, '250 gm'),
(244, 'Sweets', 'Sweets', 'Milk Cake', 100, '250 gm'),
(245, 'Sweets', 'Sweets', 'Gulab Jamun', 80, '250 gm'),
(246, 'Sweets', 'Sweets', 'Rasgulla', 80, '250 gm'),
(247, 'Sweets', 'Sweets', 'Rasmalai', 100, '250 gm'),
(248, 'Sweets', 'Sweets', 'Bengali Sweet', 100, '250 gm'),
(249, 'Sweets', 'Sweets', 'Gup Chup', 100, '250 gm'),
(250, 'Sweets', 'Sweets', 'Shrikhand', 100, '250 gm'),
(251, 'Sweets', 'Sweets', 'Rabdi', 100, '250 gm'),
(252, 'Sweets', 'Sweets', 'Besan Laddu', 100, '250 gm'),
(253, 'Sweets', 'Sweets', 'Khopra Pak', 100, '250 gm'),
(254, 'Sweets', 'Sweets', 'Makhan vada', 80, '250 gm'),
(255, 'Sweets', 'Sweets', 'Dry Fruit Mix Sweet', 240, '250 gm'),
(256, 'Sweets', 'Sweets', 'Mawa Bati', 80, '250 gm'),
(257, 'Sweets', 'Sweets', 'Mysor Pak', 120, '250 gm');

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE IF NOT EXISTS `notification` (
  `notf_no` int(11) NOT NULL AUTO_INCREMENT,
  `notf_data` varchar(500) NOT NULL,
  PRIMARY KEY (`notf_no`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`notf_no`, `notf_data`) VALUES
(1, 'Use the special mansoon Mania for the foodies.Enjoy you meal n order online'),
(5, '20% off on sweet in  this summer'),
(6, 'For great deal go at Combos');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE IF NOT EXISTS `orders` (
  `orderId` bigint(20) NOT NULL AUTO_INCREMENT,
  `userId` varchar(25) NOT NULL,
  `orderItem` varchar(2000) NOT NULL,
  `orderStatus` int(11) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `trxnId` varchar(40) NOT NULL,
  `orderTime` varchar(30) NOT NULL,
  `address` varchar(200) NOT NULL,
  `paymentMode` varchar(20) NOT NULL,
  `deliveryPartnerId` varchar(10) NOT NULL,
  PRIMARY KEY (`orderId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=200216 ;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`orderId`, `userId`, `orderItem`, `orderStatus`, `amount`, `trxnId`, `orderTime`, `address`, `paymentMode`, `deliveryPartnerId`) VALUES
(200202, 'akaushal451', '{"Plain Rice":{"food":"Plain Rice","price":"60.0","noOfItems":2},"Mattar Paneer":{"food":"Mattar Paneer","price":"140.0","noOfItems":2}}', 1, '{"totalAmount": "400", "deliveryCharges": "0", "packingCharges": "0"}', 'temp', 'Sun Apr 26 15:52:50 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Paytm', 'DP356vrahu'),
(200203, 'akaushal451', '{"Plain Rice":{"food":"Plain Rice","price":"60.0","noOfItems":2},"Mattar Paneer":{"food":"Mattar Paneer","price":"140.0","noOfItems":2},"Aloo Gobhi":{"food":"Aloo Gobhi","price":"120.0","noOfItems":1},"Butter Kofta":{"food":"Butter Kofta","price":"120.0","noOfItems":1},"Kaju Paneer":{"food":"Kaju Paneer","price":"160.0","noOfItems":1},"Shahi Paneer":{"food":"Shahi Paneer","price":"160.0","noOfItems":1},"Paneer Chatpata":{"food":"Paneer Chatpata","price":"160.0","noOfItems":1},"Kadhai Paneer":{"food":"Kadhai Paneer","price":"160.0","noOfItems":1},"Paneer Bhurji":{"food":"Paneer Bhurji","price":"140.0","noOfItems":1},"Palak Paneer":{"food":"Palak Paneer","price":"140.0","noOfItems":1}}', 0, '{"totalAmount": "1560", "deliveryCharges": "0", "packingCharges": "0"}', 'temp', 'Sun Apr 26 16:17:26 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Paytm', 'DP852bunty'),
(200204, 'akaushal451', '{"Plain Rice":{"food":"Plain Rice","price":"60.0","noOfItems":2},"Mattar Paneer":{"food":"Mattar Paneer","price":"140.0","noOfItems":2}}', 0, '{"totalAmount": "400", "deliveryCharges": "0", "packingCharges": "0"}', 'temp', 'Wed Apr 29 19:03:31 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Paytm', 'DP852bunty'),
(200205, 'akaushal451', '{"Shahi Paneer":{"food":"Shahi Paneer","price":"160.0","noOfItems":1},"Aloo Gobhi":{"food":"Aloo Gobhi","price":"120.0","noOfItems":1},"Fried Rice":{"food":"Fried Rice","price":"110.0","noOfItems":1},"Kashmiri Pulao":{"food":"Kashmiri Pulao","price":"120.0","noOfItems":1}}', 0, '{"totalAmount": "510", "deliveryCharges": "0", "packingCharges": "0"}', 'temp', 'Sat May  2 20:44:36 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Paytm', 'DP356vrahu'),
(200206, 'akaushal451', '{"Shahi Paneer":{"food":"Shahi Paneer","price":"160.0","noOfItems":1},"Aloo Gobhi":{"food":"Aloo Gobhi","price":"120.0","noOfItems":2},"Fried Rice":{"food":"Fried Rice","price":"110.0","noOfItems":1},"Kashmiri Pulao":{"food":"Kashmiri Pulao","price":"120.0","noOfItems":1}}', 0, '{"totalAmount": "630", "deliveryCharges": "0", "packingCharges": "0"}', '20200502111212800110168769501502890', 'Sat May  2 20:59:21 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Paytm', 'DP863ravik'),
(200207, 'akaushal451', '{"Kashmiri Pulao":{"food":"Kashmiri Pulao","price":"120.0","noOfItems":1},"Tomato Masala":{"food":"Tomato Masala","price":"100.0","noOfItems":1},"Sev Tamater":{"food":"Sev Tamater","price":"120.0","noOfItems":1},"Bhindi Masala":{"food":"Bhindi Masala","price":"120.0","noOfItems":1},"Butter Kofta":{"food":"Butter Kofta","price":"120.0","noOfItems":1},"Malai Kofta":{"food":"Malai Kofta","price":"140.0","noOfItems":1}}', 0, '{"totalAmount": "720", "deliveryCharges": "0", "packingCharges": "0"}', '20200502111212800110168770801507312', 'Sat May  2 21:13:48 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Paytm', 'DP852bunty'),
(200208, 'akaushal451', '{"Sev Tamater":{"food":"Sev Tamater","price":"120.0","noOfItems":1},"Bhindi Masala":{"food":"Bhindi Masala","price":"120.0","noOfItems":1},"Butter Kofta":{"food":"Butter Kofta","price":"120.0","noOfItems":1},"Malai Kofta":{"food":"Malai Kofta","price":"140.0","noOfItems":1}}', 0, '{"totalAmount": "500", "deliveryCharges": "0", "packingCharges": "0"}', '20200502111212800110168783501528600', 'Sat May  2 21:16:44 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Paytm', 'DP863ravik'),
(200209, 'akaushal451', '{"Sev Tamater":{"food":"Sev Tamater","price":"120.0","noOfItems":1},"Bhindi Masala":{"food":"Bhindi Masala","price":"120.0","noOfItems":1},"Butter Kofta":{"food":"Butter Kofta","price":"120.0","noOfItems":1},"Malai Kofta":{"food":"Malai Kofta","price":"140.0","noOfItems":1}}', 0, '{"totalAmount": "500", "deliveryCharges": "0", "packingCharges": "0"}', '20200502111212800110168792101508107', 'Sat May  2 21:39:14 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Paytm', 'DP863ravik'),
(200210, 'akaushal451', '{"Sev Tamater":{"food":"Sev Tamater","price":"120.0","noOfItems":1},"Bhindi Masala":{"food":"Bhindi Masala","price":"120.0","noOfItems":1},"Butter Kofta":{"food":"Butter Kofta","price":"120.0","noOfItems":1},"Malai Kofta":{"food":"Malai Kofta","price":"140.0","noOfItems":1}}', 0, '{"totalAmount": "500", "deliveryCharges": "0", "packingCharges": "0"}', '20200502111212800110168013201500532', 'Sat May  2 21:40:34 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Paytm', 'DP326gupta'),
(200211, 'akaushal451', '{"Sev Tamater":{"food":"Sev Tamater","price":"120.0","noOfItems":1},"Bhindi Masala":{"food":"Bhindi Masala","price":"120.0","noOfItems":1},"Butter Kofta":{"food":"Butter Kofta","price":"120.0","noOfItems":1},"Malai Kofta":{"food":"Malai Kofta","price":"140.0","noOfItems":1}}', 0, '{"totalAmount": "500", "deliveryCharges": "0", "packingCharges": "0"}', '20200502111212800110168025302923150', 'Sat May  2 21:41:53 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Paytm', 'DP326gupta'),
(200212, 'akaushal451', '{"Malai Kofta":{"food":"Malai Kofta","price":"140.0","noOfItems":1}}', 0, '{"totalAmount": "140", "deliveryCharges": "60", "packingCharges": "0"}', '20200502111212800110168031301499575', 'Sat May  2 21:52:22 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Net Banking', 'DP356vrahu'),
(200213, 'akaushal451', '{"Malai Kofta":{"food":"Malai Kofta","price":"140.0","noOfItems":1}}', 1, '{"totalAmount": "140", "deliveryCharges": "60", "packingCharges": "0"}', '20200502111212800110168040901655668', 'Sat May  2 22:02:50 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Net Banking', ' DP326gupt'),
(200214, 'abhikoushal10', '{"Bhindi Masala":{"food":"Bhindi Masala","price":"120.0","noOfItems":1},"Butter Khichdi":{"food":"Butter Khichdi","price":"120.0","noOfItems":1},"Shahi Pulao":{"food":"Shahi Pulao","price":"120.0","noOfItems":1}}', 1, '{"totalAmount": "360", "deliveryCharges": "0", "packingCharges": "0"}', '20200503111212800110168051901508682', 'Sun May  3 11:14:17 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Net Banking', 'DP326gupta'),
(200215, 'abhikoushal10', '{"Shahi Pulao":{"food":"Shahi Pulao","price":"120.0","noOfItems":1}}', 1, '{"totalAmount": "120", "deliveryCharges": "60", "packingCharges": "0"}', '20200503111212800110168065601493550', 'Sun May  3 11:23:30 2020', '{"doorNo":"39","area":"Kandilpura","city":"Indore","pincode":"452006","landmark":"Gokulganj"}', 'Net Banking', 'DP863ravik');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE IF NOT EXISTS `payment` (
  `orderId` varchar(10) NOT NULL,
  `trxnId` varchar(40) NOT NULL,
  `trxnAmount` varchar(10) NOT NULL,
  `paymentMode` varchar(10) NOT NULL,
  `trxnDate` varchar(25) NOT NULL,
  `bankName` varchar(40) NOT NULL,
  `bankTrxnId` varchar(20) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`orderId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`orderId`, `trxnId`, `trxnAmount`, `paymentMode`, `trxnDate`, `bankName`, `bankTrxnId`, `status`) VALUES
('200209', '20200502111212800110168792101508107', '500.00', 'CC', '2020-05-02 21:37:51.0', 'Bank of Bahrain and Kuwait', '777001703158516', 'TXN_SUCCES'),
('200210', '20200502111212800110168013201500532', '500.00', 'NB', '2020-05-02 21:40:14.0', 'ICICI', '16916106635', 'TXN_SUCCES'),
('200211', '20200502111212800110168025302923150', '500.00', 'NB', '2020-05-02 21:41:16.0', 'PNB', '12963863741', 'TXN_FAILUR'),
('200212', '20200502111212800110168031301499575', '200.00', 'NB', '2020-05-02 21:51:52.0', 'PSB', '11966507629', 'TXN_SUCCES'),
('200213', '20200502111212800110168040901655668', '200.00', 'NB', '2020-05-02 22:02:32.0', 'SBI', '14103019592', 'TXN_SUCCES'),
('200214', '20200503111212800110168051901508682', '360.00', 'NB', '2020-05-03 11:14:01.0', 'HDFC', '12260656946', 'TXN_SUCCES'),
('200215', '20200503111212800110168065601493550', '180.00', 'NB', '2020-05-03 11:22:59.0', 'CITIUB', '11138454828', 'TXN_FAILUR');

-- --------------------------------------------------------

--
-- Table structure for table `ratting`
--

CREATE TABLE IF NOT EXISTS `ratting` (
  `userId` varchar(25) NOT NULL,
  `rate` float NOT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ratting`
--

INSERT INTO `ratting` (`userId`, `rate`, `feedback`) VALUES
('aakashh91', 2, ''),
('abhikoushal', 5, ''),
('akaushal', 4, ''),
('akaushal451', 2.75, 'dkfmgk'),
('amanmishra1319', 2, ''),
('anshjain31', 1, ''),
('ayquq12', 2, ''),
('gagany381', 3, ''),
('jainparam242', 5, ''),
('jayrathore34', 4, 'ejrnnds'),
('rahulverma412', 1, ''),
('sourabh52125', 3, '');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE IF NOT EXISTS `registration` (
  `userId` varchar(20) NOT NULL,
  `name` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(20) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `city` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `role` varchar(10) NOT NULL,
  `status` int(11) NOT NULL,
  `dt` varchar(20) NOT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`userId`, `name`, `email`, `password`, `address`, `mobile`, `city`, `gender`, `role`, `status`, `dt`) VALUES
('2', '', 'aman134@gmail.com', 'aman@123', 'Vrandavan Colony', '7828123456', 'Indore', 'male', 'user', 1, 'Tue Jul 23 11:20:13 '),
('3', 'admin', 'admin@gmail.com', 'admin@123', 'admin ka ghr', '7894561230', 'Mumbai', 'female', 'admin', 1, 'Tue Jul 23 11:21:12 '),
('abhikoushal10', 'Abhishek koushal', 'abhikoushal10@gmail.com', 'koushal', 'Kandilpura', '8109113079', 'Indore', 'male', 'user', 1, 'Tue Apr  7 15:25:51 '),
('akaushal451', 'Abhishek', 'akaushal451@gmail.com', 'akaushal', 'BAda Ganpatai', '7894561230', 'Indore', 'male', 'user', 1, 'Tue Apr  7 19:50:29 ');

-- --------------------------------------------------------

--
-- Table structure for table `subcatagory`
--

CREATE TABLE IF NOT EXISTS `subcatagory` (
  `subcatid` varchar(15) NOT NULL,
  `catnm` varchar(20) NOT NULL,
  `subcatnm` varchar(20) NOT NULL,
  `subcaticon` varchar(1000) NOT NULL,
  PRIMARY KEY (`subcatid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subcatagory`
--

INSERT INTO `subcatagory` (`subcatid`, `catnm`, `subcatnm`, `subcaticon`) VALUES
('Caksek487', 'Bakery', 'Cakes', 'cake.jpeg'),
('Chiese703', 'Chinese', 'Chinese', 'chineseSub.jpg'),
('Coosei717', 'Bakery', 'Cookies', 'cookies.jpg'),
('IndAcctne463', 'Indian', 'Accomplishment', 'Indian_Accomplishment.jpg'),
('IndBevseg916', 'Indian', 'Beverages', 'Indian_Bevegers.jpg'),
('IndDallaD273', 'Indian', 'Dal', 'Indian_dal.jpg'),
('IndDesstr845', 'Indian', 'Desserts', 'Indian_Dessert.jpg'),
('IndInddae105', 'Indian', 'Indian Bread', 'Indian_Roti.jpg'),
('IndIndgeV917', 'Indian', 'Indian Veg', 'Indian_Sabji.jpg'),
('IndRiceci387', 'Indian', 'Rice', 'Indian_rice.jpg'),
('IndThasei714', 'Indian', 'Thalies', 'Indian_thali.jpg'),
('Othsre629', 'Bakery', 'Others', 'others.jpg'),
('Pasyrt643', 'Bakery', 'Pastry', 'pastry.jpeg'),
('Quiset44', 'Bakery', 'Quick Bites', 'snakes.jpg'),
('Rajina137', 'Rajeshthani', 'Rajeshthani', 'DalBati.jpg'),
('Sounai158', 'South Indian', 'South Indian', 'biryani_.jpg'),
('Sweste635', 'Sweets', 'Sweets', 'Barfi.jpg');
