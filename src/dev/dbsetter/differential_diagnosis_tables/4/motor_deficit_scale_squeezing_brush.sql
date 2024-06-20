CREATE TABLE IF NOT EXISTS "motor_deficit_scale_squeezing_brush" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "sign" VARCHAR(35) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."motor_deficit_scale_squeezing_brush" IS 'Шкала моторного дефицита LAMS (Los Angeles Motor Scale) - Сжимание в кисти';
COMMENT ON COLUMN public."motor_deficit_scale_squeezing_brush".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."motor_deficit_scale_squeezing_brush".sign IS 'Признак';
COMMENT ON COLUMN public."motor_deficit_scale_squeezing_brush".points IS 'Баллы';

INSERT INTO "motor_deficit_scale_squeezing_brush" ("id", "sign", "points") VALUES
  ('1', 'Сила не снижена', '0'),
  ('2', 'Снижение силы', '1'),
  ('3', 'Не сжимает (нет движений в кисти)', '2');