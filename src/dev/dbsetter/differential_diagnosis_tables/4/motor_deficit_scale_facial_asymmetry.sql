CREATE TABLE IF NOT EXISTS "motor_deficit_scale_facial_asymmetry" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "sign" VARCHAR(5) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."motor_deficit_scale_facial_asymmetry" IS 'Шкала моторного дефицита LAMS (Los Angeles Motor Scale) - Ассиметрия лица';
COMMENT ON COLUMN public."motor_deficit_scale_facial_asymmetry".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."motor_deficit_scale_facial_asymmetry".sign IS 'Признак';
COMMENT ON COLUMN public."motor_deficit_scale_facial_asymmetry".points IS 'Баллы';

INSERT INTO "motor_deficit_scale_facial_asymmetry" ("id", "sign", "points") VALUES
  ('1', 'Нет', '0'),
  ('2', 'Да', '1');