create table department(
dept_id varchar(10),
dept_name varchar(15),
primary key (dept_id));

create table employee(
name varchar(15),
emp_id varchar(10),
dept_id varchar(10),
role varchar(10),
address text,
aadhaar bigint(12) unique,
primary key(emp_id),
foreign key (dept_id) references department(dept_id) on delete cascade);

create table Patient(
p_id varchar(8),
name varchar(15),
aadhaar bigint(12),
dob date,
mobile bigint(10),
email varchar(50),
address varchar(50),
Insurence_id varchar(15),
sex char(1),
primary key (p_id,Insurence_id));

create table Room(
r_no varchar(5),
r_type varchar(8),
b_name varchar(2),
b_no int(2),
primary key(r_no));

create table affiliated(
p_id varchar(8),
emp_id varchar(10),
r_no varchar(5),
status varchar(3),
DOA date,
DOD date,
foreign key (p_id) references patient(p_id) on delete cascade,
foreign key (emp_id) references employee(emp_id) on delete cascade,
foreign key (r_no) references room(r_no) on delete cascade);


create table precription(
emp_id varchar(10),
p_id varchar(8),
MEDication_name varchar(16),
dose varchar(5),
foreign key (p_id) references patient(p_id) on delete cascade,
foreign key (emp_id) references employee(emp_id) on delete cascade);

create table procedur(
pro_id varchar(8),
name varchar(10),
decription text,
cost int(9),
primary key(pro_id));

create table undergo(
emp_id varchar(10),
p_id varchar(8),
pro_id varchar(8),
r_no varchar(5),
sedu_date date,
foreign key (p_id) references patient(p_id) on delete cascade,
foreign key (emp_id) references employee(emp_id) on delete cascade,
foreign key (pro_id) references procedur(pro_id) on delete cascade,
foreign key (r_no) references Room(r_no) on delete cascade);

create table appointment(
a_no INT AUTO_INCREMENT PRIMARY KEY,
p_id varchar(8),
time datetime,
emp_id varchar(8),
phone_no bigint(10),
foreign key (p_id) references patient(p_id) on delete cascade,
foreign key (emp_id) references employee(emp_id) on delete cascade);

