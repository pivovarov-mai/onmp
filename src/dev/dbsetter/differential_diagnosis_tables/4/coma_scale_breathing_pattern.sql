CREATE TABLE IF NOT EXISTS "coma_scale_breathing_pattern" (
  "id" SERIAL PRIMARY KEY,
  "sign" VARCHAR(55) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."coma_scale_breathing_pattern" IS 'Шкала комы FOUR - Дыхательный паттерн (R)';
COMMENT ON COLUMN public."coma_scale_breathing_pattern".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."coma_scale_breathing_pattern".sign IS 'Признак';
COMMENT ON COLUMN public."coma_scale_breathing_pattern".points IS 'Баллы';

INSERT INTO "coma_scale_breathing_pattern" ("sign", "points") VALUES
  ('Не интубирован, регулярное дыхание', '4'),
  ('Не интубирован, дыхание Чейна-Стокса', '3'),
  ('Не интубирован, нерегулярное дыхание', '2'),
  ('Сопротивляется аппарату ИВЛ', '1'),
  ('Полностью синхронизирован с аппаратом ИВЛ или апноэ', '0');