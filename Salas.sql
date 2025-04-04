CREATE DATABASE IF NOT EXISTS PEPS;
CREATE USER 'user'@'%' IDENTIFIED BY 'userpw';
GRANT ALL PRIVILEGES ON PEPS.* TO 'user'@'%';
FLUSH PRIVILEGES;
USE PEPS;
CREATE TABLE salas(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
	foto VARCHAR(255)
);
CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    fechaUltimoAcceso DATE,
    fechaBloqueo DATE,
    numeroAccesosErroneo INTEGER,
    debeCambiarClave BOOLEAN
);
INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`,`estado`, `correo`,`numeroAccesosErroneo`,`fechaUltimoAcceso`) VALUES ('root','$10$hJtLt4u0SqSf.h3S5Uuev.nu98ARhn.6SpvFCYbc1eeynJmy81cmK', 'admin', 'activo','root@pp.es', 0, '2022-03-01 00:00');