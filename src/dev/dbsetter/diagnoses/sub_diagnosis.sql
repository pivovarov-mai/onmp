CREATE TABLE IF NOT EXISTS "sub_diagnosis" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name_sub_diagnosis" TEXT NOT NULL,
  "recommendations" TEXT NOT NULL
);

COMMENT ON TABLE public."sub_diagnosis" IS 'Поддиагноз';
COMMENT ON COLUMN public."sub_diagnosis".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."sub_diagnosis".name_sub_diagnosis IS 'Название поддиагноза';
COMMENT ON COLUMN public."sub_diagnosis".recommendations IS 'Рекомендации';

INSERT INTO "sub_diagnosis" ("id", "name_sub_diagnosis", "recommendations") VALUES
  ('1', 'При повышении САД не более чем на 20 мм. рт. ст. от привычного', 'Рекомендаций нет'),
  ('2', 'При повышении САД более чем на 20 мм. рт. ст. от привычного', 'Рекомендаций нет'),
  ('3', 'При тахикардии (ЧСС > 100 в минуту)', 'Рекомендаций нет'),
  ('4', 'При хронической почечной недостаточности', 'Противопоказаны: ингибиторы АПФ и мочегонные'),
  ('5', 'При боли', 'Рекомендаций нет'),
  ('6', 'При боли в спине и грудной клетке', 'Рекомендаций нет'),
  ('7', 'При тахикардии', 'Рекомендаций нет'),
  ('8', 'При головной боли', 'Рекомендаций нет'),
  ('9', 'При рвоте и/или тошноте', 'Рекомендаций нет');