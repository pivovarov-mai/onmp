CREATE TABLE IF NOT EXISTS "condition_assessment_protocol_blood_oxygen_saturation" (
  "id" SERIAL PRIMARY KEY,
  "parameter" VARCHAR(10) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."condition_assessment_protocol_blood_oxygen_saturation" IS 'Проктокол оценки тяжести состояния пациента (NEWS) - Насыщение крови кислородом, %)';
COMMENT ON COLUMN public."condition_assessment_protocol_blood_oxygen_saturation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."condition_assessment_protocol_blood_oxygen_saturation".parameter IS 'Параметр';
COMMENT ON COLUMN public."condition_assessment_protocol_blood_oxygen_saturation".points IS 'Расшифровка баллов';

INSERT INTO "condition_assessment_protocol_blood_oxygen_saturation" ("parameter", "points") VALUES
  ('<= 91', '3'),
  ('92-93', '2'),
  ('94-95', '1'),
  ('>= 96', '0');