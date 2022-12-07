using SQLite;
using OnmpApp.Models;

namespace OnmpApp.Data;

public static partial class Database
{
    private static SQLiteAsyncConnection db;

    public static async Task Init()
    {
        if (db is not null)
            return;

        db = new SQLiteAsyncConnection(Settings.DatabasePath, Settings.DatabaseFlags);

        // Создание таблиц, если они не существуют
        var res = await db.CreateTableAsync<User>();
    }
}
