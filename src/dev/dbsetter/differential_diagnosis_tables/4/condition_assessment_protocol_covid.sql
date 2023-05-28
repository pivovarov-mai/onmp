CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_covid" (
  "id" SERIAL PRIMARY KEY,
  "parameter" VARCHAR(30) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_covid" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Пациент с COVID-19';
COMMENT ON COLUMN public."condition_assessment_protocol_covid".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_covid".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_covid".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_covid" ("parameter", "points") VALUES
  ('Подтверждено позитивный', '0'),
  ('Подозрительный', '0'),
  ('Маловероятно', '0'),
  ('Подтверждено отрицательный', '0');