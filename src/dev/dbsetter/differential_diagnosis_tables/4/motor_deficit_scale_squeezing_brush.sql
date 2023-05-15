CREATE TABLE IF NOT EXISTS "motor_deficit_scale_squeezing_brush" (
  "id" SERIAL PRIMARY KEY,
  "sign" VARCHAR(35) NOT NULL,
  "points" INTEGER
);

COMMENT ON TABLE public."motor_deficit_scale_squeezing_brush" IS 'Шкала моторного дефицита LAMS (Los Angeles Motor Scale) - Сжимание в кисти';
COMMENT ON COLUMN public."motor_deficit_scale_squeezing_brush".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."motor_deficit_scale_squeezing_brush".sign IS 'Признак';
COMMENT ON COLUMN public."motor_deficit_scale_squeezing_brush".points IS 'Баллы';

INSERT INTO "motor_deficit_scale_squeezing_brush" ("sign", "points") VALUES
  ('Сила не снижена', '0'),
  ('Снижение силы', '1'),
  ('Не сжимает (нет движений в кисти)', '2');