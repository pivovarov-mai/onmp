-- Связующая таблица МКБ - Диагноз --
CREATE TABLE IF NOT EXISTS "mkb_diagnosis" (
  "id" SERIAL PRIMARY KEY NOT NULL,
  "mkb_id" INTEGER REFERENCES mkb(id) NOT NULL,
  "diagnosis_id" INTEGER REFERENCES diagnosis(id) NOT NULL
);

COMMENT ON TABLE public."mkb_diagnosis" IS 'Связующая таблица МКБ - Диагноз';
COMMENT ON COLUMN public."mkb_diagnosis".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."mkb_diagnosis".mkb_id IS 'Внешний ключ к таблице МКБ';
COMMENT ON COLUMN public."mkb_diagnosis".diagnosis_id IS 'Внешний ключ к таблице Диагноз';

INSERT INTO "mkb_diagnosis" ("mkb_id", "diagnosis_id") VALUES
  ('1', '1'),
  ('1', '2'),
  ('2', '3'),
  ('3', '4');
