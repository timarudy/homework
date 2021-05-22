--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.actors (
    name character varying(255),
    last_name character varying(255)
);


--
-- Name: movies; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.movies (
    name character varying(255),
    jenre character varying(255)
);


--
-- Name: producers; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.producers (
    name character varying(255),
    last_name character varying(255)
);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.actors (name, last_name) FROM stdin;
Timmy	McGhost
Bill	Murrey
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.movies (name, jenre) FROM stdin;
Star Wars	Fantasy
Deadpool	Action
\.


--
-- Data for Name: producers; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.producers (name, last_name) FROM stdin;
Quenty	Tarantino
Buen	Defo
\.


--
-- PostgreSQL database dump complete
--

