using SQLite;
using OnmpApp.Models;
using OnmpApp.Properties;
using CommunityToolkit.Maui.Core.Extensions;
using Microsoft.Maui.ApplicationModel.Communication;
using System.Runtime.CompilerServices;
using System.Diagnostics;
using OnmpApp.Models.Database;

namespace OnmpApp.Database;

public static class BaseDatabase
{
    public static SQLiteAsyncConnection DB;

    public static async Task Init()
    {
        if (DB is not null)
            return;

        DB = new SQLiteAsyncConnection(Settings.DatabasePath, Settings.DatabaseFlags);

        // Создание таблиц, если они не существуют
        _ = await DB.CreateTableAsync<User>();
        _ = await DB.CreateTableAsync<Card>();
        _ = await DB.CreateTableAsync<FullCard>();
        _ = await DB.CreateTableAsync<Catalog>();
    }

}

