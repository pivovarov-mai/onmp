CREATE TABLE IF NOT EXISTS "newborn_apgar_criteria_color_skin" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "description" VARCHAR(30) NOT NULL,
  "point" INTEGER NOT NULL
);

COMMENT ON TABLE public."newborn_apgar_criteria_color_skin" IS 'Критерии оценки новорождённого по шкале Апгар - Цвет кожи';
COMMENT ON COLUMN public."newborn_apgar_criteria_color_skin".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."newborn_apgar_criteria_color_skin".description IS 'Описание';
COMMENT ON COLUMN public."newborn_apgar_criteria_color_skin".point IS 'Балл';

INSERT INTO "newborn_apgar_criteria_color_skin" ("id", "description", "point") VALUES
  ('1', 'Бледный или диффузный цианоз', '0'),
  ('2', 'Акроцианоз', '1'),
  ('3', 'Розовый', '2');