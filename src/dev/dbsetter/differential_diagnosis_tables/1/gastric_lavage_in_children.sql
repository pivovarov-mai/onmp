CREATE TABLE IF NOT EXISTS "gastric_lavage_in_children" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "age" VARCHAR(15) NOT NULL,
  "one_time_volume" VARCHAR(20) NOT NULL,
  "maximum_flushing_volume" VARCHAR(15) NOT NULL
);

COMMENT ON TABLE public."gastric_lavage_in_children" IS 'Промывание желудка у детей';
COMMENT ON COLUMN public."gastric_lavage_in_children".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."gastric_lavage_in_children".age IS 'Возраст';
COMMENT ON COLUMN public."gastric_lavage_in_children".one_time_volume IS 'Разовый объем, в мл';
COMMENT ON COLUMN public."gastric_lavage_in_children".maximum_flushing_volume IS 'Максимальный объём промывания, в мл';

INSERT INTO "gastric_lavage_in_children" ("id", "age", "one_time_volume", "maximum_flushing_volume") VALUES
  ('1', 'Новорожденные:', '10-12 мл/кг веса', '50-100'),
  ('2', '1 неделя жизни', '10-12 мл/кг веса', '50-100'),
  ('3', '2 неделя жизни', '10-12 мл/кг веса', '50-100'),
  ('4', '3 неделя жизни', '10-12 мл/кг веса', '100-150'),
  ('5', '4 неделя жизни', '10-12 мл/кг веса', '150-200'),
  ('6', '1-2 месяца', '60-90', '200-250'),
  ('7', '3-4 месяца', '90-100', '300-400'),
  ('8', '5-6 месяцев', '100-110', '400-500'),
  ('9', '7-8 месяцев', '110-120', '600-700'),
  ('10', '9-12 месяцев', '120-150', '800-900'),
  ('11', '2-3 года', '200-250', '1-1,5 л'),
  ('12', '4-5 лет', '300-350', '1,5-2 л'),
  ('13', '6-7 лет', '350-400', '2,5-3 л'),
  ('14', '8-11 лет', '400-450', '3,5-4 л'),
  ('15', '12-14 лет', '450-500', '4-4,5 л');