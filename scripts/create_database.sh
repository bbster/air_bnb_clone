--- Docker Run 이후

"""
psql -U postgres - postgres 접속
"""

--- DATABASE 생성
CREATE DATABASE air_bnb_db;

--- User 생성
CREATE USER bnb WITH PASSWORD '1r2r3r4r';
ALTER ROLE bnb SET client_encoding TO 'utf8';
ALTER ROLE bnb SET default_transaction_isolation TO 'read committed';
ALTER ROLE bnb WITH SUPERUSER;

--- DB에 대한 User 권한 부여
GRANT ALL PRIVILEGES ON DATABASE air_bnb_db TO bnb;