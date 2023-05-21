CREATE TABLE IF NOT EXISTS "motor_deficit_scale_holding_hands" (
  "id" SERIAL PRIMARY KEY,
  "sign" VARCHAR(15) NOT NULL,
  "points" INTEGER
);

COMMENT ON TABLE public."motor_deficit_scale_holding_hands" IS 'Шкала моторного дефицита LAMS (Los Angeles Motor Scale) - Удержание рук';
COMMENT ON COLUMN public."motor_deficit_scale_holding_hands".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."motor_deficit_scale_holding_hands".sign IS 'Признак';
COMMENT ON COLUMN public."motor_deficit_scale_holding_hands".points IS 'Баллы';

INSERT INTO "motor_deficit_scale_holding_hands" ("sign", "points") VALUES
  ('Норма', '0'),
  ('Опускается вниз', '1'),
  ('Быстро падает', '2');