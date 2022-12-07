using SQLite;

namespace OnmpApp;

public static class Settings
{
    #region App
    // Почта пользователя
    public static string Email
    {
        get => Preferences.Get(nameof(Email), string.Empty);
        set => Preferences.Set(nameof(Email), value);
    }

    // Пароль пользователя
    public static string Password
    {
        get => Preferences.Get(nameof(Password), string.Empty);
        set => Preferences.Set(nameof(Password), value);
    }

    // Статус: был ли пользователь успешно авторизован в приложение
    public static bool WasAuthorized
    {
        get => Preferences.Get(nameof(WasAuthorized), false); 
        set => Preferences.Set(nameof(WasAuthorized), value);
    }

    #endregion


    #region Database
    // Название БД
    public const string DatabaseFilename = "onmp.db3";

    // Путь к БД
    public static string DatabasePath => GetPath();

    private static string GetPath()
    {
        try
        {
            return Path.Combine(FileSystem.AppDataDirectory, DatabaseFilename);
        }
        catch
        {
            // Необходимо для тестирования
            return Path.Combine(@"C:\OnmpApp", DatabaseFilename);
        }
    }

    // Флаги для инициализации БД
    public const SQLiteOpenFlags DatabaseFlags =
        // Открыть БД на чтение и запись
        SQLiteOpenFlags.ReadWrite |
        // Создать БД, если не существует
        SQLiteOpenFlags.Create |
        // Включить мультипоточный доступ к БД
        SQLiteOpenFlags.SharedCache;

    #endregion
}