CREATE TABLE IF NOT EXISTS "newborn_apgar_criteria_muscle_tone" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(50) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."newborn_apgar_criteria_muscle_tone" IS 'Критерии оценки новорождённого по шкале Апгар - Мышечный тонус';
COMMENT ON COLUMN public."newborn_apgar_criteria_muscle_tone".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."newborn_apgar_criteria_muscle_tone".description IS 'Описание';
COMMENT ON COLUMN public."newborn_apgar_criteria_muscle_tone".point IS 'Балл';

INSERT INTO "newborn_apgar_criteria_muscle_tone" ("id", "description", "point") VALUES
  ('1', 'Атония', '0'),
  ('2', 'Низкий или умеренный, легкое сгибание конечностей', '1'),
  ('3', 'Нормальный с активными движениями', '2');