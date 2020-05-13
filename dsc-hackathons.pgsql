--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

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
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    id integer NOT NULL,
    name character varying,
    description character varying
);


ALTER TABLE public.category OWNER TO postgres;

--
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_id_seq OWNER TO postgres;

--
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_id_seq OWNED BY public.category.id;


--
-- Name: hackathon; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hackathon (
    id integer NOT NULL,
    name character varying,
    start_time timestamp with time zone,
    end_time timestamp with time zone,
    place_name character varying,
    status_id integer
);


ALTER TABLE public.hackathon OWNER TO postgres;

--
-- Name: hackathon_category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hackathon_category (
    id integer NOT NULL,
    hackathon_id integer,
    category_id integer
);


ALTER TABLE public.hackathon_category OWNER TO postgres;

--
-- Name: hackathon_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hackathon_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hackathon_category_id_seq OWNER TO postgres;

--
-- Name: hackathon_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hackathon_category_id_seq OWNED BY public.hackathon_category.id;


--
-- Name: hackathon_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hackathon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hackathon_id_seq OWNER TO postgres;

--
-- Name: hackathon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hackathon_id_seq OWNED BY public.hackathon.id;


--
-- Name: hackathon_item; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hackathon_item (
    id integer NOT NULL,
    hackathon_id integer,
    item_id integer,
    available boolean
);


ALTER TABLE public.hackathon_item OWNER TO postgres;

--
-- Name: hackathon_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hackathon_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hackathon_item_id_seq OWNER TO postgres;

--
-- Name: hackathon_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hackathon_item_id_seq OWNED BY public.hackathon_item.id;


--
-- Name: hackathon_workshop; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hackathon_workshop (
    id integer NOT NULL,
    hackathon_id integer,
    workshop_id integer,
    event_description character varying
);


ALTER TABLE public.hackathon_workshop OWNER TO postgres;

--
-- Name: hackathon_workshop_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hackathon_workshop_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hackathon_workshop_id_seq OWNER TO postgres;

--
-- Name: hackathon_workshop_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hackathon_workshop_id_seq OWNED BY public.hackathon_workshop.id;


--
-- Name: item; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.item (
    id integer NOT NULL,
    name character varying,
    description character varying
);


ALTER TABLE public.item OWNER TO postgres;

--
-- Name: item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_id_seq OWNER TO postgres;

--
-- Name: item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.item_id_seq OWNED BY public.item.id;


--
-- Name: status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.status (
    id integer NOT NULL,
    name character varying,
    description character varying
);


ALTER TABLE public.status OWNER TO postgres;

--
-- Name: status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.status_id_seq OWNER TO postgres;

--
-- Name: status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.status_id_seq OWNED BY public.status.id;


--
-- Name: workshop; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.workshop (
    id integer NOT NULL,
    name character varying,
    speaker_name character varying,
    participants integer,
    duration character varying,
    speaker_phone character varying
);


ALTER TABLE public.workshop OWNER TO postgres;

--
-- Name: workshop_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.workshop_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workshop_id_seq OWNER TO postgres;

--
-- Name: workshop_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.workshop_id_seq OWNED BY public.workshop.id;


--
-- Name: category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category ALTER COLUMN id SET DEFAULT nextval('public.category_id_seq'::regclass);


--
-- Name: hackathon id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon ALTER COLUMN id SET DEFAULT nextval('public.hackathon_id_seq'::regclass);


--
-- Name: hackathon_category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_category ALTER COLUMN id SET DEFAULT nextval('public.hackathon_category_id_seq'::regclass);


--
-- Name: hackathon_item id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_item ALTER COLUMN id SET DEFAULT nextval('public.hackathon_item_id_seq'::regclass);


--
-- Name: hackathon_workshop id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_workshop ALTER COLUMN id SET DEFAULT nextval('public.hackathon_workshop_id_seq'::regclass);


--
-- Name: item id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item ALTER COLUMN id SET DEFAULT nextval('public.item_id_seq'::regclass);


--
-- Name: status id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.status ALTER COLUMN id SET DEFAULT nextval('public.status_id_seq'::regclass);


--
-- Name: workshop id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workshop ALTER COLUMN id SET DEFAULT nextval('public.workshop_id_seq'::regclass);


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (id, name, description) FROM stdin;
\.


--
-- Data for Name: hackathon; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hackathon (id, name, start_time, end_time, place_name, status_id) FROM stdin;
\.


--
-- Data for Name: hackathon_category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hackathon_category (id, hackathon_id, category_id) FROM stdin;
\.


--
-- Data for Name: hackathon_item; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hackathon_item (id, hackathon_id, item_id, available) FROM stdin;
\.


--
-- Data for Name: hackathon_workshop; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hackathon_workshop (id, hackathon_id, workshop_id, event_description) FROM stdin;
\.


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.item (id, name, description) FROM stdin;
\.


--
-- Data for Name: status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.status (id, name, description) FROM stdin;
1	Pending	Submitted application
2	Approved	Application approved
3	Rejected	Application rejected
\.


--
-- Data for Name: workshop; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.workshop (id, name, speaker_name, participants, duration, speaker_phone) FROM stdin;
\.


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_id_seq', 1, false);


--
-- Name: hackathon_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hackathon_category_id_seq', 1, false);


--
-- Name: hackathon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hackathon_id_seq', 1, false);


--
-- Name: hackathon_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hackathon_item_id_seq', 1, false);


--
-- Name: hackathon_workshop_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hackathon_workshop_id_seq', 1, false);


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.item_id_seq', 1, false);


--
-- Name: status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.status_id_seq', 3, true);


--
-- Name: workshop_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.workshop_id_seq', 1, false);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- Name: hackathon_category hackathon_category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_category
    ADD CONSTRAINT hackathon_category_pkey PRIMARY KEY (id);


--
-- Name: hackathon_item hackathon_item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_item
    ADD CONSTRAINT hackathon_item_pkey PRIMARY KEY (id);


--
-- Name: hackathon hackathon_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon
    ADD CONSTRAINT hackathon_pkey PRIMARY KEY (id);


--
-- Name: hackathon_workshop hackathon_workshop_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_workshop
    ADD CONSTRAINT hackathon_workshop_pkey PRIMARY KEY (id);


--
-- Name: item item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_pkey PRIMARY KEY (id);


--
-- Name: status status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.status
    ADD CONSTRAINT status_pkey PRIMARY KEY (id);


--
-- Name: workshop workshop_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workshop
    ADD CONSTRAINT workshop_pkey PRIMARY KEY (id);


--
-- Name: hackathon_category hackathon_category_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_category
    ADD CONSTRAINT hackathon_category_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.category(id);


--
-- Name: hackathon_category hackathon_category_hackathon_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_category
    ADD CONSTRAINT hackathon_category_hackathon_id_fkey FOREIGN KEY (hackathon_id) REFERENCES public.hackathon(id);


--
-- Name: hackathon_item hackathon_item_hackathon_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_item
    ADD CONSTRAINT hackathon_item_hackathon_id_fkey FOREIGN KEY (hackathon_id) REFERENCES public.hackathon(id);


--
-- Name: hackathon_item hackathon_item_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_item
    ADD CONSTRAINT hackathon_item_item_id_fkey FOREIGN KEY (item_id) REFERENCES public.item(id);


--
-- Name: hackathon hackathon_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon
    ADD CONSTRAINT hackathon_status_id_fkey FOREIGN KEY (status_id) REFERENCES public.status(id);


--
-- Name: hackathon_workshop hackathon_workshop_hackathon_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_workshop
    ADD CONSTRAINT hackathon_workshop_hackathon_id_fkey FOREIGN KEY (hackathon_id) REFERENCES public.hackathon(id);


--
-- Name: hackathon_workshop hackathon_workshop_workshop_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hackathon_workshop
    ADD CONSTRAINT hackathon_workshop_workshop_id_fkey FOREIGN KEY (workshop_id) REFERENCES public.workshop(id);


--
-- PostgreSQL database dump complete
--

