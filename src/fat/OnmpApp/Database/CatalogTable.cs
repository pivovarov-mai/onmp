using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OnmpApp.Models.Database;

namespace OnmpApp.Database;


public class SearchParameters
{
    public string SearchParam { get; set; }
    public int Skip { get; set; }
    public int Take { get; set; }
}

public static class CatalogTable
{
    public static async Task<List<CatalogShort>> Search(string search, int skip, int take)
    {
        string query = "SELECT Name, ElType, CASE WHEN Text IS NULL THEN 0 ELSE 1 END AS Loaded " +
               "FROM Catalogs " +
               "WHERE LowerName LIKE ? " +
               "ORDER BY Name " +
               "LIMIT ? OFFSET ?";
        var res = await BaseDatabase.DB.QueryAsync<CatalogShort>(query, $"%{search.ToLower()}%", take, skip);
        return res.ToList();
    }

    public static async Task<Catalog> Get(string name)
    {
        return await BaseDatabase.DB.Table<Catalog>().Where(el => el.Name == name).FirstOrDefaultAsync();
    }

    public static async Task<int> Count()
    {
        return await BaseDatabase.DB.Table<Catalog>().CountAsync();
    }

    public static async Task<bool> Update(Catalog catalog)
    {
        _ = await BaseDatabase.DB.UpdateAsync(catalog);
        return true;
    }

    public static async Task<bool> Insert(string name, CatalogType type, string text=null)
    {
        _ = await BaseDatabase.DB.InsertAsync(new Catalog
        {
            Name = name,
            ElType = type,
            Text = text,
            LowerName = name.ToLower()
        });
        return true;
    }
}
