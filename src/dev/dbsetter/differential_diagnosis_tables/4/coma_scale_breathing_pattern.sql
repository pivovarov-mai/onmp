CREATE TABLE IF NOT EXISTS "coma_scale_breathing_pattern" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "sign" VARCHAR(55) NOT NULL,
  "points" INTEGER NOT NULL
);

COMMENT ON TABLE public."coma_scale_breathing_pattern" IS 'Шкала комы FOUR - Дыхательный паттерн (R)';
COMMENT ON COLUMN public."coma_scale_breathing_pattern".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."coma_scale_breathing_pattern".sign IS 'Признак';
COMMENT ON COLUMN public."coma_scale_breathing_pattern".points IS 'Баллы';

INSERT INTO "coma_scale_breathing_pattern" ("id", "sign", "points") VALUES
  ('1', 'Не интубирован, регулярное дыхание', '4'),
  ('2', 'Не интубирован, дыхание Чейна-Стокса', '3'),
  ('3', 'Не интубирован, нерегулярное дыхание', '2'),
  ('4', 'Сопротивляется аппарату ИВЛ', '1'),
  ('5', 'Полностью синхронизирован с аппаратом ИВЛ или апноэ', '0');