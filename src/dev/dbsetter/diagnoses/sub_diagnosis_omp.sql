CREATE TABLE IF NOT EXISTS "sub_diagnosis_omp" (
  "id" SERIAL PRIMARY KEY NOT NULL,
  "sub_diagnosis_id" INTEGER REFERENCES sub_diagnosis(id) NOT NULL,
  "omp_id" INTEGER REFERENCES omp(id) NOT NULL
);

COMMENT ON TABLE public."sub_diagnosis_omp" IS 'Связующая таблица Поддиагноз - ОМП - Объем медицинской помощи ';
COMMENT ON COLUMN public."sub_diagnosis_omp".sub_diagnosis_id IS 'Внешний ключ к таблице Поддиагноз';
COMMENT ON COLUMN public."sub_diagnosis_omp".omp_id IS 'Внешний ключ к таблице ОМП - Объем медицинской помощи';

INSERT INTO "sub_diagnosis_omp" ("sub_diagnosis_id", "omp_id") VALUES
  ('1', '2'),
  ('2', '3'),
  ('2', '4'),
  ('3', '8'),
  ('4', '9'),
  ('5', '10'),
  ('6', '11'),
  ('6', '12'),
  ('7', '14'),
  ('8', '15'),
  ('9', '16');