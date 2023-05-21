CREATE TABLE IF NOT EXISTS "newborn_apgar_criteria_muscle_tone" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(50) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."newborn_apgar_criteria_muscle_tone" IS 'Критерии оценки новорождённого по шкале Апгар - Мышечный тонус';
COMMENT ON COLUMN public."newborn_apgar_criteria_muscle_tone".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."newborn_apgar_criteria_muscle_tone".description IS 'Описание';
COMMENT ON COLUMN public."newborn_apgar_criteria_muscle_tone".point IS 'Балл';

INSERT INTO "newborn_apgar_criteria_muscle_tone" ("description", "point") VALUES
  ('Атония', '0'),
  ('Низкий или умеренный, легкое сгибание конечностей', '1'),
  ('Нормальный с активными движениями', '2');