CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_breathing_rate" (
  "id" SERIAL PRIMARY KEY,
  "parameter" VARCHAR(10) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_breathing_rate" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Частота дыхания за 1 минуту';
COMMENT ON COLUMN public."condition_assessment_protocol_breathing_rate".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_breathing_rate".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_breathing_rate".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_breathing_rate" ("parameter", "points") VALUES
  ('<= 8', '3'),
  ('9-11', '1'),
  ('12-20', '0'),
  ('21-24', '2'),
  ('>= 25', '3');