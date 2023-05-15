CREATE TABLE IF NOT EXISTS "cards" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name" VARCHAR(64) NOT NULL,
  "date" DATE NOT NULL DEFAULT CURRENT_DATE,
  "order" VARCHAR(64) NOT NULL,
  "status" VARCHAR(8) NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'ready', 'archive', 'template')),
  "comment" VARCHAR(64),
  "user_id" INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user_profile(id)
);

COMMENT ON TABLE public."cards" IS 'Медицинские карты (листы осмотра)';
COMMENT ON COLUMN public."cards".id IS 'ID карты';
COMMENT ON COLUMN public."cards".name IS 'Название карты';
COMMENT ON COLUMN public."cards".date IS 'Дата вызова';
COMMENT ON COLUMN public."cards".order IS 'Номер наряда';
COMMENT ON COLUMN public."cards".status IS 'Статус карты (черновик, завершена, архивная, шаблон)';
COMMENT ON COLUMN public."cards".comment IS 'Комментарий';
COMMENT ON COLUMN public."cards".user_id IS 'Внешний ключ к таблице user_profile(ID врача)';