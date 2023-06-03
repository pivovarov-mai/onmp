CREATE TABLE IF NOT EXISTS "omp" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name_omp" TEXT NOT NULL
);

COMMENT ON TABLE public."omp" IS 'ОМП - Объем медицинской помощи';
COMMENT ON COLUMN public."omp".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."omp".name_omp IS 'Название ОМП - Объем медицинской помощи';

INSERT INTO "omp" ("id", "name_omp") VALUES
  ('1', 'ЭКГ'),
  ('2', 'Не требует антигипертензивной терапии  на этапе оказания неотложной медицинской помощи'),
  ('3', 'Каптоприл 12,5 - 25 мг или Моксонидин 0,4 мг сублингвально'),
  ('4', 'Контроль АД через 20 минут после терапии.'),
  ('5', 'ЭКГ'),
  ('6', 'Снижение АД выполнять постепенно, не более 20%: - Моксонидин 0,4 мг или Каптоприл 12,5 - 25 мг сублингвально или же при отсутствии эффекта: - Урапидил 12,5 - 25 мг в/венно медленно в течение 5 мин.'),
  ('7', 'Контроль АД во время введения препарата и через 20 минут после терапии.'),
  ('8', 'Метопролол 12,5 - 25 мг внутрь'),
  ('9', 'Моксонидин 0,4 мг сублингвально'),
  ('10', 'Кеторолак 30 мг в/мышечно'),
  ('11', 'ЭКГ'),
  ('12', 'Кеторолак 30 мг в/мышечно'),
  ('13', 'Не требует лечения на этапе оказания неотложной медицинской помощи'),
  ('14', 'Метопролол 12,5 - 25 мг внутрь'),
  ('15', 'Кеторолак 30 мг в/венно и/или парацетамол 500 мг внутрь'),
  ('16', 'Метоклопрамид 10 мг в/венно');