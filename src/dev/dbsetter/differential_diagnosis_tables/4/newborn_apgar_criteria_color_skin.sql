CREATE TABLE IF NOT EXISTS "newborn_apgar_criteria_color_skin" (
  "id" SERIAL PRIMARY KEY,
  "description" VARCHAR(30) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."newborn_apgar_criteria_color_skin" IS 'Критерии оценки новорождённого по шкале Апгар - Цвет кожи';
COMMENT ON COLUMN public."newborn_apgar_criteria_color_skin".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."newborn_apgar_criteria_color_skin".description IS 'Описание';
COMMENT ON COLUMN public."newborn_apgar_criteria_color_skin".point IS 'Балл';

INSERT INTO "newborn_apgar_criteria_color_skin" ("description", "point") VALUES
  ('Бледный или диффузный цианоз', '0'),
  ('Акроцианоз', '1'),
  ('Розовый', '2');