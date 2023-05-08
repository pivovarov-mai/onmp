CREATE TABLE IF NOT EXISTS "sub_diag_diagnosis" (
  "id" SERIAL PRIMARY KEY NOT NULL,
  "diagnosis_id" INTEGER REFERENCES diagnosis(id) NOT NULL,
  "sub_diagnosis_id" INTEGER REFERENCES sub_diagnosis(id) NOT NULL
);

COMMENT ON TABLE public."sub_diag_diagnosis" IS 'Связующая таблица Поддигноз - Диагноз';
COMMENT ON COLUMN public."sub_diag_diagnosis".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."sub_diag_diagnosis".diagnosis_id IS 'Внешний ключ к таблице Диагноз';
COMMENT ON COLUMN public."sub_diag_diagnosis".sub_diagnosis_id IS 'Внешний ключ к таблице Поддиагноз';

INSERT INTO "sub_diag_diagnosis" ("diagnosis_id", "sub_diagnosis_id") VALUES
  ('1', '1'),
  ('1', '2'),
  ('2', '3'),
  ('2', '4'),
  ('3', '5'),
  ('3', '6'),
  ('4', '7'),
  ('4', '8'),
  ('4', '9');