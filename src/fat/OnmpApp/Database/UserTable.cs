using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OnmpApp.Models.Database;

namespace OnmpApp.Database;

public static class UserTable
{
    private static async Task<bool> EmailExists(string email)
    {
        var cnt = await BaseDatabase.DB.Table<User>().Where(x => x.Email == email).CountAsync();
        return cnt > 0;
    }

    public static async Task<int> GetId(string email)
    {
        var cnt = await BaseDatabase.DB.Table<User>().Where(x => x.Email == email).FirstOrDefaultAsync();
        return cnt.Id;
    }

    public static async Task<bool> Insert(string email)
    {
        if (await EmailExists(email))
            return false;

        _ = await BaseDatabase.DB.InsertAsync(new User(email));
        return true;
    }
}
