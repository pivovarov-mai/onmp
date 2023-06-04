CREATE TABLE IF NOT EXISTS "cards" (
  "id" SERIAL PRIMARY KEY NOT NULL,
  "name" VARCHAR(64) NOT NULL,
  "date" DATE DEFAULT CURRENT_DATE,
  "order" VARCHAR(64) NOT NULL,
  "status" VARCHAR(8) DEFAULT 'draft' CHECK (status IN ('draft', 'ready', 'archive', 'template')),
  "comment" VARCHAR(64),
  "account_user_id" INTEGER REFERENCES account_user(id) NOT NULL
);

COMMENT ON TABLE public."cards" IS 'Медицинские карты (листы осмотра)';
COMMENT ON COLUMN public."cards".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."cards".name IS 'Название карты';
COMMENT ON COLUMN public."cards".date IS 'Дата создания';
COMMENT ON COLUMN public."cards".order IS 'Номер наряда';
COMMENT ON COLUMN public."cards".status IS 'Статус карты (черновик, завершена, архивная, шаблон)';
COMMENT ON COLUMN public."cards".comment IS 'Комментарий к карте';
COMMENT ON COLUMN public."cards".account_user_id IS 'Внешний ключ к таблице user_profile(ID врача)';