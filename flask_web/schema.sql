drop table if exists web_data;
create table web_data (
  id integer primary key autoincrement,
  temperature REAL not null,
  wet REAL not null
  c_time text not null
);


drop table if EXISTS from_data;
create table from_data (
    id integer primary key autoincrement,
    temperature REAL not null,
    wet REAL not null,
    c_time text not null
)

drop table if EXISTS num;
create table num (
    id integer primary key autoincrement,
    c_time text not null
)