CREATE TABLE IF NOT EXISTS "diagnosis_tactics" (
  "id" SERIAL PRIMARY KEY NOT NULL,
  "diagnosis_id" INTEGER REFERENCES diagnosis(id) NOT NULL,
  "tactics_id" INTEGER REFERENCES tactics(id) NOT NULL
);

COMMENT ON TABLE public."diagnosis_tactics" IS 'Связующая таблица Диагноз - Тактика';
COMMENT ON COLUMN public."diagnosis_tactics".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."diagnosis_tactics".diagnosis_id IS 'Внешний ключ к таблице Диагноз';
COMMENT ON COLUMN public."diagnosis_tactics".tactics_id IS 'Внешний ключ к таблице Тактика';

INSERT INTO "diagnosis_tactics" ("diagnosis_id", "tactics_id") VALUES
  ('1', '1'),
  ('2', '2'),
  ('2', '3'),
  ('2', '4'),
  ('3', '5'),
  ('4', '6');