create database jobs_for_flask;
use jobs_for_flask;

create table jobs(
id int primary key ,
title varchar(250) not null,
location varchar(250) not null,
salary int ,
currency varchar(15),
responsibilities varchar(2000),
requirements varchar(2000)
);


create table application(
AID int primary key ,
JID INT ,
FULL_NAME varchar(50),
Email varchar(70),
Linkedin_URL varchar(200),
Education varchar(500),
Work_Experience varchar(500),
foreign key (JID) references jobs(id) 
);

ALTER TABLE application MODIFY AID int AUTO_INCREMENT;



create table courses(
CID int primary key,
Instructor varchar(200),
filed varchar(200),
price int );



create table events_for_site(
EID int primary key,
organizer varchar(200),
about varchar(200),
location varchar(200) ,
date_for_event date);


create  table users(
user varchar(100),
password varchar(100),
email varchar(100));


insert into jobs
values (1,"Data Analyst","USA",15000,"$","Data Collection and Extraction , Data Cleaning and Preparation , Data Analysis,Data Visualization","Educational Background,Technical Skills,Analytical Skills");


insert into events_for_site
values(2,"DR.Rami","Networks","cairo,helwan",'2024-09-12');


insert into courses
values(2,"DR.Hossam","introduction to clouding",1500);