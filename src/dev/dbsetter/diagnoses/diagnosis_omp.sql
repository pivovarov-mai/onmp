CREATE TABLE IF NOT EXISTS "diagnosis_omp" (
  "id" SERIAL PRIMARY KEY NOT NULL,
  "diagnosis_id" INTEGER REFERENCES diagnosis(id) NOT NULL,
  "omp_id" INTEGER REFERENCES omp(id) NOT NULL
);

COMMENT ON TABLE public."diagnosis_omp" IS 'Связующая таблица Диагноз - ОМП(Объем медицинской помощи)';
COMMENT ON COLUMN public."diagnosis_omp".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."diagnosis_omp".diagnosis_id IS 'Внешний ключ к таблице Диагноз';
COMMENT ON COLUMN public."diagnosis_omp".omp_id IS 'Внешний ключ к таблице ОМП(Объем медицинской помощи)';

INSERT INTO "diagnosis_omp" ("diagnosis_id", "omp_id") VALUES
  ('1', '1'),
  ('2', '5'),
  ('2', '6'),
  ('2', '7'),
  ('4', '13');