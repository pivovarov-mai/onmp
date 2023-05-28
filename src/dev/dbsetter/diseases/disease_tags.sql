-- Теги заболеваний -- 
CREATE TABLE IF NOT EXISTS "disease_tags" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name_tag" TEXT NOT NULL
);

COMMENT ON TABLE public."disease_tags" IS 'Таблица тегов к заболеваниям';
COMMENT ON COLUMN public."disease_tags".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."disease_tags".name_tag IS 'Название тега';

INSERT INTO "disease_tags" ("id", "name_tag") VALUES
  ('1', 'Акушерство и гинекология'),
  ('2', 'Инфекционные заболевания'),
  ('3', 'Кардиология'),
  ('4', 'Неврология'),
  ('5', 'Педиатрия'),
  ('6', 'Пульмонология, эндокринология, терапия'),
  ('7', 'Реанимация, интенсивная терапия'),
  ('8', 'Токсикология, отравления'),
  ('9', 'Травмы'),
  ('10', 'Урология и нефрология'),
  ('11', 'Хирургия абдоминальная и сосудистая');