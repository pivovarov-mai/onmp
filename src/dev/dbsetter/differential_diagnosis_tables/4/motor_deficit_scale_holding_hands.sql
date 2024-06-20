CREATE TABLE IF NOT EXISTS "motor_deficit_scale_holding_hands" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "sign" VARCHAR(15) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."motor_deficit_scale_holding_hands" IS 'Шкала моторного дефицита LAMS (Los Angeles Motor Scale) - Удержание рук';
COMMENT ON COLUMN public."motor_deficit_scale_holding_hands".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."motor_deficit_scale_holding_hands".sign IS 'Признак';
COMMENT ON COLUMN public."motor_deficit_scale_holding_hands".points IS 'Баллы';

INSERT INTO "motor_deficit_scale_holding_hands" ("id", "sign", "points") VALUES
  ('1', 'Норма', '0'),
  ('2', 'Опускается вниз', '1'),
  ('3', 'Быстро падает', '2');