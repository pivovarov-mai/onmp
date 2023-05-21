CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_level_of_consciousness" (
  "id" SERIAL PRIMARY KEY,
  "parameter" VARCHAR(5) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_level_of_consciousness" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Изменение уровня сознания';
COMMENT ON COLUMN public."condition_assessment_protocol_level_of_consciousness".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_level_of_consciousness".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_level_of_consciousness".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_level_of_consciousness" ("parameter", "points") VALUES
  ('Нет', '0'),
  ('Есть', '3');