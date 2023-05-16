-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2023 at 02:14 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bdprueba`
--

-- --------------------------------------------------------

--
-- Table structure for table `incursiones`
--

CREATE TABLE `incursiones` (
  `Identificador` int(255) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` text COLLATE utf8_spanish_ci NOT NULL,
  `imagen` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` datetime NOT NULL,
  `localizacion` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `linklocalizacion` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `lider` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `minparticipantes` int(3) NOT NULL,
  `participantesactuales` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `incursiones`
--

INSERT INTO `incursiones` (`Identificador`, `nombre`, `descripcion`, `imagen`, `fecha`, `localizacion`, `linklocalizacion`, `lider`, `minparticipantes`, `participantesactuales`) VALUES
(1, 'Incursión Playa de Marenys de Rafalcaid ', 'Esta es la descripción para la Incursión a la Playa de Marenys de Rafalcaid.', 'playacontaminada .jpeg', '2023-05-22 11:00:00', 'Playa de Marenys de Rafalcaid\nCarrer de Rafalcaid, 46730 Gandia, Valencia', 'https://goo.gl/maps/EBVrgEVYczpMGhkW6', 'joanbt', 10, 1),
(2, 'Incursión El Portalet', 'Esta es la descripción para la Incursión a el Portalet.', 'montañacontaminada.jpg', '2023-06-08 09:00:00', 'El Portalet (SL-CV80)\r\n46728 Gandia, Valencia', 'https://goo.gl/maps/2suVziycb9tPbGrZ7', 'joanbt', 15, 4),
(3, 'Incursión Mirador de las Aves', 'Esta es la descripción para la Incursión a el Mirador de las Aves.', 'montañacontaminada4.jpg', '2023-05-24 17:00:00', 'Mirador de las Aves\nPlaça Poligono 07, 2, 46770, Valencia', 'https://goo.gl/maps/pRA2EV4DhtdfxHv26', 'victoriacm', 8, 3),
(4, 'Incursión Fuente del Mondúver', 'Esta es la descripción para la Incursión a la Fuente del Mondúver.', 'montañacontaminada3.jpg', '2023-06-02 10:00:00', 'Fuente del Mondúver\r\n46790 Xeresa, Valencia', 'https://goo.gl/maps/dXQEZt4PDqUuFwCu8', 'adriandb', 6, 3),
(5, 'Incursión Torradores Marxuquera', 'Esta es la descripción para la Incursión a los Torradores de Marxuquera.', 'montañacontaminada2.jpg', '2023-05-28 18:00:00', 'Torradores Marxuquera\r\nCarrer Cami Vell de Pinet, 43, 46728 Gandia, Valencia', 'https://goo.gl/maps/1SGYYAeoNGXjAjUF7', 'joanbt', 10, 4);

-- --------------------------------------------------------

--
-- Table structure for table `incursionespersonales`
--

CREATE TABLE `incursionespersonales` (
  `Identificador` int(255) NOT NULL,
  `id_incursion` int(255) NOT NULL,
  `id_usuario` int(255) NOT NULL,
  `cargo` varchar(30) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `incursionespersonales`
--

INSERT INTO `incursionespersonales` (`Identificador`, `id_incursion`, `id_usuario`, `cargo`) VALUES
(1, 1, 1, 'líder'),
(2, 2, 1, 'líder'),
(3, 2, 2, 'incursionista'),
(4, 2, 5, 'incursionista'),
(5, 2, 8, 'incursionista'),
(6, 3, 3, 'líder'),
(7, 3, 2, 'incursionista'),
(8, 3, 7, 'incursionista'),
(9, 4, 2, 'líder'),
(10, 4, 4, 'incursionista'),
(11, 4, 6, 'incursionista'),
(12, 5, 1, 'líder'),
(13, 5, 3, 'incursionista'),
(14, 5, 7, 'incursionista'),
(15, 5, 8, 'incursionista');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `Identificador` int(255) NOT NULL,
  `nombre` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `apellidos` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `usuario` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `contrasena` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `incursionescompletadas` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`Identificador`, `nombre`, `apellidos`, `email`, `usuario`, `contrasena`, `incursionescompletadas`) VALUES
(1, 'Joan', 'Bañuls Torres', 'joanbanyulstorres@gmail.com', 'joanbt', 'joanbt', 3),
(2, 'Adrian', 'Dos Santos Baeza', 'adriandossantosbaeza@gmail.com', 'adriandb', 'adriandb', 2),
(3, 'Victoria', 'Cuadros Mansilla', 'victoriacuadrosmansilla@gmail.com', 'victoriacm', 'victoriacm', 5),
(4, 'Lucia', 'Ruz Real', 'luciaruzreal@gmail.com', 'luciarr', 'luciarr', 1),
(5, 'Noelia', 'Vasquez Villalba', 'noeliavasquezvillalba@gmail.com', 'noeliavv', 'noeliavv', 0),
(6, 'Guillermo', 'Georgieva Palencia', 'guillermogeorgievapalencia@gmail.com', 'guillermogp', 'guillermogp', 0),
(7, 'Antonio', 'Jara Zabaleta', 'antoniojarazabaleta@gmail.com', 'antoniojz', 'antoniojz', 0),
(8, 'Natalia', 'Galisteo Hernan', 'nataliagalisteohernan@gmail.com', 'nataliagh', 'nataliagh', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `incursiones`
--
ALTER TABLE `incursiones`
  ADD PRIMARY KEY (`Identificador`);

--
-- Indexes for table `incursionespersonales`
--
ALTER TABLE `incursionespersonales`
  ADD PRIMARY KEY (`Identificador`),
  ADD KEY `Relacion` (`id_incursion`),
  ADD KEY `Relacion2` (`id_usuario`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`Identificador`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `incursiones`
--
ALTER TABLE `incursiones`
  MODIFY `Identificador` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `incursionespersonales`
--
ALTER TABLE `incursionespersonales`
  MODIFY `Identificador` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `Identificador` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `incursionespersonales`
--
ALTER TABLE `incursionespersonales`
  ADD CONSTRAINT `Relacion` FOREIGN KEY (`id_incursion`) REFERENCES `incursiones` (`Identificador`),
  ADD CONSTRAINT `Relacion2` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`Identificador`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
