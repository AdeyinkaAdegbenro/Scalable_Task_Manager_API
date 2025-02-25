--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22
-- Dumped by pg_dump version 12.22

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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: adeyinkaadegbenro
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO adeyinkaadegbenro;

--
-- Name: tasks; Type: TABLE; Schema: public; Owner: adeyinkaadegbenro
--

CREATE TABLE public.tasks (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    description character varying(30) NOT NULL,
    priority character varying(30) NOT NULL,
    due_date timestamp without time zone NOT NULL,
    done boolean NOT NULL,
    user_id integer NOT NULL,
    created_at timestamp without time zone NOT NULL
);


ALTER TABLE public.tasks OWNER TO adeyinkaadegbenro;

--
-- Name: tasks_id_seq; Type: SEQUENCE; Schema: public; Owner: adeyinkaadegbenro
--

CREATE SEQUENCE public.tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tasks_id_seq OWNER TO adeyinkaadegbenro;

--
-- Name: tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adeyinkaadegbenro
--

ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: adeyinkaadegbenro
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(30) NOT NULL,
    password_hash character varying(300) NOT NULL,
    created_at timestamp without time zone NOT NULL,
    email character varying(30) DEFAULT 'adeyinkaadegbenro@gmail.com'::character varying NOT NULL
);


ALTER TABLE public.users OWNER TO adeyinkaadegbenro;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: adeyinkaadegbenro
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO adeyinkaadegbenro;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adeyinkaadegbenro
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: tasks id; Type: DEFAULT; Schema: public; Owner: adeyinkaadegbenro
--

ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: adeyinkaadegbenro
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: adeyinkaadegbenro
--

COPY public.alembic_version (version_num) FROM stdin;
574b9b8bb688
\.


--
-- Data for Name: tasks; Type: TABLE DATA; Schema: public; Owner: adeyinkaadegbenro
--

COPY public.tasks (id, name, description, priority, due_date, done, user_id, created_at) FROM stdin;
2	Write Docs	Document API endpoints	Medium	2025-02-17 00:00:00	f	1	2025-02-09 15:56:38.017083
4	Deploy App	Deploy to production	Medium	2025-02-19 00:00:00	f	2	2025-02-09 15:56:38.017083
5	Set Up CI/CD	Automate deployment	High	2025-02-18 00:00:00	f	3	2025-02-09 15:56:38.017083
3	Optimize DB	Improve query performance	High	2025-02-05 00:00:00	f	2	2025-02-09 15:56:38.017083
8	Buy Milk	Great milk	Minor	2025-02-09 18:57:02.006278	f	8	2025-02-09 18:56:20.089232
1	Build API	Develop task management API	High	2025-02-15 00:00:00	f	8	2025-02-09 15:56:38.017083
9	Buy beans	Great beans	Major	2025-02-10 00:00:00	f	8	2025-02-09 19:06:35.763232
6	Buy meat	Great meat	Major	2025-09-18 00:00:00	f	8	2025-02-09 18:53:52.666552
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: adeyinkaadegbenro
--

COPY public.users (id, username, password_hash, created_at, email) FROM stdin;
1	yvonnek	hashedpassword1	2025-02-09 15:56:09.605319	adeyinkaadegbenro@gmail.com
3	coderx	hashedpassword3	2025-02-09 15:56:09.605319	adeyinkaadegbenro@gmail.com
4	backendpro	hashedpassword4	2025-02-09 15:56:09.605319	adeyinkaadegbenro@gmail.com
5	taskmaster	hashedpassword5	2025-02-09 15:56:09.605319	adeyinkaadegbenro@gmail.com
2	devmaster	hashedpassword2	2025-02-09 15:56:09.605319	adeyinkaadegbenro1@gmail.com
8	admin	scrypt:32768:8:1$fBu26QKxlYNWE8mV$bcb613ebc236c08b3e347577d0a55bdd6dcd906ab10a914767fbe72c8a4911adab97d780f6f2227dee01bb0f58f8d2905715cee969a6183509ab564ca7ca49e5	2025-02-13 13:25:14.075906	ade@fr.cd
\.


--
-- Name: tasks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adeyinkaadegbenro
--

SELECT pg_catalog.setval('public.tasks_id_seq', 11, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adeyinkaadegbenro
--

SELECT pg_catalog.setval('public.users_id_seq', 8, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: adeyinkaadegbenro
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: tasks tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: adeyinkaadegbenro
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: adeyinkaadegbenro
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: done_equals_false; Type: INDEX; Schema: public; Owner: adeyinkaadegbenro
--

CREATE INDEX done_equals_false ON public.tasks USING btree (done) WHERE (done = false);


--
-- Name: ix_tasks_due_date; Type: INDEX; Schema: public; Owner: adeyinkaadegbenro
--

CREATE INDEX ix_tasks_due_date ON public.tasks USING btree (due_date);


--
-- Name: ix_tasks_user_id; Type: INDEX; Schema: public; Owner: adeyinkaadegbenro
--

CREATE INDEX ix_tasks_user_id ON public.tasks USING btree (user_id);


--
-- Name: ix_users_username; Type: INDEX; Schema: public; Owner: adeyinkaadegbenro
--

CREATE UNIQUE INDEX ix_users_username ON public.users USING btree (username);


--
-- Name: unique_task_name_per_user; Type: INDEX; Schema: public; Owner: adeyinkaadegbenro
--

CREATE UNIQUE INDEX unique_task_name_per_user ON public.tasks USING btree (name, user_id);


--
-- Name: tasks tasks_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adeyinkaadegbenro
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

