insert into department values ('10','General');
insert into department values ('11','Cardiology');
insert into department values ('12','Oncology');
insert into department values ('13','Emergency');
insert into department values ('14','Radiology');

insert into employee values('Ramesh','10001','10','Doctor','Ujire',563516627192);
insert into employee values('Suresh','10002','10','Surgon','Mangalore',987268233583);
insert into employee values('Pavitra','12002','12','Nurse','Belal',094296161903);
insert into employee values('Satisha','13003','13','Doctor','Kolli',554694914098);
insert into employee values('Adheesh','11006','11','Surgon','Kakinje',893869084021);
insert into employee values('Dhruti','11009','11','Doctor','Kakinje',387183909182);

insert into employee values('Neha','10016','11','Doctor','Ujire',765432109876);
insert into employee values('Rajesh','10017','14','Surgeon','Ujire',654321098765);
insert into employee values('Ananya','10018','14','Nurse','Ujire',543210987654);
insert into employee values('Sanjay','10019','13','Doctor','Ujire',432109876543);
insert into employee values('Priyanka','10020','13','Nurse','Ujire',321098765432);
insert into employee values('Akash','10021','12','Surgeon','Ujire',210987654321);
insert into employee values('Shweta','10022','11','Doctor','Ujire',109876543210);   
insert into employee values('Vivek','10023','12','Nurse','Ujire',98765432109);
insert into employee values('Anita','10024','10','Doctor','Ujire',87654321098);
insert into employee values('Aryan','10025','12','Nurse','Ujire',76543210987);


insert into Patient values('50021','Anil',123456789012,'1999-04-11',1787849870,'123@123.com','Kasaragodu','10021','M');
insert into Patient values('50022','Anu',064763463265,'1987-01-31',0608217811,'644@233.com','Mangaluru','12777','F');
insert into Patient values('50034','Kantappa',027695057474,'1989-05-25',5687783133,'123@sdaf.com','Bengaluru','92371','M');
insert into Patient values('50045','Kattapa',880812882641,'2000-02-01',7500203548,'asas@gmail.com','Belgavi','88271','M');
insert into Patient values('50078','Rahulla',555521976991,'1997-07-22',1541438563,'2sfdjs@2173.in','Belgaluru','73891','M');
insert into Patient values('50079','Prakash',987456321456,'1998-12-05',9448983156,'sadasd@asd.in','Nada','73897','M');

insert into Room values('1101','Regular','Pi',1);
insert into Room values('1102','Sregular','Pi',1);
insert into Room values('1103','Premium','Pi',1);
insert into Room values('1201','General','Pi',2);
insert into Room values('1202','Delux','Pi',2);

insert into affiliated values('50021','10002','1101','A','2001-01-01','2001-02-01');
insert into affiliated values('50022','10002','1102','A','2001-02-23','2001-03-17');
insert into affiliated values('50034','10001','1103','D','2003-06-24','2003-07-24');
insert into affiliated values('50045','11006','1201','A','2004-05-11','2004-05-15');
insert into affiliated values('50078','13003','1202','D','2004-04-09','2004-04-13');
insert into affiliated values('50079','13003','1201','D','2004-06-08','2004-06-20');


insert into precription values('10002','50021','Paracitamol','1-0-1');
insert into precription values('10001','50034','Rantac','1-1-1');
insert into precription values('13003','50078','Glycomol','0-0-1');
insert into precription values('11006','50045','Aten','1-1-1');

insert into procedur values('60001','X-ray','as',1900);
insert into procedur values('60002','MRI','df',8000);
insert into procedur values('60003','Angeoplast','gh',19000);
insert into procedur values('60004','GMedicine','jk',200);
insert into procedur values('60005','Ultrasound','li',1000);
insert into procedur values('60007','Chemo','li',100600);

insert into undergo values('10002','50021','60001','1101','2001-01-02');
insert into undergo values('10001','50034','60002','1103','2004-06-27');
insert into undergo values('13003','50078','60003','1202','2004-04-15');
insert into undergo values('11006','50045','60004','1201','2004-05-11');
insert into undergo values('10002','50021','60005','1101','2001-01-02');
insert into undergo values('10002','50021','60007','1101','2001-01-02');
insert into undergo values('10002','50021','60007','1101','2024-03-03');

insert into appointment values(1,50021,'24-03-12 03:15','10001',1234567890);
INSERT INTO appointment (p_id, time, emp_id, phone_no)
VALUES ('50078', '24-03-12 13:00:00', '10002', 0987654321);
INSERT INTO appointment (p_id, time, emp_id, phone_no)
VALUES ('50045', '24-03-12 15:00:00', '10002', 0987654321);
INSERT INTO appointment (p_id, time, emp_id, phone_no)
VALUES ('50045', '24-03-12 16:00:00', '12002', 0987654321);
DELIMITER //

CREATE TRIGGER prevent_duplicate_appointments
BEFORE INSERT ON appointment
FOR EACH ROW
BEGIN
    DECLARE app_count INT;

    SELECT COUNT(*) INTO app_count
    FROM appointment
    WHERE p_id = NEW.p_id AND time = NEW.time;

    IF app_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Patient already has an appointment at this time';
    END IF;
END;
//

DELIMITER ;


