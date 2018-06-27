-- lists all the cities of California
-- that can be found in the database hbtn_0d_usa
SELECT  cities.id,cities.name FROM hbtn_0d_usa.states ,hbtn_0d_usa.cities WHERE cities.state_id=states.id ORDER BY cities.id;
