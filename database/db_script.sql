CREATE TABLE public.variables (
    key text PRIMARY KEY,
    value text NOT NULL
);

ALTER TABLE public.variables OWNER TO postgres;
