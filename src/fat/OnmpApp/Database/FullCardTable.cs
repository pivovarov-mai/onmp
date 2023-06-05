using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OnmpApp.Models.Database;

namespace OnmpApp.Database;

public static class FullCardTable
{
    public static async Task<bool> Update(FullCard card)
    {
        _ = await BaseDatabase.DB.UpdateAsync(card);
        return true;
    }
     
    public static async Task<bool> Remove(int id)
    {
        _ = await BaseDatabase.DB.DeleteAsync<FullCard>(id);
        return true;
    }

    public static async Task<FullCard> Get(int id)
    {
        try
        {
            var card = await BaseDatabase.DB.GetAsync<FullCard>(id);
            return card;
        }
        catch (Exception)
        {
            FullCard card = new()
            {
                Id = id
            };
            await BaseDatabase.DB.InsertAsync(card);
            return card;
        }
    }
}
