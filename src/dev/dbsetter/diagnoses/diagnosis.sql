CREATE TABLE IF NOT EXISTS "diagnosis" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name_diagnosis" TEXT NOT NULL,
  "recommendations_diagnosis" TEXT NOT NULL
);

COMMENT ON TABLE public."diagnosis" IS 'Диагноз';
COMMENT ON COLUMN public."diagnosis".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."diagnosis".name_diagnosis IS 'Название диагноза';
COMMENT ON COLUMN public."diagnosis".recommendations_diagnosis IS 'Рекомендации диагноза';

INSERT INTO "diagnosis" ("id", "name_diagnosis", "recommendations_diagnosis") VALUES
  ('1', 'Гипертоническая болезнь (вне криза)', 'Контроль уровня АД; Прием назначенной антигипертензивной терапии'),
  ('2', 'Гипертонический криз неосложненный', 'Рекомендаций нет'),
  ('3', 'Болезни костно-мышечной системы и соединительной тканей (артрозы, артриты и т.д.)', 'Рекомендации: прием НПВС при отсутствии противопоказаний со стороны ЖКТ.'),
  ('4', 'Расстройства вегетативной нервной системы', 'Рекомендаций нет');