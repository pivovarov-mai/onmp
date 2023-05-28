CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_oxygen_insufflation" (
  "id" SERIAL PRIMARY KEY,
  "parameter" VARCHAR(10) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_oxygen_insufflation" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Необходимость инсуффляции кислорода';
COMMENT ON COLUMN public."condition_assessment_protocol_oxygen_insufflation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_oxygen_insufflation".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_oxygen_insufflation".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_oxygen_insufflation" ("parameter", "points") VALUES
  ('Да', '1'),
  ('Нет', '0');