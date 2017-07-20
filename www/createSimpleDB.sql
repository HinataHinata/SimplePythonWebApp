-- createSimpleDB.sql
-- 执行口令 mysql -u root -p < + sql文件目录。注意⚠️ < 符号要带着

drop database if exists simple;
create database simple;
use simple;

grant select,insert,update,delete on simple.* to 'www-data'@'localhost' identified by 'www-data';

create table users(
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `create_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_create_at` (`create_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table blogs(
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_iamge` varchar(500) not null,
    `name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `create_at` real not null,
    key `idx_create_at` (`create_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table comments(
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `content` mediumtext not null,
    `create_at` real not null,
    key `idx_create_at` (`create_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;



