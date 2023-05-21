CREATE TABLE IF NOT EXISTS "motor_deficit_scale_facial_asymmetry" (
  "id" SERIAL PRIMARY KEY,
  "sign" VARCHAR(5) NOT NULL,
  "points" INTEGER
);

COMMENT ON TABLE public."motor_deficit_scale_facial_asymmetry" IS 'Шкала моторного дефицита LAMS (Los Angeles Motor Scale) - Ассиметрия лица';
COMMENT ON COLUMN public."motor_deficit_scale_facial_asymmetry".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."motor_deficit_scale_facial_asymmetry".sign IS 'Признак';
COMMENT ON COLUMN public."motor_deficit_scale_facial_asymmetry".points IS 'Баллы';

INSERT INTO "motor_deficit_scale_facial_asymmetry" ("sign", "points") VALUES
  ('Нет', '0'),
  ('Да', '1');