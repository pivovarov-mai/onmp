CREATE TABLE IF NOT EXISTS "muscle_strength_assessment" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "point" INTEGER NOT NULL,
  "note" VARCHAR(110) NOT NULL
);

COMMENT ON TABLE public."muscle_strength_assessment" IS 'Оценка мышечной силы по баллам';
COMMENT ON COLUMN public."muscle_strength_assessment".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."muscle_strength_assessment".point IS 'Балл';
COMMENT ON COLUMN public."muscle_strength_assessment".note IS 'Примечание';

INSERT INTO "muscle_strength_assessment" ("id", "point", "note") VALUES
  ('1', '0', 'Сокращение мышц отсутствует'),
  ('2', '1', 'Едва условимое сокращение'),
  ('3', '2', 'Активное движение возможно, но не преодолевает собственную силу тяжести'),
  ('4', '3', 'Активное движение преодолевает собственную силу тяжести'),
  ('5', '4', 'Активное движение преодолевает собственную силу тяжести и споротивление врача'),
  ('6', '5', 'Нормальная мышечная сила, движения не ограничены по основным направлениям, преодолевают сопротивления врача');