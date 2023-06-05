using OnmpApp.Models.Database;
using SQLite;

namespace OnmpApp.Properties;

public static class Settings
{
    public const char FieldDelimeter = '\u2E2F';
    public const char PropertyDelimeter = '\u2E2E';

    #region App

    // Почта пользователя
    public static string Email
    {
        get => Preferences.Get(nameof(Email), string.Empty);
        set => Preferences.Set(nameof(Email), value);
    }

    // Id пользователя
    public static int UserId
    {
        get => Preferences.Get(nameof(UserId), -1);
        set => Preferences.Set(nameof(UserId), value);
    }

    // Пароль пользователя
    public static string Password
    {
        get => Preferences.Get(nameof(Password), string.Empty);
        set => Preferences.Set(nameof(Password), value);
    }

    // Токен пользователя
    public static string Token
    {
        get => Preferences.Get(nameof(Token), string.Empty);
        set => Preferences.Set(nameof(Token), value);
    }

    // Статус: был ли пользователь успешно авторизован в приложение
    public static bool WasAuthorized
    {
        get => Preferences.Get(nameof(WasAuthorized), false);
        set => Preferences.Set(nameof(WasAuthorized), value);
    }

    // Дата авторизации
    public static DateTime AuthorizedDate
    {
        get => Preferences.Get(nameof(AuthorizedDate), DateTime.Now);
        set => Preferences.Set(nameof(AuthorizedDate), value);
    }

    // Адрес сервера
    public static string ApiAddress => "https://apu-hd.fun/api/v1";

    #endregion


    #region Database

    // Название БД
    private const string DatabaseFilename = "onmpApp.db3";

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

    // Дата синхронизации справочников
    public static DateTime CatalogSyncDate
    {
        get => Preferences.Get(nameof(CatalogSyncDate), DateTime.Now);
        set => Preferences.Set(nameof(CatalogSyncDate), value);
    }

    #endregion
}