-- Теги заболеваний --
CREATE TABLE IF NOT EXISTS "mkb_tags" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name_tag" TEXT NOT NULL
);

COMMENT ON TABLE public."mkb_tags" IS 'Таблица тегов к заболеваниям';
COMMENT ON COLUMN public."mkb_tags".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."mkb_tags".name_tag IS 'Название тега';

INSERT INTO "mkb_tags" ("id", "name_tag") VALUES
  ('1', 'Терапия'),
  ('2', 'Кардиология'),
  ('3', 'Неврология'),
  ('4', 'Акушерство и гинекология'),
  ('5', 'Инфекционные заболевания'),
  ('6', 'Оториноларингология'),
  ('7', 'Офтальмология'),
  ('8', 'Стоматология'),
  ('9', 'Урология'),
  ('10', 'Хирургия и травматология'),
  ('11', 'Педиатрия и неонатология'),
  ('121', 'Терапия'),
  ('122', 'Кардиология'),
  ('123', 'Неврология'),
  ('124', 'Инфекционные заболевания'),
  ('125', 'Хирургия и Травматология'),
  ('126', 'Акушерство и гинекология'),
  ('127', 'Урология'),
  ('128', 'Оториноларингология'),
  ('129', 'Педиатрия'),
  ('1210', 'Стоматология');
