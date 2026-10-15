-- Todo List 테이블 생성 DDL (MySQL)
CREATE DATABASE IF NOT EXISTS todo_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE todo_db;

CREATE TABLE `todo_todo` (
    `id`           BIGINT       NOT NULL AUTO_INCREMENT,
    `title`        VARCHAR(200) NOT NULL,
    `content`      LONGTEXT     NULL,
    `is_completed` TINYINT(1)   NOT NULL DEFAULT 0,
    `created_at`   DATETIME(6)  NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
